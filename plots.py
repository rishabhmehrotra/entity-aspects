import matplotlib.pyplot as plt
from numpy.random import normal, uniform
import numpy as np
import random
import math

nq=[]
na=[]
with open("e-nq-na.txt") as infile:
	for line in infile:
		t1 = int(line.split("\t")[1])
		t2 = int(line.split("\t")[2])
		nq.append(t1)
		na.append(t2)
print len(nq)
print len(na)

#plt.hist(nq,20)
plt.hist(nq,bins=[10, 15,20,25, 30,35, 40,45, 50,55,60,65,70,75,80,85,90, 95,100], histtype='stepfilled', label='Distinct Queries')
plt.hist(na,bins=[10, 15,20,25, 30,35, 40,45, 50,55,60,65,70,75,80,85,90, 95,100], histtype='stepfilled', color='r', label='Distinct Contexts')
#plt.hist(na, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Uniform')
plt.title("Distribution of Entities based on nQueries & nContexts")
plt.xlabel("No of Distinct Queries/Contexts")
plt.ylabel("No of Entities")
plt.legend()
plt.show()