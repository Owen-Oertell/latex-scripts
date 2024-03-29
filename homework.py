import subprocess
import sys

directory = "."
if len(sys.argv) > 1:
    directory = sys.argv[1]
if len(sys.argv) > 2:
    addition = sys.argv[2]
else:
    addition = "homework.tex"

# add the homework.tex file to the directory
subprocess.run(
    "cp /Users/owenoertell/Documents/School/notes-scripting/neurips_2022.tex " +
    directory + "/" + addition,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    shell=True)

subprocess.run(
    "cp /Users/owenoertell/Documents/School/notes-scripting/neurips_2022.sty " +
    directory,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    shell=True)
