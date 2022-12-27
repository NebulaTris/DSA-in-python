# Aim:Compute the list of common factors from 1 to min(m,n)

#Method 1:
def gcd(m,n):
  cf = [] # List of common factors
  for i in range(1, min(m,n) + 1):
    if (m%i) == 0 and (n%i) == 0:
      cf.append(i)
  return cf[-1]

#Method 2:
def gcd(m,n):
  for i in range(1, min(m,n) + 1):
    if (m%i) == 0 and (n%i) == 0:
      mrcf = i
    return mrcf
