#Import Section
from __future__ import division
import math
import csv
import sys

#Method to get Majority Vote among the labels in dataset
def getMajorityVote(dataFrame, attributes, labelColumn):

	labelCount = {}

	for tup in dataFrame:
		if tup[labelColumn] in labelCount:
			labelCount[tup[labelColumn]] = labelCount[tup[labelColumn]] + 1
		else:
			labelCount[tup[labelColumn]] = 1

	maxCount = 0
	maxKey = ""

	for key in labelCount:
		if labelCount[key] > maxCount:
			maxCount = labelCount[key]
			maxKey = key

	return maxKey


#Method to calculate entropy
def entropyCalculator(dataFrame, column):

	columnKeyCount = {}
	entropy = 0

	columnList = []

	for tup in dataFrame:
		columnList.append(tup[column])

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
	
	H_Y = entropyCalculator(dataFrame, labelColumn)

	attributeEntropy = 0
	attributeCount = {}

	for tup in dataFrame:
		if tup[attribute] in attributeCount:
			attributeCount[tup[attribute]] = attributeCount[tup[attribute]] + 1
		else:
			attributeCount[tup[attribute]] = 1

	sumOfCount = sum(attributeCount.values())

	for key in attributeCount:
		keyProb = attributeCount[key]/sumOfCount
		dataFrameSubset = []
		for tup in dataFrame:
			if tup[attribute] == key:
				dataFrameSubset.append(tup)
		attributeEntropy = attributeEntropy + keyProb *entropyCalculator(dataFrameSubset, labelColumn)
	
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

#Method to return a list of values held by the best Attribute
def getValues (dataFrame, attributeList, bestAttribute):

	values = []
	for tup in dataFrame:
		if tup[bestAttribute] not in values:
			values.append(tup[bestAttribute])

	return values

#Method to recursively build Decision Tree
def buildDecisionTree(dataFrame, attributeList, labelColumn):
	
	majorityLabel = getMajorityVote(dataFrame, attributeList, labelColumn)

	if majorityLabel == len(dataFrame):
		return majorityLabel
	else:
		bestAttribute = attributeSelector(dataFrame, attributeList, labelColumn)
		node = {bestAttribute:{}}
		bestAttributeValues=[]
		bestAttributeValues = getValues(dataFrame, attributeList, bestAttribute)

		for attributeValue in bestAttributeValues:

			dataFrameSubset=[]

			for tup in dataFrame:
				newRow = []
				if tup[bestAttribute] == attributeValue:
					for i in range(len(tup)):
						if i != bestAttribute:
							newRow.append(tup[i])
				if len(newRow) != 0:
					dataFrameSubset.append(newRow)

			newAttributeList = list(attributeList)
			newAttributeList.remove(bestAttribute)
			tup
			childNode = buildDecisionTree(dataFrameSubset, newAttributeList, )

	return 0


#Method to initialize the creation of decision Tree
def decisionTreeAlgo():
	#print "In Main Method"
	dataFrame = []
	attributeList = []
	labelList = [] 
	with open(sys.argv[1], 'rb') as csvfile:
		fileData = csv.reader(csvfile, delimiter=',')
		for row in fileData:
			dataFrame.append(tuple(row))

	attributeList = []

	dataFrame = dataFrame[1:]
	tup = dataFrame[0]
	for i in range(len(tup)):
	 	attributeList.append(i)

	labelColumn = len(tup) - 1

	#Building root node
	root = {}
	root = buildDecisionTree(dataFrame, attributeList, labelColumn)
	
	

if __name__ == '__main__':
	decisionTreeAlgo()