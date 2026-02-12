import os
import shutil
from tkinter import filedialog
import sorter

def file_access():
    file_path=filedialog.askopenfilename()
    print(file_path)

    file_name=os.path.basename(file_path)
    print(file_name)

    extension=os.path.splitext(file_path)[1]
    print(extension)

    destination= "E:/Git/College-Projects/Python/File Automation/uploads/" + file_name
    shutil.copy(file_path,destination)
    sorter.sortet(file_name)

file_access()

    


