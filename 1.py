# вводится список целых чисел в одну строчку через пробел.необходимо оставить в нем только двузначные числа.
# реализовать программу с использванием функции filter.
# результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел

list_1 = list(map(int, input("enter your list devided by space").split()))

print(list_1)

result_list_1 = list(filter(lambda x: 9 < abs(x) < 100, list_1))

print(result_list_1)
