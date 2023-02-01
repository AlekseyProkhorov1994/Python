# Задача 1

# num = int(input("Введите трехначное число: " ))
# sumDig = 0
# while num < 99 or num > 999:
#     num = int(input("Неверное число, введите трехзначное число: " ))
# while num > 0:
#     sumDig = sumDig + num % 10
#     num //= 10
# print(f"Сумма цыфр равно {sumDig}")

# Задача 2 

# s = int(input("Введите количество журавликов: " ))
# if s % 6 == 0:
#     pet = s // 6
#     ser = pet
#     kat = (pet + ser) * 2
#     print(pet, kat, ser)
# else: print("Некорректные данные")

# Задача 3 

# numTiket = int(input("Введите номер билета: " ))
# while numTiket < 99999 or numTiket > 999999:
#     numTiket = int(input("Некорректный номер билета,введите номер билета: " ))
# firstNum = numTiket // 1000
# secondNum = numTiket % 1000
# sum1 = 0
# sum2 = 0
# while firstNum > 0:
#     sum1 = sum1 + firstNum % 10
#     firstNum //= 10
#     sum2 = sum2 + secondNum % 10
#     secondNum //= 10
# if sum1 == sum2:
#     print("Yes")
# else: print("No")

# Задача 4

n = int(input("Введите высоту шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите количество долек, которые хотети отломить "))
if k < m and k < n:
    print("No")
elif k % n == 0 or k % m == 0:
    print("Yes")
else: print("No")
