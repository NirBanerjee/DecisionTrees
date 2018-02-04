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

def infoGainCalculator(labelList, attributeList):
	H_Y = entropyCalculator(labelList)
	print H_Y
	return 0

def decisionTreeLearn():
	#print "In Main Method"
	dataFrame = []
	attributeList = []
	labelList = [] 
	with open(sys.argv[1], 'rb') as csvfile:
		fileData = csv.reader(csvfile, delimiter=',')
		for row in fileData:
			dataFrame.append(row)

	dataFrame = dataFrame[1:];

	for tup in dataFrame:
		labelList.append(tup[len(tup) -1])
		attributeList.append(tup[:len(tup) -1])

	infoGain = infoGainCalculator(labelList, attributeList)
	print infoGain


if __name__ == '__main__':
	decisionTreeLearn()