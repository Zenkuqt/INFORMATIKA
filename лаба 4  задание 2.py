import csv
import json

INPUT_FILENAME = "input1.csv"
OUTPUT_FILENAME = "output.json"

# читаем csv файл
with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
    r = csv.DictReader(f)
    data = list(r)

# записываем в json
with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# выводим результат
with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")

