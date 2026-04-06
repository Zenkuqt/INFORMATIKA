import json
# модуль для работы с JSON файлами
with open('input.json') as f:  # открываем файл
    data = json.load(f)

s = 0  # переменная для суммирования
for d in data:
    s += d['score'] * d['weight']

print(round(s, 3))

