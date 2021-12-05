import os
import time

#get today time and delete 20 days older files

path = r'C:\\ipek\\'
now = time.time()

for filename in os.listdir(path):

    if os.path.getmtime(os.path.join(path, filename)) < now - 20 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))