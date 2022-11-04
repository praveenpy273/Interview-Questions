"""Write a program to print only non repeating elements in a string"""

example = 'pythonprogramming'
d = {}

for i in example:
    count = 0
    for j in example:
        if i == j:
            count += 1
        if count > 1:
            break

    if count == 1:
        print(i, end= '')

        
