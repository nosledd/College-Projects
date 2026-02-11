from tkinter import filedialog
from sorter import sort_file

def upload_and_sort():
    
    # Open file picker
    file_path = filedialog.askopenfilename(
        title="Select Notes/PDF",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    
    if file_path:
        subject = input("Enter Subject Name: ")
        new_path = sort_file(file_path, subject)
        print("Sorted Path:", new_path)

# Run function
upload_and_sort()
