"""
Write a python script prints names of all functions and classes in a module (and
count how many functions, how many classes)::
    func_class.py func_class.py
"""

import os
import inspect 

all_func = inspect.getmembers(os, inspect.isfunction)
all_class = inspect.getmembers(os, inspect.isclass)

print(all_func)
print('Module have %d functions' % len(all_func))
print('==================')
print(all_class)
print('Module have %d classes' % len(all_class))
