#Определить, какое число в массиве встречается чаще всего.

import random
min_item = 0
max_item = 5
size = 10
max_count = 0
mass_1 = [random.randint(min_item, max_item) for i in range (size)]
for item in mass_1:
    count1 = mass_1.count(item)
    if count1 > max_count:
        max_count = count1 
        max_ch = item
       
print ('Число', max_ch, 'встречается максимально раз')
print ('Количество повторений', max_count)

print(mass_1)
    
    
