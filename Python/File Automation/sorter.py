def sortet(file_name,folders):
    
    file_name=file_name.lower()
    print(file_name)

    subjects={
        "flutter.pdf":["flutter.pdf", "addition"],
        "Yt":["Who needs roads lol"]
    }

    for i in folders:
        print(i)
        if (file_name == i):
           print("Yes")
           break
        else:
           continue
           
          

    