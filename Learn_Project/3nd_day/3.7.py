n = 1
r = 1
while n < 100:
	if n % 5 == 0:
		print(n, '==', r ,'x', 5 )
		r +=1
	n +=1 


#Difference way: 
lis = [1,2,3,4,5,6,7,8,9]
print(lis[::-1])	