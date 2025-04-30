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
	quickSort(v, 0, n-1)
	#print(v)


def fill(n):
	v = []
	random.seed(0)
	for _ in range(0,n):
		v.append(random.randint(1, n)) #[1,n]
	return v

def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

if __name__ == '__main__':
	main()