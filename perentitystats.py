#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost","root","password","aol")

cursor = db.cursor()



#sql = "SELECT entity, count(*) AS n FROM qe group by entity having n>5 ORDER BY n DESC"
sql = "SELECT entity, query FROM qe group by entity"
cursor.execute(sql)
res = cursor.fetchall()
preve = "";c=0;start=1;qlist = "";t=0;
for row in res:
	e = row[0]
	q = row[1]
	if start == 1:
		start = 0
		preve = e
	if preve == e:
		qlist = q + "\t" + qlist
		c+=1
	else:
		if c > 5:
			print "%s \t %s" %(e,qlist)
			qlist = ""
			c=0
	preve = e
	if t%100000 == 0:
		print t


db.close()