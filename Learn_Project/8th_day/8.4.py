"""
Write a python script simulates
`head <http://manpages.ubuntu.com/manpages/trusty/en/man1/head.1.html>`_
and `tail <http://manpages.ubuntu.com/manpages/trusty/en/man1/tail.1.html>`_
commands.
Usage::
  head_tail.py -h file_path
  Print 10 first lines of file_path
  head_tail.py -t file_path
  Print 10 last lines of file_path
Use ``sys.argv``
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--head", help="head command, print numbers of first lines of a file", action='store_true')
parser.add_argument("-t", "--tail", help="tail command, print number of last lines of a files", action="store_true")
parser.add_argument("file", type=argparse.FileType('r'))
parser.add_argument("square", type=int, help="display a square of a given number")
args = parser.parse_args()

if args.head:
    n = 1
    while n<=int(args.square):
        print(args.file.readline(), end='')
        n+=1
elif args.tail:
    output = []
    for line in args.file:
        output.append(line)
        if len(output) >= int(args.square):
            output.pop(0)
    for line in output:
        print(line, end='')
else:
    print(parser.print_help())