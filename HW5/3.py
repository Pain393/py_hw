with open('sotr.txt', encoding="utf-8") as f:
    worker = f.readlines()
    zp_all = []
    sum_zp = 0
    for i in range(len(worker)):
        salary = int((worker[i].split())[1])
        if salary < 20000:
            zp_all.append((worker[i].split())[0])
        sum_zp += salary
    print(f'Средняя зарплата всех сотрудников: {sum_zp / len(worker)}')
    print(f'Меньше 20000 рублей получают: {", ".join(zp_all)}')
