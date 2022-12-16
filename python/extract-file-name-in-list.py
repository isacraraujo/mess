import os

# folder path
dir_path = r'C:\Users\Isac\Downloads\CARTORIO\LIVRO DE CASAMENTO\\'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)