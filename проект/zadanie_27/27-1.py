f = open('27_8.txt')
n = int(f.readline())

sum_ost = [1096594666] * 43
k = [0] * 43

mx = 0
ln = 0

s = 0

sum_ost[0] = 0
k[0] = -1

for i in range(n):
    x = int(f.readline())
    s = s + x
    ost = s % 43

    if s - sum_ost[ost] == mx:
        ln = min(ln, i - k[ost])

    if s - sum_ost[ost] > mx:
        mx = s - sum_ost[ost]
        ln = i - k[ost]

    if sum_ost[ost] == 1096594666:
        sum_ost[ost] = s
        k[ost] = i

print(ln)
