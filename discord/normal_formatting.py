import csv

CSV_FP = 'Direct Messages - Private - SpaceJew [377634224699867147].csv'

with open(CSV_FP, newline='', encoding="utf-8") as source, open('formatted.txt', encoding="utf-8", mode='w') as output:
    reader = csv.DictReader(source)
    for line in reader:
        output.write(f'{line["Author"].split("#")[0]}: {line["Content"]}\n')