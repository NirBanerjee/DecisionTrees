from __future__ import division
import math

a = 1
b = 2
c = 3

#print (a/c)

entropy = -1*(((a/c) * math.log((a/c),2.0)) + ((b/c) * math.log((b/c),2.0)))

print entropy