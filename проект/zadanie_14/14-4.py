'''
Решите уравнение
  121 x + 1 = 101 7
Ответ запишите в троичной системе счисления. Основание системы счисления указывать не нужно.
'''
for x in range(3, 50):
    if x * x + 2 * x + 1 + 1 == 7 * 7 + 1:
        print(x)

