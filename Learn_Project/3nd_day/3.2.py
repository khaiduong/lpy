n = -2#raw_input('--> ')
try:
        s = int(n)
except ValueError:
        print("Not a number, it's a monster...")
        exit(1)
if n > 0:
	print("this is positive number")
elif n < 0:
	print(" this is negative number")
else:
	print("Zero!!!!")