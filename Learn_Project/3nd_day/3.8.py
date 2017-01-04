n = 0
lis = [] 
while n < 1000:
	if n % 3 == 0 and n % 5 == 0:
		#print(n)
		lis.append(n) 
	#n +=1
print(sum(lis))