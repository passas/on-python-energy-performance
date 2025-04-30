import sys
import random
import math

def main ():
	if len(sys.argv) != 2:
		sys.exit("Usage: " + sys.argv[0] + " <n>")
	try:
		n = int(sys.argv[1])
	except ValueError:
		sys.exit('The argument must be a positive integer.')
	else:
		if (n<0):
			sys.exit('The argument must be a positive integer.')
	v = fill(n)
	#print(v)
	shell_sort(v, n)
	#print(v)


def fill(n):
	v = []
	random.seed(0)
	for _ in range(0,n):
		v.append(random.randint(1, n)) #[1,n]
	return v

def swap(v, p, q):
	t = v[p]
	v[p]=v[q]
	v[q]=t

def shell_sort(v, n):
	gap = math.floor(n/2)
	while gap > 0:
		for i in range(gap,n):
			j = i-gap
			while j>=0 and v[j]>v[j+gap]:
				swap(v, j, j+gap)
				j-=gap
		gap = math.floor( gap/2 )

if __name__ == '__main__':
	main()