"""
Bài 4.6
-------
s = '12 drummers drumming, 11 pipers 23piping, 10 lords a-leaping'
Print out list of all numbers in this string.
Output::
  [12, 11, 23, 10]
"""
string = '12 drummers drumming, 11 pipers 23piping, 10 lords a-leaping' 
list_num = [i for i in string.split()]
print(list_num)

