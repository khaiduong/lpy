"""
a, b, c là các số nguyên dương nhỏ hơn 10 và:
a + b/c = 10
In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).
Ví dụ:
- output: [[9, 1, 1], ...]
"""
lis = []
for a in range(0,10):
	for b in range(0,10):
		for c in range(1,10):
			if a + b/c == 10:
				lis.append([a,b,c])

print(lis)

