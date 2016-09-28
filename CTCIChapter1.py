import string
#1.1 is Unique see if a string has all unique characters
def isUniqueLessOptimal(string):
	characterList=sorted(list(string))
	leftIndex=0
	for i in range(1, len(characterList)):
		while leftIndex<(len(characterList)-1):
			if characterList[i]==characterList[leftIndex]:
				return False
			leftIndex+=1
	return True

def isUniqueMoreOptimal(string):
	if len(string)>256:
		return False
	listOfBooles=[False for i in range(256)]
	for i in range(len(string)):
		val=ord(string[i])
		if listOfBooles[val]:
			return False
		listOfBooles[val]=True
	return True

#1.2 Check Permutations check if one string is a permutation of another
def CheckPermutation(str1, str2):
	string1=sorted(list(str1))
	string2=sorted(list(str2))
	if string1==string2:
		return True
	return False

def CheckPermutationCharacterCount(str1, str2):
	string1=0
	string2=0
	if len(str1)==len(str2):
		for i in range(len(str1)):
			string1+=ord(str1[i])
			string2+=ord(str2[i])
	if string1==string2:
		return True
	return False

#1.3 URLify replace spaces with %20
def URLify(string, length):
	nonSpaces=string.split()
	URL=""
	for i in nonSpaces:
		if i==nonSpaces[len(nonSpaces)-1]:
			URL=URL+i
		else: 
			URL=URL+i+"%20"
	return URL
	
#1.4 isPermutationPalindrome? checks if a string is a permutation of a palindrome
def isPermutationPalindrome(string):
	return NotOverMaxOdd(buildDict(string))
		
		
def NotOverMaxOdd(dict):
	foundOdd=False
	for a in dict:
		if dict[a]%2==1:
			if foundOdd==True:
				return False
			else:
				foundOdd=True
	return True
		 

def buildDict(str):
	 table=dict.fromkeys(string.ascii_lowercase, 0)
	 for i in list(str):
	 	table[i]+=1
	 return table
	
	

	
	
	
	
	
	
	
	



		