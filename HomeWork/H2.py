# Задача 1
# n = int(input("Введите количество арбузов:" ))
# n1 = int(input("Введите массу арбуза:" ))
# n2 = int(input("Введите массу арбуза:" ))
# maxA = 0
# minA = 0
# a = 0
# if n1 > n2:
#     maxA = n1
#     minA = n2
# else:
#     maxA = n2
#     minA = n1
# for i in range(n - 2):
#     a = int(input("Введите массу арбуза:" ))
#     if a > maxA:
#         maxA = a
#     elif a < minA:    
#         minA = a
# print(f"Арубз для себя: {maxA}кг, арбуз для тещи: {minA}кг")

# Задача 2
# n = int(input("Введите число монет: "))
# orel = int(input("Введите число монет, лежащих орлом ввех: "))
# while n < orel:
#     orel = int(input("Введите число монет, лежащих орлом ввех: "))
# resh = n - orel
# if orel > resh:
#     print(resh)
# else: print(orel)

# Задача3

# s = int(input("Введите сумму чисело x и y: "))
# p = int(input("Введите произведение чисел x и y: "))
# num1 = 0
# num2 = 0
# for i in range(1,1001):
#     if s - i == p / i:
#         num1 = i
#         break
# num2 = s - num1
# print(num1, num2)

# Задача 4

n = int(input("Введите N: "))
current = 0
i = 0
while n > current:
    print(i)
    i += 1
    current = 2 ** i
   







