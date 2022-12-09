#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#     Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

from random import randint
from sympy import symbols
from math import prod

def write_file(file, koef):
    with open(file, 'w') as data:
        data.write(get_polynomial(koef))

def get_polynomial(k):
    max_val=100
    koeff=[randint(1 ,max_val) for i in range(k)] + [randint(1,max_val)]
    x = symbols('x')

    pol = str(sum(map(prod,zip(koeff,[x**i for i in range(k+1)])))) + ' = 0'
    return pol

k = int(input('Введите натуральную степень для первого многочлена k: '))
k1 = int(input('Введите натуральную степень для второго многочлена k: '))
file = 'file.txt'
file1 = 'file1.txt'

write_file(file, k)
write_file(file1, k1)