"""6.8
Viết 1 script sinh password random, bắt buộc phải chứa ít nhất 1 chữ thường,
1 chữ hoa, 1 số, 1 ký tự punctuation. Trong code chứa hàm test một vòng
loop 10 lần, sinh 10 password và đảm bảo không cái nào giống nhau
"""


import string
import random

### First Way: 
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
list_password = [''.join(random.SystemRandom().choice(chars) for i in range(8)) for _ in range(11) ]
print(list_password)


### Second Way 

def pass_generator(count):
	
	low_alpha = string.ascii_lowercase
	up_alpha = string.ascii_uppercase
	number = string.digits 
	spec_char = string.punctuation
	pw_length = 8
	for i in range(count):
		mypw = ""
		for i in range(pw_length):
		    next_index = random.randrange(len(low_alpha))
		    mypw = mypw + low_alpha[next_index]
		# replace 1 or 2 characters with a number
		for i in range(random.randrange(1,3)):
		    replace_index = random.randrange(len(mypw)//2)
		    mypw = mypw[0:replace_index] + str(random.choice(number)) + mypw[replace_index+1:]
		# replace 1 or 2 letters with an uppercase letter
		for i in range(random.randrange(1,3)):
		    replace_index = random.randrange(len(mypw)//2,len(mypw))
		    mypw = mypw[0:replace_index] + str(random.choice(up_alpha)) + mypw[replace_index+1:]
		# replace 1 or 2 letters with an special letter
		for i in range(random.randrange(1,3)):
		    replace_index = random.randrange(len(mypw)//2,len(mypw))
		    mypw = mypw[0:replace_index] + str(random.choice(spec_char)) + mypw[replace_index+1:]
		print(mypw)
	

pass_generator(10)