import os
import time

cmd = "time curl  http://helloworld-python.default.kingdo.club"

for i in range(60):
    time.sleep(i)
    print("################", i, "###############")
    print(os.popen(cmd).read())
