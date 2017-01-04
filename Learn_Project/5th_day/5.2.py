"""
Verify that current machine whether linux based OS?
Hint: using sys module
https://docs.python.org/2/library/sys.html
"""
import sys

if sys.platform.startswith('linux'):
	print('Great! Linux based.')
else:
	print('Kind of SUCK things!!!')