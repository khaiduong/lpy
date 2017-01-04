"""
6.2
---
Given a list::

  li = ['meo', 'bo', 'ga', 'cho', 'chim', 'lon']

Write one-liner python to return a list of::

   [('meo', 'bo'), ('ga', 'cho'), ('chim', 'lon')]
"""
li = ['meo', 'bo', 'ga', 'cho', 'chim', 'lon']
print(list(zip(li[::2], li[1::2])))
