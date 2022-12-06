# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_num(x):
    d = 2
    while x % d !=0:
        d += 1
    return d==x

n = int(input('Введите число: '))
x = 2
lst_multi =[]
while n / x!=1:
    if n % x == 0:
        n /= x
        lst_multi.append(x)
    else:
        x +=1
        prime_num(x)
lst_multi.append(x)    

print(lst_multi)



# n = int(input('Введите число: '))
# multipliers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# lst_multi =[]

# for i in range(0, len(multipliers)):
#     while n / multipliers[i]!=1:
#         if n % multipliers[i] == 0:
#             n = n / multipliers[i]
#         else:
#             i +=1
#         lst_multi.append(multipliers[i])
#     break
# print(lst_multi)


