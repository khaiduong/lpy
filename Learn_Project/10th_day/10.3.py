"""
10.3
----

- Viết script lấy top **x** câu hỏi được vote cao nhất của tag **y** trên stackoverflow.com

- In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs
"""

import requests
import json

url = "https://api.stackexchange.com/2.2/tags?order=desc&sort=popular&site=stackoverflow"

res = requests.get(url)
content = json.loads(res.text)
items = content['items']
for i in items:
	if 'python' in i['name']:
		print(i)

