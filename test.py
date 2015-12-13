#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost","root","password","aol")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s " % data

sql = "SELECT userid, query FROM aollogs"
cursor.execute(sql)
#uq = cursor.fetchall
prev = '';c=0;
for (u,q) in cursor:
	if prev==u:
		c+=1
	else:
		print "%s %d" %(prev,c)
		c=0;
		prev = u


db.close()