"""
(М.В. Кузнецова) Значение арифметического выражения: 9**7 - 3**10 + 3**21 – 9 записали в системе счисления с основанием 3.
Сколько цифр «2» содержится в этой записи?
"""
x = 9 ** 7 - 3 ** 10 + 3 ** 21 - 9
k = 0
while x > 0:
    if x % 3 == 2:
        k += 1
    x //= 3
print(k)
