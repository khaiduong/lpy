"""
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Form::

  ketqua.py [NUMBER1] [NUMBER2]

Libs:

- beautifulsoup4
- requests
- logging

Tips:

- ``nargs`` https://docs.python.org/2/library/argparse.html
"""
import requests
import logging
import json
from bs4 import BeautifulSoup
import html



url = "http://ketqua.net/"
res = requests.get(url)

print(res)

soup = BeautifulSoup(res.text, 'html.parser').encode("ascii")
print(type(soup))
print(soup)
#rint(soup.prettify())
#print(soup.get_text())

#print(soup.title)
