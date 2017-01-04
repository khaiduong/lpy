"""
6.7
---
Viết function tính tổng của tất cả các argument được gọi. Chạy function này với
các argument dưới::
  sumall(1,2,3,4,5,6,7)
  sumall(1,2,3,4,5,6,7,8,9)
"""

def sum_args(*args):
	print(sum(args))

sum_args(1,2,3,4,5,6,7)
sum_args(1,2,3,4,5,6,7,8,9)