string = "co cai quan que treo tren cay che"
list1 = []
for i in string:
	count = string.count(i)
	if count == 1:
		list1 += i

print(list1)


# difference way
list2=[i for i in string if string.count(i) == 1]
print(list1)