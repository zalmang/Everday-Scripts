import os
from datetime import date
import zfunctions as z


DOWNLOADS_PATH = "~/Downloads"

def main():
    return stage2(z.zinput("Are your files in Downloads?"))

def stage2(option):
    if option == 0:
        return enterPath(os.path.expanduser(DOWNLOADS_PATH))
    elif option == 1:
        path = input("Enter path (format: /Users/(zalmangagerman?)/...)\n")
    else:
        print(f"Invalid entry: {option}. Try again")
        return main()
    return enterPath(path)

def enterPath(path):
    qExists = os.path.exists(path)
    qIsFile = not os.path.isdir(path)
    if not qExists:
        print("Invalid path. Please try again.")
        return stage2(1)

    if qIsFile:
        fileName = path.split("/")[-1]
        if (not z.zinput(f"Is one of the files you want to rename {fileName}?")):
            return enterPath(input("Please enter the path of the folder that the new files exist: "))
    return decidePattern(path, qIsFile)

def decidePattern(directory, qIsFile):
    if (qIsFile):
        returnPatternBasedOnFileName(directory)
    else:
        if (z.zinput("Do you want to give your pattern now?")):
            pattern = input("Please enter the pattern")
            #to-do: check to make sure this is a valid pattern
            return rename(directory, pattern)
        if (z.zinput("Do you want to rename based on date?") == 1):
            if z.zinput("Did you download your files today?"):
                udate = date.today()
            else:
                #define dateInput()
                udate = input("What date did you download your files? (dd-mm-yyyy)")
                #convert to something python can understand
                #find a group of files with that date
            return returnPatternBasedOnDate(directory, udate)
        else:
            return userGivesFileName(directory)
        
            # os.path.getmtime(path) returns the last modified time
            # Add your logic here for processing the files
            
def userGivesFileName(directory):
    print(f"Looks like you want to do it by file name.")
    fileName = input(f"What's the name of one file you want to sort by? Remember, you're in {directory}.")
    if os.path.exists(f"{directory}/{fileName}" and not os.path.isdir(f"{directory}/{fileName}")):
        return returnPatternBasedOnFileName(f"{directory}/{fileName}")
    else:
        print("No such file. Lets' try again")
        return userGivesFileName(directory)


def rename(directory, pattern):
    pass

def returnPatternBasedOnDate(directory, dateStr):
    pass

def returnPatternBasedOnFileName(directoryWithFile):
    pass

main()

directory = os.path.expanduser("~/Downloads") # this is not correct
print(f"Directory: {directory}")

for i in range(18, 40):
    old_filename = f"Daily Hafez Haim Lesson Number 0{i}.mp3"
    new_filename = f"hlr {i}.mp3"
    old_path = os.path.join(directory, old_filename)
    new_path = os.path.join(directory, new_filename)


os.rename(old_path, new_path)

    #to add: copy the files in a holding tank in case there are errors
    #finding user input

""" different ways to locate similarly-named files:
    by extension
"""

"""
questions for the user:

0) is the directory in the downloads folder?
0.5) where they downloaded today.
    if not, what date were they downloaded (dd-mm-yyyy)
    and then ask, are these your files and print them out.
1) what is the string in common?
2) how are the strings sorted? from what number to what number?
3) where do you want the files to end up? 
    give options for same directory
    different drive (please detect this)


end: print out the folder on top and then a list of all of the renamed files, 
like this:
    Folder: ~/Downloads
    Daily Hafez Chaim 003.mp3 -> hlr 3.mp3
    ...
    ...
    Daily Hafez Chaim 067.mp3 -> hlr 67.mp3

    
then, make a seperate function, or an option, to move them onto a recorder,

obviously detecting the recorder.


Stages: find the latest downloaded files
"""