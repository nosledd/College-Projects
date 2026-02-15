import pandas as pan

def panda(file_path):
    file=pan.read_csv(file_path)
    print(file)