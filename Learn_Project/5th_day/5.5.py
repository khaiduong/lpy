"""
For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

https://projecteuler.net/problem=22
"""

import string
with open('./names.txt') as f:
	for line in f:
		lst = line.replace('"', '').split(',')
list_of_total = []
for name in lst:
	total =  sum([string.ascii_letters.index(i) for i in name ]) + lst.index(name)
	list_of_total.append(total)

print('The final resulf is: %d' %(sum(list_of_total)))