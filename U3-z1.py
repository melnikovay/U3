#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
#кратны каждому из чисел в диапазоне от 2 до 9.
list_kr2 = []
list_kr3 = []
list_kr4 = []
list_kr5 = []
list_kr6 = []
list_kr7 = []
list_kr8 = []
list_kr9 = []
min_ch = 2
max_ch = 99
ost_d = 0
while True:
    if min_ch > max_ch:
        break
    if min_ch % 2 == ost_d:
        list_kr2.append(min_ch)
    if min_ch % 3 == ost_d:
        list_kr3.append(min_ch)
    if min_ch % 4 == ost_d:
        list_kr4.append(min_ch)
    if min_ch % 5 == ost_d:
        list_kr5.append(min_ch)
    if min_ch % 6 == ost_d:
        list_kr6.append(min_ch)
    if min_ch % 7 == ost_d:
        list_kr7.append(min_ch)
    if min_ch % 8 == ost_d:
        list_kr8.append(min_ch)
    if min_ch % 9 == ost_d:
        list_kr9.append(min_ch)
    min_ch += 1

print (list_kr2)
print ('На 2 делится ', len(list_kr2), 'чисел')
print()
print (list_kr3)
print ('На 3 делится ', len(list_kr3), 'числа')
print()
print (list_kr4)
print ('На 4 делится ', len(list_kr4), 'числа')
print()
print (list_kr5)
print ('На 5 делится ', len(list_kr5), 'чисел')
print()
print (list_kr6)
print ('На 6 делится ', len(list_kr6), 'чисел')
print()
print (list_kr7)
print ('На 7 делится ', len(list_kr7), 'чисел')
print()
print (list_kr8)
print ('На 8 делится ', len(list_kr8), 'чисел')
print()
print (list_kr9)
print ('На 9 делится ', len(list_kr9), 'чисел')
print()
