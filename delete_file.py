import os
import fnmatch

files =['*.docx', '*.txt']
#delete docx and txt files in a folder

for path, dirnames, filesnames in os.walk('C:\\ipek\\'):
    print(filesnames)
    for extensions in files:
        for filename in fnmatch.filter(filesnames,extensions):
            os.remove(os.path.join(path, filename))
            print(filename)
