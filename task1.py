# Запрос числа у пользователя
number = int(input("Введите целое число: "))

# Определение четности
if number % 2 == 0:
    # Четное
    print(f"Число {number} является четным.")
else:
    # Нечетное
    print(f"Число {number} является нечетным.")