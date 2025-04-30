import sys
import random
import math

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

def main ():
	n = 4000000
	v = fill(n)
	#print(v)
	shell_sort(v, n)
	#print(v)




if __name__ == '__main__':
	main()