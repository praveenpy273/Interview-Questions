"""Write a program to print only non common elements in a string"""

example = 'pythonprogramming'
d = {}

for i in example:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for k,v in d.items():
    if d[k] == 1:
        print(k,end='')
