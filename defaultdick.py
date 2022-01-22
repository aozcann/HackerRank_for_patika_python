# Enter your code here. Read input from STDIN. Print output to STDOUT
# dictionary
from collections import defaultdict

n, m = map(int, input().split(' '))

list1 = []


for i in range(0,int(n)):
    list1.append(input())
    
    list2 = []
for i in range(0,int(m)):
    list2.append(input())
    
    
d = defaultdict(list)


for i in range(n):
    d[list1[i]].append(i+1)

for i in list2:
    if i in d:
        print(*d[i])
    else:
        print(-1)
        
