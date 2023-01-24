"""

Convert the string "123" into 123, without using the built-api `int()`

"""

s = "123"
n= []

for i in s:
    n.append(ord(i))

for j in n:
    print(chr(j),end =' ')
