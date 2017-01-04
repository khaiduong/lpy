#!/usr/bin/python3
"""
8.1
---
Write a python script that simulate ``cat`` command::
    pass 1 argument : path of file (mycat.py /etc/passwd)
    print that file's content
Use ``sys.argv``
"""
from sys import argv


def cat_command():
    script, filename = argv
    with open(filename) as f:
        print(f.read())

if __name__ == "__main__":
    cat_command()
