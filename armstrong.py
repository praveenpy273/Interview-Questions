n = input('Enter an integer: ')

l = len(n)
n = int(n)
sum = 0
for i in str(n):
    sum += int(i) ** l

print('n:',n, 'sum:',sum)
if sum == n:
    print('Number is armstrong')
else:
    print('Not an armstrng number')
