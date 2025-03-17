import sys

def main():
   if len(sys.argv) != 2:
      print("Usage:", sys.argv[0], "<n>")
      return
   n = int(sys.argv[1])
   if (n<0):
      print("Value of n must be non-negative.")
   result = fib( n )
   print (f'Fibonacci({n}) = {result}')

def fib (n):
   if n == 0:
      return 0
   if n == 1:
      return 1
   curr = 0
   prev2 = 0
   prev1 = 1
   for _ in range(2,n+1):
      curr = prev1 + prev2
      prev2 = prev1
      prev1 = curr
   return curr

if __name__ == '__main__':
   main()
