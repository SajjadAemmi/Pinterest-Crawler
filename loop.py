import time
import subprocess


while True:
    command = "python3 main.py"
    process = subprocess.Popen(command, shell=True)
    process.wait()
    print("Sleeping for 30 seconds ...")
    time.sleep(30)
