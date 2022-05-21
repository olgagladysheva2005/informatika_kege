"""
(В. Шелудько) Значение выражения 7**103 + 6∙7**104 – 3∙7**57 + 98 записали в системе счисления с основанием 7.
Найдите сумму цифр получившегося числа и запишите её в ответе в десятичной системе счисления.
"""
x = 7**103 + 6*7**104 - 3*7**57 + 98
s = 0
while x > 0:
    s += x % 7
    x = x // 7
print(s)