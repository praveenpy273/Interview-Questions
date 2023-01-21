"""Write a program to count the number of individual characters in a string and
 print it as countand the character name, for example: 'aaaabbbccd', should be
 printed as 4a 3b 2c 1d"""
letter = 'aaaabbbccd'
n_list = {}
count = 0
for i in letter:
    if i in n_list:
        n_list[i] +=1
    else:
        n_list[i]= 1

for k,v in n_list.items():
    print(v,k, sep='',end =' ')

