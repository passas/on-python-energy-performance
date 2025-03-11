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
   
   return fib(n-1) + fib(n-2)


if __name__ == '__main__':
   main()
