import sys
sys.path.append('../')
import time
import sqlite3
from BMX160_LIB import BMX160


print("new table created")

bmx = BMX160(1)
#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)

def main():
    datafile = open("sensor_data.txt","w")
    i=0
    while True:
        i+=1
        data= bmx.get_all_data()
        data = [str(data),'\n']
        datafile.writelines(data)
        print("gyros X:{0:.2f} Y:{1:.2f} Z:{2:.2f} (g)".format(data[3],data[4],data[5]))
        print("accel X:{0:.2f} Y:{1:.2f} Z:{2:.2f} (m/s^2)".format(data[6],data[7],data[8])) 
if __name__ == "__main__":
    main()
