import shutil

def sortet(file_path,file_name):
    
    file_name=file_name.lower()
    print("name",file_name)

    subjects={
        "flutter":["flutter", "addition"],
        "Yt":["Who needs roads lol"]
    }

    for subject in subjects:
        print(subject)
        if subject in file_name:
            print("Found Thrpugh file name")
        else:
             for keyword in subjects[subject]:
                 if keyword in file_name:
                     print("Found through keyword")
        
        
    '''if (file_name == i):
             destination= "E:/Git/College-Projects/Python/File Automation/uploads/sorted_notes/Python/"
             print(file_path)
             shutil.copy(file_path,destination)
             break
        else:
           print("Error")  '''       
        