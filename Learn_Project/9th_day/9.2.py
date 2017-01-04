"""
Given a list ``['nhung', 'bong', 'hoa', 'nho']``, write a function which
prints each item of the list.
Must NOT using ``for ... in``, indexing.

Tips:

- iterator
"""

def print_from_list(list):
	a = iter(list)
	n = 0
	while n < len(list):
		print(next(a))
		n +=1

lst = ['nhung', 'bong', 'hoa', 'nho']
print_from_list(lst)



mas = 'ld1111'
slas = ['ld2222', 'ld3333']


lst = [mas] + slas


print('+++++++++++')
print(lst)