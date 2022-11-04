"""

Given an input string, find the first recurring character in it.

"""

letter = input('Enter a string: ')
x = {}

for i in letter:
    if i not in x:
        x[i] = 1
    else:
        x[i] += 1

for j in x:
    if x[j] > 1:
        print(j)
        break
