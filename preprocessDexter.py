# -*- coding: utf-8 -*-

import sys,json

def main(argv):
	c = 0;
	errors=0
	oFile = open('queryentity.txt', 'w')
	with open("Logs_dexter.final") as infile:
		for line in infile:
			#print line
			line = line.replace("u'","'")
			line = line.replace("u\"","\"")
			if "wagner photography" in line or "clothing stores in louisiana" in line:
				continue;
			#print c
			#if(1):
			try:
				#line = line.replace("'","\"")
				line = line.replace("{'","{\"")
				line = line.replace("':","\":")
				line = line.replace(" '"," \"")
				line = line.replace("'}","\"}")
				line = line.replace("'","")
				#print line
				query = line.split('\t')[0]
				if "\\" in query:
					continue
				#query = queryentity.replace(" \\","")
				part2 = line.split('\t')[1]
				#print "~~~~~~~~"
				#print part1
				#print part2
				data = json.loads(part2)
				
				for key, value in data.iteritems():
					#print "%s-----------" %(key)
					entityinfo = ""
					d = json.loads(json.dumps(value))
					for entity in d.values():
						entityinfo = entityinfo + " " +str(entity)
						#print " ____ %s" %(entity)
					#print "%s_____%s" %(key, entityinfo)
					if len(query)>0 and len(key)>0 and len(entityinfo)>0:
						oFile.write(query + '\t' + key + '\t' + entityinfo + '\n')
				#print "\n\n\n"
			except:
					print line
					errors += 1
			c=c+1
			if c%100000 == 0:
				print c

	print c
	print errors
	oFile.close()

if __name__ == '__main__':
  main(sys.argv)