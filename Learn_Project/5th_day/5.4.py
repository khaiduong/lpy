"""
Viết function tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1, 
các dòng chẵn chứa giá trị 2 * số dòng hiện tại.
Viết function in ra 10 dòng cuối cùng của file nói trên.
(Nâng cao) Viết function in ra kích thước của file nói trên tính theo byte. 
# note: should use tail not open file or readfile, with files which have the size is too large, cp ram might overload.
"""

def dump_ram_fuct(n):
	print('Be care before call, as you can be beaten to death!!!! Y_Y ')
	with open('./30Mil_Lines.txt','w') as f:
		for i in range(1,n+1):
			if i % 2 == 0:
				f.write('This is even line number %d, and duplicate is %d\n'%(i,i*2) )
			else:
				f.write('1'*30 +'\n')

def tail(n):
	count = 0
	with open('./30Mil_Lines.txt') as f:
		lst = [line for line in f if count < n]
		print(lst[-n:])

dump_ram_fuct(200000)
print('++++++++++++')
tail(5)