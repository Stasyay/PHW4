# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 

import re
from sympy import symbols
from sympy import sympify

def read_file(file):
    with open(file) as data:
        pol = data.read()
    return pol

def convert_pol(polynomial):
    polynomial = polynomial.replace('= 0', '')
    polynomial = polynomial.split('+')
    return polynomial

def get_list(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(sympify(lst[i]))
    return new_lst

x = symbols('x')
file = 'file.txt'
file1 = 'file1.txt'

pol = convert_pol(read_file(file)) 
pol1 = convert_pol(read_file(file1))

pol = ([0,] * (len(pol1) - len(pol))) + pol
pol1 = ([0,] * (len(pol) - len(pol1))) + pol1

new_pol = get_list(pol)
new_pol1 = get_list(pol1)

total_pol = str(list(map(sum, zip(new_pol,new_pol1))))+ ' = 0'

with open('total_file.txt', 'w') as data:
    data.write(total_pol)

print(f'первый исходный многочлен {read_file(file)}')
print(f'второй исходный многочлен {read_file(file1)}')
print(f'сумма многочленов {total_pol}')
