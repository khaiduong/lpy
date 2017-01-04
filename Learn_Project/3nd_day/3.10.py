"""
In ra 10 số nguyên tố đầu tiên trên cùng một dòng.
- Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
Primi number is a number which can only devide for it and it**1/2
"""
pri_list = []
for x in range(10000000000):
	if x == 0 or x == 1:
		print(x, 'is not prime number')
	else:
		for n in range(2, x):
			if (x % n) == 0:
				break
		else:
			pri_list.append(x)
			if len(pri_list) == 10:
				break
print(pri_list)
				