import json

prib = {}
ub = {}
med = []
with open('7.txt', encoding="utf-8") as f:
    for line in f:
        name, form, proceeds, costs = line.split()
        income = int(proceeds) - int(costs)
        if income > 0:
            med.append(income)
            prib[name] = income
        else:
            ub[name] = abs(income)
    if med != []:
        medium = sum(med) / len(med)
        print(f'Средняя прибыль компаний: {medium}\n')
    else:
        print('Все компании из перечисленных работают в убыток')
    statistics = [prib, ub]
    print(f'Статистика фирм:\n{statistics}\n')
with open('7.json', 'w+') as js:
    json.dump(statistics, js)
    js.seek(0)
    res = js.read()
    print(f'Вот, что хранится в файле 7.json:\n{res}')