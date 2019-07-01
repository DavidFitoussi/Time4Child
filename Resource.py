import  datetime
import time
import config
import getpass
from datetime import date

class clsResource:
    def __init__(self):
        self.WakeUpTimeInMinute = config.DATABASE_CONFIG['WakeUpTimeInMinute']
        self.WorkingDirectory = config.DATABASE_CONFIG['WorkingDirectory']
        self.TimeAllowedInMinute = config.DATABASE_CONFIG['TimeAllowedInMinute']
        self.username = getpass.getuser()

    def UpdateTime(self, timeToUpdate):
        print("the time was updated to ",timeToUpdate)
        f = open("{}{}\{}.txt".format(self.WorkingDirectory,date.today(),self.username), "w")
        f.write(str(timeToUpdate))
        f.close()

    def GetLastTime(self):
        f = open("{}{}\{}.txt".format(self.WorkingDirectory,date.today(),self.username),"r")
        sumTime = int(f.read())
        f.close()
        return sumTime
