import sys

# n = 200000000 # +- 1m9s

def isPrime(n):
   if n<=0:
      return False
   if n<=3:
      return True
   for i in range(3,n):
      if n % i == 0:
         return False
   return True

def main():
   n = 300000000
   for i in range(1,n):
      r = isPrime( n )
      #print(r)

if __name__ == '__main__':
   main()
