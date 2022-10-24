import os # pip install os-sys
import shutil #pip install pytest-shutil
import os as file
import os as path

path1 = r'C:\Users\Isac\Documents\Development\test-zone'
path2 = r'C:\Users\Isac\Documents\Development\test-zone\teste'

for root, dirs, files in os.walk(path1):
    for file in files:
        old_path = os.path.join(root, file)
        new_path = os.path.join(path2, file)
        if '.pdf' in file:
            shutil.move(old_path, new_path)
            print('ARQUIVO MOVIDO!')

shutil.move(old_path, new_path)