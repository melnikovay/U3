#Во втором массиве сохранить индексы четных элементов первого массива.
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
#надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
#именно в этих позициях первого массива стоят четные числа.
import random
min_item = 0
max_item = 100
size = 10
res_mass = []
mass_1 = [random.randint(min_item, max_item) for i in range (size)]
for idx, num in enumerate (mass_1):
    if num % 2 == min_item:
        res_mass.append(idx)

print('Исходный массив чисел :', mass_1)
print('Список индексов четных чисел:', res_mass)
