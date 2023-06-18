import os
from datetime import date

DOWNLOADS_PATH = "~/Downloads"

def main():
    return stage2(convertInput("Are your files in Downloads? (y/n)"))

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
        ans = input(f"Is one of the files you want to rename {fileName}? (y/n)")
        if ans != "y":
            return enterPath(input("Please enter the path of the folder that the new files exist: "))
    return decidePattern(path, qIsFile)

def decidePattern(directory, qIsFile):
    if not qIsFile:
        if convertInput("Did you download your files today? (y/n)"):
            today = date.today()
            # os.path.getmtime(path) returns the last modified time
            # Add your logic here for processing the files
            pass  # Placeholder, replace with your code

def convertInput(inputstm, str=""):
    if str == "":
        str = input(inputstm)
    if str.lower() == "y":
        return 1
    elif str.lower() == "n":
        return 0
    else:
        return convertInput("Invalid entry. Please try again (y/n): ")


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