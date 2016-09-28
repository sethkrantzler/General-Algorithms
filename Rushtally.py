"""a function I coded to take the votes on a t shirt design for my fraternities rush shirts and calculate how many votes each shirt received, check the Votesforrushtally.txt to see what the formating for the data set looked like (pulled off google sheets)"""
import numpy as np
def RST(file):
	firstchoice=np.genfromtxt(file, skiprows=0, usecols=(1,), dtype="str")
	secondchoice=np.genfromtxt(file, skiprows=0, usecols=(3,), dtype="str")
	firstchoice.tolist()
	secondchoice.tolist()
	one=0
	two=0
	three=0
	four=0
	five=0
	for i in range(len(firstchoice)):
		first=firstchoice[i]
		second=secondchoice[i]
		if first.find("1")!=-1:
			one+=2
		elif second.find("1")!=-1:
			one+=1
		if first.find("2")!=-1:
			two+=2
		elif second.find("2")!=-1:
			two+=1
		if first.find("3")!=-1:
			three+=2
		elif second.find("3")!=-1:
			three+=1
		if first.find("4")!=-1:
			four+=2
		elif second.find("4")!=-1:
			four+=1
		if first.find("5")!=-1:
			five+=2
		elif second.find("5")!=-1:
			five+=1
	print "1:%r 2:%r 3:%r 4:%r 5:%r"%(one, two, three, four, five)
RST("/Users/sethkrantzler/Documents/votes.txt")
		