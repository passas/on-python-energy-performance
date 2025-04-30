import sys
import random

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
	#bubble_sort(v)
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

def bubble_sort(v):
	for i in range(len(v)-1, 1, -1): #[len-1, 1[
		for j in range(0, i):
			if v[j]>v[j+1]:
				swap(v, j, j+1)

if __name__ == '__main__':
	main()