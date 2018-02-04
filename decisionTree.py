from __future__ import division
import math
import csv
import sys


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

def infoGainCalculator(labelList, attributeList, attributes, attribute):
	#print labelList
	#print attributeList
	H_Y = entropyCalculator(labelList)
	attributeEntropy = 0


	return (H_Y - attributeEntropy)

def attributeSelector(labelList, attributeList, attributes):

	bestAttribute = attributes[0]
	maxInfoGain = 0

	for attribute in attributes:
		newInfoGain = infoGainCalculator(labelList, attributeList, attributes, attribute)
		if newInfoGain > maxInfoGain:
			maxInfoGain = newInfoGain
			bestAttribute = attribute

	return bestAttribute 

def decisionTreeAlgo():
	#print "In Main Method"
	dataFrame = []
	attributeList = []
	labelList = [] 
	with open(sys.argv[1], 'rb') as csvfile:
		fileData = csv.reader(csvfile, delimiter=',')
		for row in fileData:
			dataFrame.append(row)

	dataFrame = dataFrame[1:]

	attributes = []

	tup = dataFrame[0]
	for i in range(len(tup) -1):
		attributes.append(i)

	for tup in dataFrame:
		labelList.append(tup[len(tup) -1])
		attributeList.append(tup[:len(tup) -1])

	root = {}
	root = buildDecisionTree(attributeList, attributes, labelList)



if __name__ == '__main__':
	decisionTreeAlgo()