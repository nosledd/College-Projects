import os
from tkinter import filedialog
import tkinter as tk

import sorter
import pandas_view


def file_access():
    root = tk.Tk()
    root.withdraw() #i am hidding the ghost window

    # folders = filedialog.askdirectory(title="Create a Folder")

    file_path=filedialog.askopenfilename()

    file_name=os.path.basename(file_path)
    print(file_name)

    extension=os.path.splitext(file_name)[0]
    print("split",extension)

    sorter.sortet(file_path,extension)
    pandas_view.panda(file_path)


file_access()