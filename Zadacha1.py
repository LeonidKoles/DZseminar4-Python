#  Вычислить число π c заданной точностью d

# *Пример:* - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# d =input('Укажите точность \n')


k = 1
pi = 0

for i in range(0, 1000000):
    if i % 2 == 0:
        pi += 4 / k
    else:
        pi -= 4 / k
    k += 2

d = float(input('Введите желаеммую точность \n'))
cou = 0
if 0 < d < 1:
    while d < 1:
        d *= 10
        cou += 1
print(cou)        
print(round(pi, cou))