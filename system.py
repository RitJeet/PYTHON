import subprocess
import os
import psutil
id =  subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new=[]
for item in id:
    new.append(str(item.split('\r')[:-1]))
for i in new:
    print(i[2:-2])
print(f"RAM : {psutil.virtual_memory()}")
