n = int(input('Введите количество экспонатов: '))
m = int(input('Введите количество заходов: '))
k = int(input('Введите колиечство киллограм: '))

exhibit = []
for i in range(n):
    w, c = map(int, input('Введедите вес и стоимость экспоната: ').split())
    exhibit.append([w, c, c/w])

exhibit.sort(key=lambda x:x[2], reverse=True)

print()
for i in range(m):
    bag_weight = 0
    bag_coast = 0
    j = 0
    while j < len(exhibit):
        if bag_weight + exhibit[j][0] <= k:
            bag_weight += exhibit[j][0]
            bag_coast += exhibit[j][1]
            exhibit.pop(j)
        if bag_weight == k:
            break
        j += 1
    print(f'{i+1} заход -- суммарная стоимость украденного: {bag_coast}')



