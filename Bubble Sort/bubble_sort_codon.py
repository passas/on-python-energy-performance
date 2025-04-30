import sys
import random

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
def main ():
	n = 30000
	#print(v)
	bubble_sort(v)
	#print(v)

if __name__ == '__main__':
	main()