import os
from datetime import datetime
import sys
import subprocess

CLASS = "spring2023"

if len(sys.argv) != 2:
    lectureName = ""
else:
    lectureName = sys.argv[1]

date = datetime.now()
# list all directories in the current directory
print("Which class is this lecture for?")

j = 1
d = [
    f for f in os.listdir(f'/Users/owenoertell/Documents/School/{CLASS}')
    if (not f.startswith('.'))
]

for i in d:
    print(j, i)
    j += 1

# Prompt for number of semester
semester = int(input("#? "))

os.chdir(f"/Users/owenoertell/Documents/School/{CLASS}/" + d[semester - 1] +
         "/lectures")

today = date.strftime('%a %d %b %Y %H:%M')

# get most recent lecture
# list all files in the current directory
files = [f for f in os.listdir('.') if (os.path.isfile(f) and "lec_" in f)]
if (len(files) == 0):
    lectureNumber = 1
else:
    files = [f[4:] for f in files]
    files = [f[:-4] for f in files]
    files = [int(f) for f in files]
    newFile = max(files)
    lectureNumber = newFile + 1

lecString = "lec_" + str(lectureNumber).zfill(2) + ".tex"
# make new file for the lecture
f = open(lecString, "w")
f.write(f'\\lecture{{{lectureNumber}}}{{{today}}}{{{lectureName}}}\n')
f.close()

# add new lecture to master.tex
# seek to "% end lectures

# open master.tex file and read all lines
f = open("master.tex", "r+")
lines = f.readlines()
# find the line that starts with "% end lectures
index = [idx for idx, s in enumerate(lines) if '% end lectures' in s][0]
lines.insert(index, f'\\input{{{lecString}}}\n')
# write all lines back to master.tex
f.seek(0)
f.writelines(lines)
f.truncate()
f.close()

print("Lecture added.")
print(
    f"Run to edit:\n nvim /Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/{lecString}"
)
input("Press enter to continue...")
# start watching file for editing and compile
print("compiling master pdf...")

# check if process fswatch is running
subprocess.run("inkscape-figures watch", shell=True)

# check if master.tex is already compiled
if (not os.path.isfile(
        f"/Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/master.pdf"
)):
    subprocess.run(
        f"pdflatex /Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/master.tex",
        shell=True,
        cwd=str(
            f"/Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/"
        ))

print("Starting zathura and latexmk...")

process = subprocess.Popen([
    f'zathura /Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/master.pdf',
],
                           stdin=None,
                           stdout=None,
                           stderr=None,
                           shell=True)

result = subprocess.run(
    f"latexmk -f -pvc -pdf -view=none -interaction=nonstopmode /Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/master.tex",
    cwd=str(
        f"/Users/owenoertell/Documents/School/{CLASS}/{d[semester - 1]}/lectures/"
    ),
    shell=True)
