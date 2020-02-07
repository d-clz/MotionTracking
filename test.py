import sys
sys.path.append('../')
import time
import sqlite3
from BMX160_LIB import BMX160

conn = sqlite3.connect("bmx160.db")
db = conn.cursor()

bmx = BMX160(1)
#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)

def main():
    while True:
        data= bmx.get_all_data()
        print("magn: x: {0:.2f} uT, y: {1:.2f} uT, z: {2:.2f} uT".format(data[0],data[1],data[2]))
        print("gyro  x: {0}, y: {1}, z: {2}".format(data[3],data[4],data[5]))
        print("accel x: {0}, y: {1}, z: {2}".format(data[6],data[7],data[8]))
        print(f"time stamp: {data[9]}")
        print(" ")


if __name__ == "__main__":
    main()
'''
for _ in range(0,1000):
    data= bmx.get_all_data()
    db.execute("INSERT INTO data(ax,ay,az,gx,gy,gz,mx,my,mz,t_stamp) VALUES (?,?,?,?,?,?,?,?,?,?)",(data[6],data[7],data[8],data[3],data[4],data[5],data[0],data[1],data[2],data[9]))
    conn.commit()
'''
