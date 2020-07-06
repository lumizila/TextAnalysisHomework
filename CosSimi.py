import sys
import string
import re
import numpy 
import math

def cosineSimilarity(bowA, bowB):
	atimesb = []
	squaredA = []
	squaredB = []
	for el in range(0,len(bowA)): 
		atimesb.append(bowA[el] * bowB[el])
		squaredA.append(bowA[el]*bowA[el])
		squaredB.append(bowB[el]*bowB[el])

	sqrtA = math.sqrt(sum(squaredA)) 
	sqrtB = math.sqrt(sum(squaredB)) 
	sqrtAB = sqrtA * sqrtB	

	result = float(sum(atimesb))/sqrtAB	
	return result

#Preprocessing
animals = ['cat', 'ant', 'dog', 'dolphin', 'eagle', 'fox', 'horse', 'jaguar', 'lion', 'shark']
animalFiles = {}
animalTexts = {}
animalSets = {}
animalBoW = {}
cosSimResult = {}

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


#I generate the vocabulary for the BoW
vocab = []
for animal in animals:
	vocab = vocab + (animalSets[animal])

vocab= list(dict.fromkeys(vocab))

#generating the vectors for each text
for animal in animals:               
	animalBoW[animal] = numpy.zeros(len(vocab))        
	for w in animalSets[animal]:            
		for i,word in enumerate(vocab):                
			if word == w:                     
				animalBoW[animal][i] += 1                            

#calling cosine similarity for each pair of documents and cat document
cosSim = {}
for animal in animals:
	print("Calculating cosine similarity for cat and "+animal+"...")
	cosSim[animal] = cosineSimilarity(animalBoW["cat"], animalBoW[animal])
	print("The result was: "+str(cosSim[animal])+"")

print("Sorting the cosine similarity in descending order, we have the result:")
cosSim = sorted(cosSim.items(), key = lambda k:k[1], reverse=True)

i = 0
for animal in animals:
	print (cosSim[i])
	i = i + 1

for animal in animals:
	animalFiles[animal].close()


