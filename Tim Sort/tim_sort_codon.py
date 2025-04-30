import sys
import random

def fill(n):
	v = []
	random.seed(0)
	for _ in range(0,n):
		v.append(random.randint(1, n)) #[1,n]
	return v

def main ():
	n = 50000000
	v = fill(n)
	#print(v)
	v.sort()
	#print(v)




if __name__ == '__main__':
	main()