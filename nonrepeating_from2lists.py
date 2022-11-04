"""Write a program to print non common elements in 2 lists"""
list1 = [1,2,3,4,5,6]
list2=[1,2,3,7]

list1= set(list1)
list2 = set(list2)

ans = set(list1)- set(list2)
ans = list(ans)
print(ans)
