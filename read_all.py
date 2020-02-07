import sys
import os
#sys.path.append('../')
import time
import csv
#import sqlite3
from BMX160_LIB import BMX160

bmx = BMX160(1)
#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)

def record_data(file_name):
    start_time=time.time()
    data = bmx.get_all_data()
    with open(file_name, 'a') as _file:
        writer = csv.writer(_file)
        writer.writerow([data[6],data[7],data[8],data[3],data[4],data[5],data[0],data[1],data[2],data[9]])
    time.sleep(0.005)
    elapse_time=time.time()-start_time
    return elapse_time

def main():
    i=0
    total_time=0
    avg_time=0
    file_path='/home/pi/bmx160/data.csv'
    if os.path.isfile(file_path)==True:
        os.remove(file_path)
    with open('data.csv','w', newline = '') as file:
        fieldnames=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz', 't_stamp']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    while True:
        try:
            elapse_time = record_data(file_path)
            total_time += elapse_time
            i+=1
            print("Recorded line",i,"in",elapse_time,"seconds")
        except:
            if i>0:
                avg_time = total_time / i
            print("\n recorded ", i, "lines")
            print("\n average elapse time: ", avg_time)
            break

if __name__ == "__main__":
    main()
