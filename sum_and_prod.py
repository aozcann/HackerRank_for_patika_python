# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy as np



n,m = (map(int,input().split()))

arr = np.array([input().split() for i in range(n)],int)
arrsum = np.sum(arr, axis = 0)
arrprod = np.prod(arrsum)
print(arrprod)
