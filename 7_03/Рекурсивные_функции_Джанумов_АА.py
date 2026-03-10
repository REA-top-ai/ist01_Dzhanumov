# task 1 и мой комент. я разобрался в модуле тайм
# и разбирался в том как можно сравнивать время. а еще :.xf где х - колво до запятой
# upd 2 , антон андреевич сказал что так делать не надо( но ладно.

import time

def factor_recursion(n):
    if n == 1:
        return 1
    return n * factor_recursion(n-1)

def factor_cycle(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


iterations = 100000 


start = time.perf_counter()
for i in range(iterations):
    factor_recursion(10)
end = time.perf_counter()

rec_time = (end - start) / iterations


start = time.perf_counter()
for i in range(iterations):
    factor_cycle(10)
end = time.perf_counter()

cycle_time = (end - start) / iterations


print(f'рекурсия: {rec_time:.10f}')
print(f'цикл: {cycle_time:.10f}')


print("быстрее цикл" if rec_time > cycle_time else "быстрее рекурсия")

# task 2

def kvadratt(n: list):
    return [i**2 for i in n]