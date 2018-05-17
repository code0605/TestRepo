import fileinfo
import zipfile
class FileInfoPro(fileinfo.FileInfo):
    def search(self,searchstring):
        for lno,line in enumerate(self.lines):
            if searchstring in line:
                print(lno + 1, line.rstrip())
    def compress(self):
        z=zipfile.ZipFile(self.filename + ".zip","w",zipfile.ZIP_DEFLATED)
        z.write(self.filename)
        print("Compression Done")
        z.close()

f=FileInfoPro("input.txt")
f.getsize()
f.getage()
f.getfirstline()
f.getlastline()
f.getnthline(3)
f.getlinecount()
f.search("line")
f.compress()
f.close()
