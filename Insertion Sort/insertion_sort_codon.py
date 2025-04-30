import sys
import random

def fill(n):
	v = []
	random.seed(0)
	for _ in range(0,n):
		v.append(random.randint(1, n)) #[1,n]
	return v

def insertion_sort(v):
	for i in range(1, len(v)): #[1,len(v)]
		t = v[i]
		# Inner for
		j = i-1
		while j >= 0 and v[j] > t:
			v[j+1] = v[j]
			j -= 1
		v[j+1] = t

def main ():
	n = 50000
	v = fill(n)
	#print(v)
	insertion_sort(v)
	#print(v)






if __name__ == '__main__':
	main()