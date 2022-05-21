'''
Определите, при каком наибольшем введённом значении переменной s
программа выведет число 64
Python
s = int(input())
s = s // 10
n = 1
while s < 51:
s = s + 5
n = n * 2
print(n)
'''
for i in range(1, 1000):
    s = i
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
        if n == 64:
            print(i)
