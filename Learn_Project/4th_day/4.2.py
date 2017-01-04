"""
Tính "điểm" cho từ:
(http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)
Nếu a b c d .... lần lượt bằng 1 2 3 4 ...
thì từ ``attitude`` có giá trị bằng 100
Tính giá trị của các từ:
Input: ["masturbation", pussy", "discipline", "beer", "familug"]
Output: list chứa "điểm" tương ứng của các từ.
Gợi ý::
  import string
  print string.ascii_lowercase
 """

import string
out = []
inp = ["masturbation", "pussy", "discipline", "beer", "familug"]
total2 = [sum([string.ascii_lowercase.index(i) for i in inp[word_index]]) for word_index in range(len(inp))]
print(total2)