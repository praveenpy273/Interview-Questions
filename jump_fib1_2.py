"""Write a program to find the number of ways to reach a point
point 1 can be reached in 1 way, point 2 in 2 ways , starting point 3 onwards it should be the last way+ second last way
so for point 3 , 3 ways, for point4, 5 ways, for point 5 , 8 ways, point 6, 13 ways and so on"""

n1= 1
n2 = 2
res = 0
n = int(input('Enter an integer: '))
i = 1
while i <= n:
    if i == 1:
        res = 1
    elif i == 2:
        res = 2
    else:
        res = n1 + n2
        n1,n2 = n2, res
    i += 1

print(res)
