# Найдите сумму чисел, кратных 3 или 5 до A.
def solution(A):
    j = 0
    for i in range(A):
        if i % 3 == 0 or i % 5 == 0:
            j += i
    return(j)


print(solution(10))
