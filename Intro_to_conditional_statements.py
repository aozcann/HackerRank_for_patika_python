# https://www.hackerrank.com/challenges/30-conditional-statements/problem?h_r=email&unlock_token=12d6aded1a3caf176c6ab06787bca0863f231455&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    """
    If  is odd, print Weird
If  is even and in the inclusive range of 2  to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""
    if  N % 2 == 1 :
        print("Weird")
    elif  N % 2 == 0 and 2 < N < 5 :
        print("Not Weird")
    elif N % 2 == 0 and 6 <= N <= 20:
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")
    
