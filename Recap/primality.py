#Aim:To check primality (if no is prime or not)

#Method 1:
#Gives list of factors
def factors(n):
  fl = [] # factor list
  for i in range(1, n+1):
    if (n%i) == 0:
      fl.append(i)
  return fl
  
def prime(n):
    return factors(n) == [1,n]

#Method 2:
import math
def prime(n):
  (result,i) = (True, 2)
  while (result and (i < math.sqrt(n))):
    if (n%i) == 0:
      result = False
    i = i + 1
  return result
