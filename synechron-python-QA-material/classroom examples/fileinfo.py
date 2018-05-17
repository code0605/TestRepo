import os
import time
class FileInfo:
    def __init__(self,filename):
        self.filename=filename
        self.f=open(self.filename,'r')
        self.lines = self.f.readlines()
    def getsize(self):
        print(os.path.getsize(self.filename))
    def getage(self):
        print(time.time() - os.path.getctime(self.filename))
    def getfirstline(self):
        self.getnthline(1)
    def getlastline(self):
        self.getnthline(0)
    def getnthline(self,lineno):
        print(self.lines[lineno - 1].rstrip())
    def getlinecount(self):
        print(len(self.lines))
    def close(self):
        self.f.close()
    
