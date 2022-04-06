import pyodbc
import time
import schedule
from datetime import datetime 
import os
import subprocess
import psutil

#Query follows naming schema for servers we are concerned with 
sqlQ = cursor.execute("select c.name from computer as c JOIN inactive_computers as s on c.computer_id = s.computer_id where c.name like '%e01' or c.name like '%m01' or c.name like '%h01' or c.name like '%x01' or c.name like '%w02' or c.name like '%pd2' or c.name like '%k01'")
connStr = open("altiris.txt", "r")

def main():
    #Process kill function    
    for proc in psutil.process_iter():

        if any(procstr in proc.name() for procstr in\
            ['vmping']):
            proc.kill()


if __name__ == "__main__":
    main()

theList = ''
addList = ''

def read(conn):
	sqlQ
	theList = ' '
	
	for row in cursor.fetchall():
		addList = theList + ' ' + row.name + ' '
		theList = addList
	# print(theList)
	command = r"Software\vmPing\vmping.exe"
	subprocess.Popen(command + theList)
		
def task():
	clear()
	main()
	read(conn)

conn = pyodbc.connect(connStr)

cursor = conn.cursor()


clear = lambda: os.system('cls') #on Windows System

task()
schedule.every(5).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)