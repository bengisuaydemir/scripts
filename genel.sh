find /home/ipek/ -type f -name "*.txt"
find /home/ipek/ -type f -size +10M
find /home/ipek/ -type f -name "*.txt" -size -1M
find /home/ipek/ -type f -name ".txt" -mtime +3 -exec rm -rf {} \;
find /home/ipek/ -size +50M -ecec rm -rf {} \;
find /home/ipek/  -iname "*" | xargs grep "12*"
find /* -iname "*" | xargs grep "ipek" -sl
find /home/ipek/* -type f -mtime +60 -exec mv {} /home/ipek/test1 \;
#mtime --> modified time
#ctime--> create time


