import os
import subprocess

os.chdir("/Users/owenoertell/Documents/School/")
print("Which semester are you adding a class to?")

j = 1
d = [
    f for f in os.listdir('/Users/owenoertell/Documents/School/')
    if (not f.startswith('.') and f != 'notes-scripting')
]

for i in d:
    print(j, i)
    j += 1

# Prompt for number of semester
semester = int(input("#? "))

# loop through all dirs
for dir in [
        f for f in os.listdir(
            f'/Users/owenoertell/Documents/School/{d[semester - 1]}')
        if (not f.startswith('.') and f != 'notes-scripting')
]:
    print("Compiling " + dir + " ... ", end="")
    result = subprocess.run(
        f"pdflatex /Users/owenoertell/Documents/School/{d[semester - 1]}/{dir}/lectures/master.tex",
        shell=True,
        cwd=str(
            f"/Users/owenoertell/Documents/School/{d[semester - 1]}/{dir}/lectures/"
        ),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode != 0:
        print(f"Error compiling {dir}")
        continue
    else:
        print("done.")
