import classes as c

dgetter = c.DirectoryGetter()
dgetter.getDirAndPattern()
renamer = c.Renamer(dgetter.getDir(), dgetter.getPattern())
renamer.rename()
