"""
Given an integer list from -10 to 10 except 0, write a function:
- calculate its sum without using function ``sum``.
- calculate its product
Return a tuple (sum, product).
Input::
  li = range(-10, 11)
  li = list(li)
  li.remove(0)
Compare output with this::
  from functools import reduce
  assert sum_and_product(li) == (sum(li), reduce(lambda x,y: x*y, li))
"""
