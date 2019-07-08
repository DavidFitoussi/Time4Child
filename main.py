from TimeChecker import clsTimeChecker

def TimeCheckerThread():
    InstanceTimeChecker = clsTimeChecker()
    InstanceTimeChecker.InitResource()
    InstanceTimeChecker.Run()


TimeCheckerThread()


