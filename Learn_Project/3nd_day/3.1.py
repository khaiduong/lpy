n =100000 #raw_input('--> ')
try:
        s = int(n)
except ValueError:
        print("Not a number, it's a monster...")
        exit(1)
binary = bin(s)
#for i in range(11):
#	binary = bin(i)
print(binary[binary.rfind('1'):])