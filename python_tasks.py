# Найдите сумму чисел, кратных 3 или 5 до A.
def solution(A):
    j = 0
    for i in range(A):
        if i % 3 == 0 or i % 5 == 0:
            j += i
    return(j)

# If the numbers is even return true. If it's odd, return false. 
# The following symbols/commands have been disabled: %, mod
# (Бинарные четные числа оканчиваются на 0, нечетные – на 1)
def is_even(n):
    return True if bin(n)[-1] == "0" else False

# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# for example, a tower of 3 floors looks like below
# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]
def tower_builder(n_floors):
    tower = []
    i = 1
    j = 1
    n = n_floors
    while i <= n_floors:
        tower.append(" " * (n - 1) + "*" * j + " " * (n - 1))
        i += 1
        j += 2
        n -= 1
    return tower

# Your are given a string. You must replace the word(s) coverage by covfefe,
# however, if you don't find the word coverage in the string,
# you must add it at the end of the string with a leading space.
def covfefe(s):
    if "coverage" in s:
        return s.replace("coverage", "covfefe")
    else:
        return (s + " covfefe")
