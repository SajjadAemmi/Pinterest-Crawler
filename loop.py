import os
import time
import subprocess


while True:
    command = "python main.py"
    process = subprocess.Popen(command, shell=True)
    process.wait()
    print(process.returncode)
    print("All Data in dir:", len(os.listdir("photos2")))
    print("Sleeping for 1 min ...")
    time.sleep(60)
