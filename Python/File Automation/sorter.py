import shutil

def sortet(file_path,extension):
    
    extension=extension.lower()
    print("name",extension)

    subjects={
        "flutter":["flutter.pdf", "addition"],
        "Yt":["Who needs roads lol"]
    }

    for i in subjects:
        print("Loop",i)
        if (extension == i):
             destination= "E:/Git/College-Projects/Python/File Automation/uploads/sorted_notes/Python/"
             print(file_path)
             shutil.copy(file_path,destination)
             break
        else:
           print("Error")         
        