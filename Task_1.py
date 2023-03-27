n = int(input('Введите сдачу: '))
all_coins = {}
for i in range(4):
    coin = input('Введите количество монет и номинал через пробел: ').split()
    m, s = map(int, coin)
    all_coins[s] = m

all_coins = dict(sorted(all_coins.items(), reverse=True))

print()
for i in all_coins.keys():
    count = n // i
    print(f'Монет номиналом {i} -- {min(all_coins[i], count)}')
    n -= i * min(all_coins[i], count)

if n > 0:
    print()
    print(f'Данным набором монет жадным алгоритмом полностью выдать сдачу не удалось. Осталось {n} непогашенные у.е.')


    


