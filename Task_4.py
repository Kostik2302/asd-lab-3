cities = {
    'Sydney': {
        'Melbourne': 874,
        'Brisbane': 936,
        'Perth': 3280,
        'Adelaide': 1329,
        'Canberra': 286
    },
    'Melbourne': {
        'Sydney': 874,
        'Brisbane': 1686,
        'Perth': 2756,
        'Adelaide': 727,
        'Hobart': 609
    },
    'Brisbane': {
        'Sydney': 936,
        'Melbourne': 1686,
        'Perth': 4316,
        'Cairns': 1702,
        'Gold Coast': 81
    },
    'Perth': {
        'Sydney': 3280,
        'Melbourne': 2756,
        'Brisbane': 4316,
        'Adelaide': 2134,
        'Darwin': 4141
    },
    'Adelaide': {
        'Sydney': 1329,
        'Melbourne': 727,
        'Perth': 2134,
        'Canberra': 1165,
        'Alice Springs': 1539
    },
    'Canberra': {
        'Sydney': 286,
        'Adelaide': 1165,
        'Melbourne': 662,
        'Gold Coast': 1326,
        'Hobart': 1166
    },
    'Cairns': {
        'Brisbane': 1702,
        'Darwin': 2326
    },
    'Gold Coast': {
        'Brisbane': 81,
        'Canberra': 1326
    },
    'Hobart': {
        'Melbourne': 609,
        'Canberra': 1166
    },
    'Darwin': {
        'Perth': 4141,
        'Cairns': 2326
    },
    'Alice Springs': {
        'Adelaide': 1539
    }
}

marks = {}
visited = []
path_from_Sydney = {}

for i in cities.keys():
    marks[i] = 1000000
    path_from_Sydney[i] = 'Sydney'
marks['Sydney'] = 0

while len(visited) < len(cities):
    min_mark = 10000
    min_mark_key = ''
    for i in marks.keys():
        if marks[i] < min_mark and i not in visited:
            min_mark = marks[i]
            min_mark_key = i
    for i in cities[min_mark_key].keys():
        if i not in visited and marks[i] > marks[min_mark_key] + cities[min_mark_key][i]:
            marks[i] = marks[min_mark_key] + cities[min_mark_key][i]
            path_from_Sydney[i] = min_mark_key
    visited.append(min_mark_key)

print('Название города -- кратчайшее расстояние от Сиднея до него -- город, из которого пришли: ')
for i in marks.keys():
    print(f'{i} -- {marks[i]} -- {path_from_Sydney[i]}')



    
            
