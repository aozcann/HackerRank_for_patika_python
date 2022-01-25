# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    
    if year >= 1900 and year <= 10**5 :
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            leap = True
        else :
            leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))