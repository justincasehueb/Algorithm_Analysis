
import numpy

lowRange = 1
highRange = 100
mylist = list()

for i in range(lowRange, highRange):
	insert = 8*i*i
	merge = 64*i*numpy.log(i)
	if insert<merge:
		mylist.append(i)
		#print("i:",insert,"<","m:",merge)
	#elif insert>merge:
		
		#print("i:",insert,">","m:",merge)
	#lse:
		
		#print("i:",insert,"==","m:",merge)
for i in mylist:
	print(i)