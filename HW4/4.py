ish_spis = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_spis = [i for i in ish_spis if ish_spis.count(i) == 1]
print(new_spis)