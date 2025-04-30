import sys

# n = 200000000 # +- 1m9s

def main():
   if len(sys.argv) != 2:
      print("Usage: " + sys.argv[0] + " <n>")
      return
   n = int(sys.argv[1])
   if (n<0):
      print("Value of n must be non-negative.")
   for i in range(1,n):
      r = isPrime( n )
      #print(r)

def isPrime(n):
   if n<=0:
      return False
   if n<=3:
      return 1
   for i in range(3,n):
      if n % i == 0:
         return False
   return True

if __name__ == '__main__':
   main()
