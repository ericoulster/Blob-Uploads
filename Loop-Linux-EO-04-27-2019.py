from time import sleep
import subprocess
x = 1
y = 1
while x == 1:
    print("iteration number: " + str(y))
    subprocess.run(['python Pipeline-Deploy-EO-4-24-2019.py'], shell=True)
    sleep(20)
    y += 1
