#!/usr/bin/python


eqlist = {"":[]}
eqlists = {"":""}
en = {"":0}
with open("entity_min5.txt") as infile:
	for line in infile:
		e = line.split('\t')[0]
		n = line.split('\t')[1]
		eqlist[e]=[]
		eqlists[e]=""
		en[e] = n


print len(eqlist)
t=0
with open("queryentity.txt") as infile:
	for line in infile:
		t+=1
		q = line.split('\t')[0]
		e = line.split('\t')[1]
		if eqlist.has_key(e):
			qlist = eqlist[e]
			qlist.append(q)
			#eqlist[e] = qlist
			qlists = eqlists[e]
			qlists += "\t"+q
			eqlists[e] = qlists
		if t%100000 ==0:
			print t

oFile = open('e-n-qList.txt', 'w')
print "done with appending"
t=0
for (k,v) in eqlists.items():
	#print "%s \t %s" %(k,v)
	t+=1
	if t%10000 == 0:
		print t
	oFile.write(k+'\t'+str(en[k]).replace("\n","")+"\t"+v+"\n")
oFile.close()




