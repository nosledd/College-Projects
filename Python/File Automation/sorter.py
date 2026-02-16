import shutil
import os
import database


def sortet(file_path,file_name):
    
    file_name=file_name.lower()
    print("name",file_name)

    subjects={
        "flutter":["flutter", "addition"],
        "python":["py"]
    }

    for subject in subjects:
        if subject in file_name:
            destination= "E:/Git/College-Projects/Python/File Automation/uploads/sorted_notes/"+subject+"/"
            if not os.path.exists(destination):
                os.makedirs(destination)
            
            shutil.copy(file_path,destination)
            database.insert_record(file_name, subject, destination)
            break
        else:
            for keyword in subjects[subject]:
                if keyword in file_name:
                    destination= "E:/Git/College-Projects/Python/File Automation/uploads/sorted_notes/"+subject+"/"
                    if not os.path.exists(destination):
                         os.makedirs(destination)
            
                    shutil.copy(file_path,destination)
                    database.insert_record(file_name, subject, destination)
                    break
        
# theres still lot of logic work to be done
     
        