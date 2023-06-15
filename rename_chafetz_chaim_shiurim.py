import os


directory = "/Users/zalmangagerman/Downloads" # this is not correct

for i in range(16, 40):
    old_filename = f"DailyHafez Haim Lesson Number 0{i:03}.mp3"
    new_filename = f"hlr {i}.mp3"
    old_path = os.path.join(directory, old_filename)
    new_path = os.path.join(directory, new_filename)

    os.rename(old_path, new_path)

    #to add: copy the files in a holding tank in case there are errors
    #finding user input
    