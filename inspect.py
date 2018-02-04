from __future__ import division
import math
import csv
import sys
####All Imports#####

##Read the csv file to memory##
dataFrame = []
with open(sys.argv[1],'rb') as csvfile:
	fileData = csv.reader(csvfile, delimiter=',')
	for row in fileData:
		dataFrame.append(row)

#Count the number of different classes and store in dictionary
dictOutput = {}
dataFrame = dataFrame[1:]
for row in dataFrame:
	if row[len(row)-1] in dictOutput:
		dictOutput[row[len(row)-1]] = dictOutput[row[len(row)-1]] + 1
	else:
		dictOutput[row[len(row)-1]] = 1;

#Calculating Entropy
maxKey = 0
entropy = 0
no_of_inputs = len(dataFrame)
for key in dictOutput:
	if dictOutput[key] > maxKey:
		maxKey = dictOutput[key]

	entropy = entropy + ((dictOutput[key]/no_of_inputs) * math.log((dictOutput[key]/no_of_inputs),2.0))

entropy = entropy * -1;
error = (no_of_inputs-maxKey)/no_of_inputs

#Writing the result to file
writer = open(sys.argv[2],'w')
writer.write("entropy: " + str(entropy) + "\n")
writer.write("error: " + str(error))
writer.close






