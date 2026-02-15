def sortet(file_name):
    
    file_name=file_name.lower()
    print(file_name)

    subjects={
        "flutter":["flutter.pdf", "addition"],
        "Yt":["Who needs roads lol"]
    }

    for i in subjects:
        print(i)
        if (file_name == i):
             destination= "E:/Git/College-Projects/Python/File Automation/uploads/" + file_name
             shutil.copy(file_path,destination)
             sorter.sortet(file_name,)
             break
        else:
           continue 





           for i in subjects:
        print(i)
        if (file_name == i):
             destination= "E:/Git/College-Projects/Python/File Automation/uploads/" + file_name
             shutil.copy(file_path,destination)
             sorter.sortet(file_name,)
             break
        else:
           continue 