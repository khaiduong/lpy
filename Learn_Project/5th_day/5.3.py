"""
Write a function that prints the numbers from 1 to 100. 
But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print 
“Buzz”. For numbers which are multiples of both 3 and 5 print
“FizzBuzz”.
"""

def print_fizzbuzz_number(num): 
	if type(num) == int:
		for i in range(num):
			if i % 15 == 0:
				print('FizzBuzz', end=', ')
			elif i % 5 == 0:
				print('Buzz', end=', ')
			elif i % 3 == 0:
				print('Fizz', end=', ')
			else:
			 	print(i, end=', ')
			
	else: 
		print('Your input %s is not a number, PLEASE INPUT AGAIN!!!!!' %num)


print_fizzbuzz_number('50')