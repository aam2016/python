# Найдите сумму чисел, кратных 3 или 5 до A.
def solution(A):
    j = 0
    for i in range(A):
        if i % 3 == 0 or i % 5 == 0:
            j += i
    return(j)


#If the numbers is even return true. If it's odd, return false. 
#The following symbols/commands have been disabled: %, mod
import math


def is_even(n):
    return True if divmod(n, 2)[1] == 0 else False
