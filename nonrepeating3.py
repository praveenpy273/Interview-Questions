"""Write a program to print only non common elements in a string"""

example = 'pythonprogramming'

for i in example:
    if example.count(i)==1:
        print(i, end="")
