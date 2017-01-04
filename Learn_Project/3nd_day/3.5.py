n = raw_input('--> ') #raw_input('Please input a number in range 1 - 12: ')
try:
        input = int(n)
except ValueError:
        print("Not a number, it's a monster...")
        exit(-1)
else: 
	if 1 <= n < 13:
		print('correct! processing....')
	else:
		print('Stupid!! Only number in range 1 -> 12')
		exit(-1)
day = ''
month = ''
dic = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'June', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Nov', 11:'Oct', 12:'Dec'}
month = dic[n]
if n == 2:
	day = 28
elif (n <=7 and n % 2 != 0) or (n >=8 and n % 2 == 0):
	day = 31
else:
	day = 30
print(month, 'has', day, 'days')

# difference way: 
#Unpacking a list



