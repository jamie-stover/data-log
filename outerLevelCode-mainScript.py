""""
Feed pictures into Lasix PDF generator and delete source picture. Move and rename outputted PDF.
Run from command line.

Requires script be in a folder with screenShots and FinishedPDFs adjacent.
"""

#  Rename images -- DONE (Files lose extension specifier. Not sure whether that's a problem for Latex.)
#  Run summaryGen -- DONE
#  Delete images -- DONE # Better to move?
#  Move and rename summary PDF -- DONE



import os
import datetime

currentScriptLocation = str(os.path.dirname(os.path.abspath(__file__)))  # Give script location

def rename(dir="screenShots/"):
    """
    Rename all files in a directory to a series of integers starting at 0 arranged alphabetically. Argument dir
    specifies relative location of folder.

    """
    filesNames = os.listdir(dir[:-1])  # Remove /
    i = 0
    while i < len(filesNames):
        os.rename(dir + filesNames[i], dir + str(i) + ".png")  # Does this output need to be png?
        i += 1


def callLatex():  # Specifying will be a problem.
    """ Effectively run a latex file from command line. Argument is tex file location. """
    argument = "pdflatex " + currentScriptLocation + "/summaryGen"
    os.system(argument)


def delete():
    """ Delete all file in the relative directory specified by argument. """
    filesNames = os.listdir("screenShots")
    i = 0
    while i < len(filesNames):
        os.unlink("screenShots/" + str(i) + ".png")
        i += 1

    os.unlink("SummaryGen.log")  # These are the log files from the latex script
    os.unlink("SummaryGen.aux")  # Assume tex file name is SummaryGen


def move():
    """ Move and Rename a file to a time stamp. """
    timeStamp = datetime.datetime.now()
    newName = "FinishedPDFs/" + str(timeStamp)
    os.rename("SummaryGen.pdf", newName)


def main():
    """ """
    rename()
    callLatex()
    delete()
    move()

if __name__ == "__main__":
    main()
