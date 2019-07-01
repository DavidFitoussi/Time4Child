import  datetime
import time
import os
from datetime import date
from Resource import clsResource


def CheckTime() :
    sumTime = InstanceResource.GetLastTime()
    if sumTime > InstanceResource.TimeAllowedInMinute:
        print("Time over!!!")
        global TimeAllowed
        TimeAllowed = False
    else :
        sumTime += int(InstanceResource.WakeUpTimeInMinute);
        InstanceResource.UpdateTime(sumTime)


InstanceResource = clsResource()

if os.path.exists(InstanceResource.WorkingDirectory) == False:
    os.mkdir(InstanceResource.WorkingDirectory)
currentDayPath = "{}{}".format(InstanceResource.WorkingDirectory,date.today())
if os.path.exists(currentDayPath) == False:
    os.mkdir(currentDayPath)
if os.path.exists("{}{}\{}.txt".format(InstanceResource.WorkingDirectory,currentDayPath,InstanceResource.username)) == False:
    InstanceResource.UpdateTime(0)

TimeAllowed = True
while TimeAllowed is True:
     CheckTime()
     if TimeAllowed is True:
       time.sleep(InstanceResource.WakeUpTimeInMinute*60)

print("Shutdown machine !!!!")
os.system("shutdown -l")


