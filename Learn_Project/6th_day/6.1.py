"""
6.1
---

Cho tiền điện sinh hoạt được tính theo công thức:

- 50 số đầu: 1230 VND/số.

- 50 số tiếp: 1530 VND/số.

- Các số tiếp theo: 1786 VND/số.

Viết function tính tiền điện sinh hoạt với:

- Input: số điện sử dụng

- Ouput: số tiền phải trả

Và 1 function tính số tiền điện của nhiều tháng, với:

- Input: list số điện các tháng
- Output: list số tiền các tháng

Gọi hàm đó với list [1, 29, 1235, 69, 100]. Copy kết quả list output rồi
paste vào cuối file (commented).
"""

import sys


def electrical_calculations(electrical_number):
	try:
		number =  int(electrical_number)
	except ValueError:
		print('Please input a number, or you might be beaten to dead!!!!')
		exit(-1)
	if int(electrical_number) in range(51):
		total = 1230*int(electrical_number)
	elif int(electrical_number) in range(51, 101):
		total = 1530*(int(electrical_number) - 50) + (1230*50)
	elif int(electrical_number) > 102:
		total = 1786*(int(electrical_number) - 100) + (1230*50) + (1530*50)
	return total
electrical_calculations('10')


lst = [1, 29, 1235, 69, 100]
electrical_bills = [electrical_calculations(num) for num in lst]
print(electrical_bills)
#[1230, 35670, 2165110, 90570, 138000]