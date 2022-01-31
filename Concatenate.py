# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

x,y,z = map(int, input().split(" "))

list_1 = [1,2]
array_1 = list_1*x
array_1 = np.array(array_1)
list_2 = [3,4]
array_2 = list_2*y
array_2 = np.array(array_2)
sum_array = np.concatenate((array_1,array_2))

print(sum_array.reshape(-1,z))


