#Import Section
from __future__ import division
import math
import csv
import sys

#Method to get Majority Vote among the labels in dataset


#Method to calculate entropy
def entropyCalculator(columnList):
	maxKey = 0
	entropy = 0
	no_of_inputs = len(columnList)
	dictList = {}
	for entry in columnList:
		if entry in dictList:
			dictList[entry] = dictList[entry]+1
		else:
			dictList[entry] = 1

	for key in dictList:
		if dictList[key] > maxKey:
			maxKey = dictList[key]

		entropy = entropy + ((dictList[key]/len(columnList)) * math.log((dictList[key]/len(columnList)),2.0))


	return -1*entropy

#Method to calculate information gain for every attribute
def infoGainCalculator(labelList, attributeList, attributes, attribute):
	#print labelList
	#print attributeList
	H_Y = entropyCalculator(labelList)
	attributeEntropy = 0


	return (H_Y - attributeEntropy)

#Method to return the best attribute for split
def attributeSelector(labelList, attributeList, attributes):

	bestAttribute = attributes[0]
	maxInfoGain = 0

	for attribute in attributes:
		newInfoGain = infoGainCalculator(labelList, attributeList, attributes, attribute)
		if newInfoGain > maxInfoGain:
			maxInfoGain = newInfoGain
			bestAttribute = attribute

	return bestAttribute 

#Method to recursively build Decision Tree
def buildDecisionTree(dataFrame, attributes, labelColumn):
	
	majorityLabel = getMajorityVote(dataFrame, attributes, labelColumn)

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

	attributes = []

	dataFrame = dataFrame[1:]
	tup = dataFrame[0]
	for i in range(len(tup)):
	 	attributes.append(i)

	#print attributes
	labelColumn = len(tup) - 1
	root = {}
	root = buildDecisionTree(dataFrame, attributes, labelColumn)
	
	# root = {}
	# root = buildDecisionTree(attributeList, attributes, labelList)



if __name__ == '__main__':
	decisionTreeAlgo()