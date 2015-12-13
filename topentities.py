#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost","root","password","aol")

cursor = db.cursor()
oFile = open('entity_min5.txt', 'w')


sql = "SELECT entity, count(*) AS n FROM qe group by entity having n>5 ORDER BY n DESC"
cursor.execute(sql)
res = cursor.fetchall()
preve = "";c=0;start=1;qlist = "";t=0;
for row in res:
	e = row[0]
	n = row[1]
	oFile.write(e+"\t"+str(n)+"\n")
oFile.close()

db.close()