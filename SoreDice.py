import sys
import string
import re

#Preprocessing
animals = ['cat', 'ant', 'dog', 'dolphin', 'eagle', 'fox', 'horse', 'jaguar', 'lion', 'shark']
animalFiles = {}
animalTexts = {}
animalSets = {}
sorenResult = {}
for animal in animals:
	animalFiles[animal] = open('rawData/'+animal+'.txt', 'r')
	animalTexts[animal] = animalFiles[animal].read()
	#removing punctuations
	for char in string.punctuation:
		animalTexts[animal] = animalTexts[animal].replace(char, ' ');
	#removing digits
	animalTexts[animal] = re.sub(r'\d+', '', animalTexts[animal])
	#removing newlines
	animalTexts[animal] = re.sub(r'\n+', ' ', animalTexts[animal])
	#putting all words as lowercase
	animalTexts[animal] = animalTexts[animal].lower()
	#creating sets
	animalSets[animal] = animalTexts[animal].split(" ")
	#removing empty elements from sets
	animalSets[animal] = list(filter(lambda a: a != '', animalSets[animal]))
	#removing duplicate words
	animalSets[animal] = list(dict.fromkeys(animalSets[animal]))

def SorenDiceSimilarity(a, b):
	setA = set(a)
	setB = set(b)
	setsIntersection =  len(set.intersection(setA, setB))
	sumSets = len(setA) + len(setB)
	try:
		result = float((2 * setsIntersection)) / sumSets
		return result
	except ZeroDivisionError:
		return 1.0

#Evaluating documents by Sorensen-Dice coefficient
for animal in animals:
	print("Comparing the wikipedia introduction text for CAT with the text of "+animal.upper()+"...")
	sorenResult[animal] = SorenDiceSimilarity(animalSets["cat"], animalSets[animal])
	print("The Sorensen-Dice coefficient that resulted was:  "+str(sorenResult[animal]))

print("Sorting the coefficient in descending order, we have the result:")
print(sorted(sorenResult.items(), key = lambda k:k[1], reverse=True)) 


for animal in animals:
	animalFiles[animal].close()