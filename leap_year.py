''' Cheking whether a year is a leap year or not, if a year is leap year return True else return False '''

def is_leap(year):
    leap = False
    if year % 4 ==0:
        if year % 100 != 0:
            leap = True
        elif year % 100 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = False

    return leap



year = int(input())
