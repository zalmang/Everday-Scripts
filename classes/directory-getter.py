import os
from datetime import date, datetime
import zfunctions as z
import pattern_creator as p

class DirectoryGetter:
    
    _DOWNLOADS_PATH = "~/Downloads"
    
    
    def __init__(self, dir=_DOWNLOADS_PATH, fname="", patt=""):
        self._dir = dir
        self._fname = fname
        self._patt = patt
    
    def setDirAndPattern(self):
        if (self.dirIncludesRealFile() and self.doYouWantThisFile()):
            return self.returnPatternBasedOnFileName()
        option = z.zinput("Are your files in Downloads?")
        if option == 1:
            self._dir = os.path.expanduser(self._dir)
        elif option == 0:
            self._dir = input("Enter path (format: /Users/(zalmangagerman?)/...)\n")
        
        if not self.isRealDir():
            print("Invalid path. Please try again.")
            return self.setDirAndPattern()
        
        if (self.dirIncludesRealFile()):
            self._fname = self._dir.split("/")[-1]
            if (self.doYouWantThisFile()):
                return self.returnPatternBasedOnFileName()
            else:
                print("Let's start over")
                return self.setDirAndPattern()
        
        if (z.zinput("Do you want to give your pattern now?")):
            if (self.userInputsPattern()):
                return
            else:
                print("No good. Try again!")
                return self.setDirAndPattern()
        
        if (z.zinput("Do you want to rename based on date?") == 1):
            if z.zinput("Did you download your files today?"):
                udate = date.today()
            else:
                udate = z.dateInput()
                #convert to something python can understand
                #find a group of files with that date
            
            return returnPatternBasedOnDate(directory, udate)
        else:
            return userGivesFileName(directory)
            
                # os.path.getmtime(path) returns the last modified time
                # Add your logic here for processing the files
                
    def userGivesFileName(self):
        print(f"Looks like you want to do it by file name.")
        self._fname = input(f"What's the name of one file you want to sort by? Remember, you're in {directory}.")
        if os.path.exists(f"{self._dir}/{self._fname}" and not os.path.isdir(f"{self._dir}/{self._fname}")):
            return returnPatternBasedOnFileName(f"{directory}/{fileName}")
        else:
            print("No such file. Lets' try again")
            return userGivesFileName(directory)

    def returnPatternBasedOnDate(directory, dateStr):
        pass

    def returnPatternBasedOnFileName(directoryWithFile):
        pass


    def isValidPattern(self):
        for file in os.listdir(self._dir):
            filename = os.fsdecode(file)
            if self._patt in filename:
                return 1
        return 0

    def dirIncludesRealFile(self):
        return (self.isRealDir() and self.isRealFile())
    def isRealDir(self):
        return os.path.exists(self._dir)
    def isRealFile(self):
        return not os.path.isdir(self._dir)
    def doYouWantThisFile(self):
        if (z.zinput(f"Is one of the files you want to rename {self._fname}?")):
            return 1
        else:
            return 0
        
    def userInputsPattern(self):
        self._patt = input("Please enter the pattern")
        if (self.isValidPattern()):
            return self.areTheseYourFiles()
        else:
            print("I'm sorry! That's not a valid pattern! Try again.")
            return self.userInputsPattern()   
    
    def areTheseYourFiles(self):
        print("Are these your files?")
        for file in os.listdir(self._dir):
            if self._patt in file:
                print(f"{file}\n")
        return z.zinput("\nAre these your files?")
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