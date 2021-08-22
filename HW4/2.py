ish_spis = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_spis = [num1 for num1, num2 in zip(ish_spis[1:], ish_spis[:-1]) if num1 > num2]
print(new_spis)
