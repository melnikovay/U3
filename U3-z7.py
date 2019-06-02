#В одномерном массиве целых чисел определить два наименьших элемента.
#Они могут быть как равны между собой
#(оба являться минимальными), так и различаться.
import random
min_item = 1
max_item = 20
size = 15
count1 = 0
mass_1 = [random.randint(min_item, max_item) for i in range (size)]
min_ch = max_item
min_ch2 = max_item
for idx, num in enumerate (mass_1) :
    if num   < min_ch:
        min_ch = num
count1 = mass_1.count(min_ch)
if count1 > 1:
    min_ch2 = min_ch
else:
    for idx, num in enumerate (mass_1) :
            if min_ch < num < min_ch2:
                min_ch2 = num
            
print ('Массив', mass_1)
print ('Первое минимальное число массива', min_ch)
#print(count1)
print ('Второе минимальное число', min_ch2)
