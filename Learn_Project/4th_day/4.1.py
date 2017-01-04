"""
Cho a, b, c là ba cạnh của tam giác vuông có chu vi 24 cm (perimeter).
Biết độ dài các cạnh <= 10cm.
Viết list comprehension để tìm các bộ a,b,c thoả mãn bài toán.
"""
p = 24
lis_com = [(a,b,c)for b in range(1,11) for a in range(2*b,11) for c in range(1,11) if int(c+a+b) == 24]
print(lis_com)