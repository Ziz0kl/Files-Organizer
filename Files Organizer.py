import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

print('Welcome in organize.py script - happy clean folder')

for filename in os.listdir(current_dir):

    if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.copy(filename, "Images")
        os.remove(filename)
        print('Images Done')

    elif filename.endswith((".py", ".css", ".html", ".bash", ".js")):
        if not os.path.exists("Codes"):
            os.mkdir("Codes")
        shutil.copy(filename, "Codes")
        os.remove(filename)
        print('Code Done')

    elif filename.endswith((".pdf", ".word")):
        if not os.path.exists("Docs"):
            os.mkdir("Docs")
        shutil.copy(filename, "Docs")
        os.remove(filename)
        print('Docs Done')

    elif filename.endswith((".mp4", ".webm")):
        if not os.path.exists("Videos"):
            os.mkdir("Videos")
        shutil.copy(filename, "Videos")
        os.remove(filename)
        print('Videos Done')

    elif filename.endswith((".zip", ".rar")):
        if not os.path.exists("Archives"):
            os.mkdir("Archives")
        shutil.copy(filename, "Archives")
        os.remove(filename)
        print('Archives Done')

    

print('Done Organizing This Folder')

