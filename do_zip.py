import zipfile
import os

mypath = 'C:\\ipek\\'
zip_path = 'C:\\ipek\\'
os.chdir(zip_path)
zf = zipfile.ZipFile('log_file.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
zf.write('log.txt')
zf.close()
os.remove("log.txt")
#zip the file in a directory