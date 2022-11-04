"""

Given a list of integers, write a function the largest sums

of non-adjacent numbers. Numbers can be zero or negative

e,g 1. [2,4,6,8] => output is 12, since we can pick 4,8

e,g 2. [5,1,1,5] => output is 10, since we can pick 5,5

"""

def largest_adjacent_sum(lst=[]):
    l_sum =[]
    num = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and i >= j+2 :
                l_sum.append(lst[i]+ lst[j])
    # return l_sum


    for x in l_sum:
        for y in l_sum:
            if x > y and x > num:
                num =x

    return num
