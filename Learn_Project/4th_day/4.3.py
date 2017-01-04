"""
Given a list of numbers (float or int), find the biggest element in that list.
Compare output with max(li)::

  assert mymax(li) == max(li)
"""

list1 = [8, 39, 45, 2, 3, 5, 100, 34.8, 100.50000]
list2 = (sorted(list1, key=float))
print(list2[-1])