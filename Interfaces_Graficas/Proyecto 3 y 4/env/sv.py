import sqlite3
import csv

file=open("rutas.csv","r")
reader=csv.reader(file)

conex = sqlite3.connect('gps.db')
c=conex.cursor()

c.execute( """CREATE TABLE IF NOT EXISTS data (
 npk integer PRIMARY KEY AUTOINCREMENT,
 id VARCHAR(20),
 lat double, 
 lon double, 
 velo int, 
 angu int, 
 fecha varchar(10), 
 hora varchar(10), 
 onoff int, 
 nsat int)""")


listas=[]
for row in reader:
    listas.append(row)

for row in listas:
    c.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?)",
    (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    conex.commit()
c.execute("SELECT * FROM data")
data = c.fetchall()
print(data)
conex.commit()
c.close()
conex.close()