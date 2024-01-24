import os
import shutil
import subprocess

mydir = '/home/vlab/mini-AlphaStar/data/Replays/HardOnly'
file_list = os.listdir(mydir)
script_path = '/home/vlab/mini-AlphaStar/run.py'

for i in range(len(file_list)):
    src = mydir + '/' + file_list[i]
    dst = '/home/vlab/mini-AlphaStar/data/Replays/filtered_replays_1'
    shutil.copy(src, dst)
    try:
        subprocess.run(["python", script_path])
    except:
        print('python error')
    try:
        os.remove(dst + '/' + file_list[i])
    except:
        print('remove error')
