import os
import glob
import zipfile

home = "c:\\users\\tring\\desktop\\synechron3"
pattern = "*.py"
target = "c:\\users\\tring\\desktop\\day2.zip"

os.chdir(home)#go to the path
files = glob.glob(pattern)#select all pattern files
z = zipfile.ZipFile(target,"w",zipfile.ZIP_DEFLATED)#open a zip archive

for file in files:  #add files to the archive
    z.write(file)
z.close()#close the zip file
