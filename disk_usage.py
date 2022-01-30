import shutil

def size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024.0
    except:
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)


usage = shutil.disk_usage("C:\\")
print("free:")
free_space = size(usage[2])
free_space =float(free_space[:-1])
print(free_space)
print("used:")
used = size(usage[1])
print(used)
print("total:")
total = size(usage[0])
print(total)

def give_info():

 if free_space < 20:
        print("Clean your disk, no more free space!")

 else :
     print("No problem with your disk!")

give_info()