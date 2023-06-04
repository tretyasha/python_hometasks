# напишите программу,которая принимает на вход вещественное число и показывает сумму его цифр

# 123 -->6
# 1.23 -->6

digit = input("enter number")
print(digit)
digit = digit.replace(",", "")
digit = digit.replace(",", "")
print(digit)
result_1 = sum(map(lambda x: int(x), digit))


print(result_1)
