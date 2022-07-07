import os
# list all directories in the current directory
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

# change directories into the semester
os.chdir("/Users/owenoertell/Documents/School/" + d[semester - 1])

className = input("What is the course number of the class? (eg. cs2110)\n")
# create new folder for the class
os.mkdir(className)
# change directories into the class
os.chdir(className)

os.mkdir("lectures")
os.mkdir("homework")

os.chdir("lectures")

classTitle = input(
    "What is the title of the class? (eg. Computer Organization and Programming)\n"
)

# add template to file
f = open("master.tex", "w")

f.write("\\documentclass[a4paper]{report}\n")
f.write(
    "\\input{/Users/owenoertell/Documents/School/notes-scripting/preamble.tex}\n"
)
f.write("\\title{" + classTitle + "}\n")
f.write("\\begin{document}\n")
f.write("\\maketitle\n")
f.write("\\tableofcontents\n")
f.write("\\newpage\n")
f.write("% start lectures\n")
f.write("% end lectures\n")
f.write("\end{document}\n")

f.close()

f = open("info.yaml", "w")
f.write("title: " + classTitle)
f.write("\n")
f.write("name: " + className)
f.write("\n")
f.write("semester: " + d[semester - 1])
f.write("\n")