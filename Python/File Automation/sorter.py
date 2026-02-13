def sortet(file_name):
    
    file_name=file_name.lower()
    print(file_name)

    subjects={
        "flutter.pdf":["flutter.pdf", "addition"],
        "Yt":["Who needs roads lol"]
    }

    for i in subjects:
        if (file_name == i):
           print("Yes")
           break
        else:
           continue
           
          

    