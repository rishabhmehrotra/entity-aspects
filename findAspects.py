#!/usr/bin/python

import pickle

elist = {"":[]}
ea = {"":""}
enq = {"":0}
ena = {"":0}
enc = {"":0}#total no of contexts
encnull = {"":0}#no of contexts which were null - i.e., only the entity was the query

with open("e-n-qList.txt") as infile:
	for line in infile:
		e = line.split('\t')[0]
		n = line.split('\t')[1]
		tmp = line
		tmp = tmp.replace(e+"\t","")
		tmp = tmp.replace(str(n)+"\t","")
		elist[e] = tmp.split('\t')
		#print(elist[e])
		enq[e] = n
		enc[e] = 0
		encnull[e] = 0

print len(elist)

c=0
for (k,v) in elist.items():
	aspects = set()
	for cntx in v:
		t = cntx.replace(k,"")
		t = t.replace("  "," ")
		t = t.strip()
		aspects.add(t)
		if len(t)<2:
			tt = encnull[k]
			tt+=1
			encnull[k] = tt
		tt2 = enc[k]
		tt2+=1
		enc[k]=tt2
		
	ea[k] = aspects
	ena[k] = len(aspects)
	c+=1
	if c%10000 == 0:
		print c

print "done with generating aspect candidates"
oFile = open('e-nq-na.txt', 'w')
for (k,v) in ea.items():
	oFile.write(k+"\t"+str(enq[k])+"\t"+str(len(v))+"\n")

oFile = open('e-nq-na-a.txt', 'w')
for (k,v) in ea.items():
	oFile.write(k+"\t"+str(enq[k])+"\t"+str(len(v))+"\t"+str(v)+"\n")

oFile = open('e-nc-ncnull.txt', 'w')
for (k,v) in ea.items():
	oFile.write(k+"\t"+str(enc[k])+"\t"+str(encnull[k])+"\n")

#oFile = open('e-nq-na-a_serialized.txt', 'w')
#for (k,v) in ea.items():
#	oFile.write(k+"\t"+str(enq[k])+"\t"+str(len(v))+"\t"+pickle.dumps(v)+"\n")




