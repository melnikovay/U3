#В массиве найти максимальный отрицательный элемент. Вывести на экран его
#значение и позицию в массиве. Примечание к задаче: пожалуйста
#не путайте «минимальный» и «максимальный отрицательный». Это два
#абсолютно разных значения.
import random
min_item = -100
max_item = 100
size = 20
mass_1 = [random.randint(min_item, max_item) for i in range (size)]
max_ch = min_item
for idx, num in enumerate (mass_1) :
    if num   < 0:
        ot_ch = num
        if ot_ch > max_ch:
            max_ch = ot_ch
print ('Массив ', mass_1)
print ('Максимальный отрицательный элемент массива ', max_ch)
