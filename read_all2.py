import sys
sys.path.append('../')
import time
import sqlite3
from BMX160_LIB import BMX160

conn = sqlite3.connect("bmx160.db")
#db = conn.cursor()

try:
    conn.execute("drop table data;")
    #conn.commit()
except:
    print("nothing to delete")

conn.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT,ax REAL NOT NULL,ay REAL NOT NULL,az REAL NOT NULL,gx REAL NOT NULL,gy REAL NOT NULL,gz REAL NOT NULL,mx REAL NOT NULL,my REAL NOT NULL,mz REAL NOT NULL,t_stamp INTEGER NOT NULL);")
#conn.commit()

print("new table created")

bmx = BMX160(1)
#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)

def main():
    i=0
    while (i<3000):
        data= bmx.get_all_data()
        start_time = time.time()
        conn.execute("INSERT INTO data(ax,ay,az,gx,gy,gz,mx,my,mz,t_stamp) VALUES (?,?,?,?,?,?,?,?,?,?)",(data[6],data[7],data[8],data[3],data[4],data[5],data[0],data[1],data[2],data[9]))
        #conn.commit()
        #start_time=time.time()
        #conn.commit()
        i+=1
        elapse_time=time.time()-start_time
        print("Recorded line",i,"in",elapse_time,"seconds")
        
    conn.commit()

if __name__ == "__main__":
    main()
