#Import Section
from __future__ import division
import math
import csv
import sys

#Method to return the count of classified and unclassified keys
def getClassCount(dataFrame, attributeList, labelColumn):
	
	counts = {}
	lastIndex = attributeList.index(labelColumn)
	for tup in dataFrame:
		if tup[lastIndex] in counts:
			counts[tup[lastIndex]]  = counts[tup[lastIndex]] + 1
		else:
			counts[tup[lastIndex]] = 1

	return counts

#Print each line after tree goes to next level
def printTreeLine(counts):

	string = "["
	
	for key in counts:
		string = string + str(counts[key]) + " = " + str(key) + " /"

	string = string[:-1]
	string = string + "]"

	return string

#Method to get Majority Vote among the labels in dataset
def getMajorityVote(dataFrame, attributeList, labelColumn):

	labelCount = {}

	lastIndex = attributeList.index(labelColumn)

	for tup in dataFrame:
		if tup[lastIndex] in labelCount:
			labelCount[tup[lastIndex]] = labelCount[tup[lastIndex]] + 1
		else:
			labelCount[tup[lastIndex]] = 1

	maxCount = 0
	maxKey = ""

	for key in labelCount:
		if labelCount[key] > maxCount:
			maxCount = labelCount[key]
			maxKey = key

	return maxKey


#Method to calculate entropy
def entropyCalculator(dataFrame, attributeList, labelColumn):

	columnKeyCount = {}
	entropy = 0

	labelIndex = attributeList.index(labelColumn)

	columnList = []

	for tup in dataFrame:
		columnList.append(tup[labelIndex])

	totalInputs = len(columnList)

	for entry in columnList:
		if entry in columnKeyCount:
			columnKeyCount[entry] = columnKeyCount[entry]+1
		else:
			columnKeyCount[entry] = 1

	for key in columnKeyCount:
		entropy = entropy + ((columnKeyCount[key]/totalInputs) * math.log((columnKeyCount[key]/totalInputs),2.0))

	return -1*entropy

#Method to calculate information gain for every attribute
def infoGainCalculator(dataFrame, attributeList, attribute, labelColumn):
	
	H_Y = entropyCalculator(dataFrame, attributeList, labelColumn)

	attributeEntropy = 0
	attributeCount = {}

	for tup in dataFrame:
		if tup[attributeList.index(attribute)] in attributeCount:
			attributeCount[tup[attributeList.index(attribute)]] = attributeCount[tup[attributeList.index(attribute)]] + 1
		else:
			attributeCount[tup[attributeList.index(attribute)]] = 1

	sumOfCount = sum(attributeCount.values())

	for key in attributeCount:
		keyProb = attributeCount[key]/sumOfCount
		dataFrameSubset = []
		for tup in dataFrame:
			if tup[attributeList.index(attribute)] == key:
				dataFrameSubset.append(tup)
		attributeEntropy = attributeEntropy + keyProb *entropyCalculator(dataFrameSubset, attributeList, labelColumn)

	return (H_Y - attributeEntropy)

#Method to return the best attribute for split
def attributeSelector(dataFrame, attributeList, labelColumn):

	bestAttribute = attributeList[0]
	maxInfoGain = 0

	trimAttributeList = attributeList[:-1]
	for attribute in trimAttributeList:
		newInfoGain = infoGainCalculator(dataFrame, attributeList, attribute, labelColumn)
		#print newInfoGain
		if newInfoGain > maxInfoGain:
			maxInfoGain = newInfoGain
			bestAttribute = attribute

	return bestAttribute 

#Method to recursively build Decision Tree
def buildDecisionTree(dataFrame, attributeList, labelColumn, slashCount, levels):
	
	labelColumnValues = []
	for tup in dataFrame:
		labelColumnValues.append(tup[attributeList.index(labelColumn)])

	majorityLabel = getMajorityVote(dataFrame, attributeList, labelColumn)

	#print attributeList
	if labelColumnValues.count(labelColumnValues[0]) == len(labelColumnValues):
		return labelColumnValues[0]
	
	if not dataFrame or len(attributeList) == 1 or levels == 0:
		return majorityLabel
	
	bestAttribute = attributeSelector(dataFrame, attributeList, labelColumn)

	node = {bestAttribute:{}}

	bestAttributeValues=[]
	for tup in dataFrame:
		if tup[attributeList.index(bestAttribute)] not in bestAttributeValues:
			bestAttributeValues.append(tup[attributeList.index(bestAttribute)])
	
	for attributeValue in bestAttributeValues:
		dataFrameSubset=[]

		for tup in dataFrame:
	 		newRow = []
	 		if tup[attributeList.index(bestAttribute)] == attributeValue:
	 			for i in range(len(tup)):
	 				if i != attributeList.index(bestAttribute):
	 					newRow.append(tup[i])
	 			if len(newRow) != 0:
	 				dataFrameSubset.append(newRow)



	 	newAttributeList = list(attributeList)
	 	newAttributeList.remove(bestAttribute)

	 	string = ""
	 	for i in range(slashCount):
	 		string = string + '|'
	 	string = string + " " + bestAttribute + " = " + attributeValue + " : "
	 	counts = {}
	 	counts = getClassCount(dataFrameSubset, newAttributeList, labelColumn)
	 	string = string + printTreeLine(counts)
	 	print string

		childNode = buildDecisionTree(dataFrameSubset, newAttributeList, labelColumn, slashCount+1, levels-1)
		node[bestAttribute][attributeValue] = childNode

	return node

if __name__ == '__main__':
	dataFrame = []
	attributeList = []
	labelList = [] 
	with open(sys.argv[1], 'rb') as csvfile:
		fileData = csv.reader(csvfile, delimiter=',')
		for row in fileData:
			dataFrame.append(tuple(row))

	attributeList = []
	tup = dataFrame[0]
	attributeList = list(tup)
	dataFrame = dataFrame[1:]

	labelColumn = attributeList[-1]

	
	#print count of + and - at the root node
	counts = getClassCount(dataFrame, attributeList, labelColumn)
	slashCount = 0
	print printTreeLine(counts)

	#Get the number of levels to recurse
	levels = int(sys.argv[2])

	#If the number of levels is greater than 0, then build tree recursively 
	#else set root as majority value
	root = {}
	if levels == 0:
		root = getMajorityVote(dataFrame, attributeList, labelColumn)
	else:
		slashCount = slashCount +1
		root = buildDecisionTree(dataFrame, attributeList, labelColumn, slashCount, levels)

	print root