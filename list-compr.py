# https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = x+1
    j = y+1
    k = z+1
    result =[]
    result = [[x,y,z] for x in range(0,i) for y in range(0,j) for z in range(0,k) if (x + y + z != n) ]
    print(result)