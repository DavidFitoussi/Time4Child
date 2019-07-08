import  datetime
import time
import os
from datetime import date
from Resource import clsResource

class clsTimeChecker:
    def __init__(self):
        self.InstanceResource = clsResource()

    def CheckTime(self):
        sumTime = self.InstanceResource.GetLastTime()
        if sumTime > self.InstanceResource.TimeAllowedInMinute:
            print("Time over!!!")
            global TimeAllowed
            TimeAllowed = False
        else :
            sumTime += int(self.InstanceResource.WakeUpTimeInMinute);
            self.InstanceResource.UpdateTime(sumTime)

    def InitResource(self):
        if os.path.exists(self.InstanceResource.WorkingDirectory) == False:
            os.mkdir(self.InstanceResource.WorkingDirectory)
        currentDayPath = "{}{}".format(self.InstanceResource.WorkingDirectory,date.today())
        if os.path.exists(currentDayPath) == False:
            os.mkdir(currentDayPath)
        if os.path.exists("{}\{}.txt".format(currentDayPath,self.InstanceResource.username)) == False:
            self.InstanceResource.UpdateTime(0)

    def Run(self):
        TimeAllowed = True
        while TimeAllowed is True:
             self.CheckTime()
             if TimeAllowed is True:
               time.sleep(self.InstanceResource.WakeUpTimeInMinute*60)
        print("Shutdown machine !!!!")
        #os.system("shutdown -l")


