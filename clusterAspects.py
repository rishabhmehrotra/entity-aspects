import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

print sklearn.__version__
#nltk.download('punkt')

model = gensim.models.word2vec.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

c=0;
oFile = open('e-aspect-cluster.txt', 'w')
with open("e-nq-na-a.txt") as infile:
	for line in infile:
		c+=1
		if c==1:
			continue
		if c%10000==0:
			print c
		e = line.split("\t")[0]
		#a = set(literal_eval(line.split("\t")[3]))
		a = eval(line.split("\t")[3])
		print "%s \t\t %d" %(e,len(a))
		X = []
		XS = []
		for aspect in a:
			#print "____%s"%aspect
			if len(str(aspect))<2:
				continue
			vec = [0]*300
			text = aspect.translate(None, string.punctuation)
			tokens = word_tokenize(text)
			#print "No of tokens: %d"%len(tokens)
			tt = 1
			error=0
			for t in tokens:
				try:
					#print "finding representation for %s"%t
					vect = model[t]
					vec = np.add(vec, vect)
					tt+=1
				except:
					#print "or"
					error+=1
			if tt>1:
				tt-=1
			vec = [v/tt for v in vec]
			#print "going to add something";
			X.append(vec)
			XS.append(aspect)
			#print "added something, size right now: %d"%len(X)
		if len(X)<=20:
			nC = 5
		if len(X)>20 and len(X)<=50:
			nC = 10
		if len(X)>50 and len(X)<=100:
			nC = 20
		if len(X)>100 and len(X)<=200:
			nC = 40
		if len(X)>200:
			nC = 50
		print "vectors found for %d elements "%len(X)
		print "errors found: %d"%error
		if len(X)<5:
			nC = len(X)
		kmeans_clustering = KMeans(n_clusters = nC)
		idx = kmeans_clustering.fit_predict(X)
		#print idx
		count = len(idx)
		aspectcluster = ""
		for i in range(0,count-1):
			#print "%s\t%d" %(XS[i],idx[i])
			aspectcluster = aspectcluster + XS[i]+"____"+str(idx[i])+"\t"
		aspectcluster = aspectcluster.replace("\n","")
		oFile.write(e+"\t"+aspectcluster+"\n");


