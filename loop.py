import os
import time
import subprocess


while True:
    command = "python3 main.py"
    process = subprocess.Popen(command, shell=True)
    process.wait()
    print(process.returncode)
    print("All Data in dir:", len(os.listdir("photos")))
    print("Sleeping for 1 min ...")
    time.sleep(60)
