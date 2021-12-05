import os
import zipfile

mypath = 'C:\\ipek\\'
file ='log_zip'
zip_path = 'C:\\ipek\\'
os.chdir(zip_path)
zipf = zipfile.ZipFile(file + '.zip', 'w', zipfile.ZIP_DEFLATED)
print(zipf)
zipf.close()
os.remove("log.txt")
#zip the file and than delete the file
