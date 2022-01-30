# https://www.hackerrank.com/challenges/np-arrays/problem
import numpy

def arrays(arr):
    arr = numpy.array(arr[::-1],float)
    
    return arr
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
