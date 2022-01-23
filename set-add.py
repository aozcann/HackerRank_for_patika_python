# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-add/problem
country = []
s = set(country)

x = input()

for i in range(int(x)):
    s.add(input())
    i += 1
print(len(s)) 
