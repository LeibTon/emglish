'''Printing Info '''
print("Hemlo friemds!!!!")
print("Wemlcome imto ...")
print('\033[91m')
print("*******  ***       ***       ********     ***        ***  **********  ***      ***")
print("*******  ****     ****      ********      ***        ***  **********  ***      ***")
print("***      ******  *****     ***            ***        ***  ***    ***  ***      ***")
print("***      *** ***** ***    ***             ***        ***  *****  ***  ***      ***")
print("*****    ***  ***  ***   ***     *******  ***        ***     ***      ************")
print("*****    ***   *   ***   ***     *******  ***        ***       ***    ************")
print("***      ***       ***   ***      *** **  ***        ***  ***   ****  ***      ***")
print("***      ***       ***    ***     *** **  *********  ***  ***    ***  ***      ***")
print("*******  ***       ***     *********  **  *********  ***  **********  ***      ***")
print("*******  ***       ***      ******    **  *********  ***  **********  ***      ***")
print('\033[m')
vowel = "aeiou"

preference = ['u','o','e','i','a']

def final(word):
	word = word.replace("mmm","m")
	word = word.replace("mm","m")
	return word

def convert(word):
	if len(word)<=3 and word[len(word)-1] not in vowel:
		return final(word)
		
	word = word.replace("oo","u")
	if 'n' in word[1:-1]:
		word = word.replace("n","m",1)
		return final(word)
	for i in range(len(word)-1):
		if word[i]==word[i+1]:
			word = word[:i]+"m"+word[i+1:]
			return final(word)
	for pre in preference:
		for i in range(1,len(word)-1):
			if word[i] == pre and word[i+1] not in vowel:		
				word = word[:i+1]+"m"+word[i+1:]
				return final(word)
	for i in range(1,len(word)-1):
		if word[i] not in vowel and word[i+1] in vowel:
			word = word[:i]+"m"+word[i:]
			return final(word)
	return final(word)

symbols = "!,.?-"

def getList(sentence):
	for i in symbols:
		sentence = sentence.replace(i," "+i+" ")
	sentence = sentence.split()
	return sentence

def mergeList(l):
	sentence = ""
	for i in range(len(l)-1):
		sentence+=l[i]
		if l[i+1] not in symbols:
			sentence+=" "
	sentence+=l[len(l)-1]
	return sentence

def getNewVocab(sentence):
	l = getList(sentence)
	modified =[]

	for i in l:
		modified.append(convert(i))
	return mergeList(modified)

print(getNewVocab(input('\033[94m'+"Tympe somethimg: "+'\033[m')))
