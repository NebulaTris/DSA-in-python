#Linear Search
def linear_search(obj, item, start=0):
 for i in range(start, len(obj)):
 if obj[i] == item:
 return i
 return -1
arr=[1,2,3,4,5,6,7,8]
x=4
result=linear_search(arr,x)
if result==-1:
 print ("element does not exist")
else:
 print ("element exist in position %d" %result)

#Binary Search
array =[1,2,3,4,5,6,7,8,9]
def binary_search(searchfor,array):
  lowerbound=0
  upperbound=len(array)-1
  found=False
  while found==False and lowerbound<=upperbound:
    midpoint=(lowerbound+upperbound)//2
    if array[midpoint]==searchfor:
      found =True
      return found
    elif array[midpoint]<searchfor:
      lowerbound=midpoint+1
    else:
      upperbound=midpoint-1
    return found
  
searchfor=int(input("what are you searching for?"))
if binary_search(searchfor,array):
 print ("element found")
else:
 print ("element not found")

#Fibonacci Search
# Python3 program for Fibonacci search.
from bisect import bisect_left
# Returns index of x if present, else
# returns -1
def fibMonaccianSearch(arr, x, n):

 # Initialize fibonacci numbers
 fibMMm2 = 0 # (m-2)'th Fibonacci No.
 fibMMm1 = 1 # (m-1)'th Fibonacci No.
 fibM = fibMMm2 + fibMMm1 # m'th Fibonacci
 # fibM is going to store the smallest
 # Fibonacci Number greater than or equal to n
 while (fibM < n):
 fibMMm2 = fibMMm1
 fibMMm1 = fibM
 fibM = fibMMm2 + fibMMm1
 # Marks the eliminated range from front
 offset = -1;
 # while there are elements to be inspected.
 # Note that we compare arr[fibMm2] with x.
 # When fibM becomes 1, fibMm2 becomes 0
 while (fibM > 1):
 
17
 # Check if fibMm2 is a valid location
 i = min(offset+fibMMm2, n-1)
 # If x is greater than the value at
 # index fibMm2, cut the subarray array
 # from offset to i
 if (arr[i] < x):
 fibM = fibMMm1
 fibMMm1 = fibMMm2
 fibMMm2 = fibM - fibMMm1
 offset = i
 # If x is greater than the value at
 # index fibMm2, cut the subarray
 # after i+1
 elif (arr[i] > x):
 fibM = fibMMm2
 fibMMm1 = fibMMm1 - fibMMm2
 fibMMm2 = fibM - fibMMm1
 # element found. return index
 else :
 return i
 # comparing the last element with x */
 if(fibMMm1 and arr[offset+1] == x):
 return offset+1;
 # element not found. return -1
 return -1
# Driver Code
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
n = len(arr)
x = 80
print("Found at index:",
 fibMonaccianSearch(arr, x, n))
