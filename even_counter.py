numbers = input("Введите числа через пробел: ")
even_numbers = [int(n) for n in numbers.split() if int(n) % 2 == 0]

print(f"Чётные числа: {even_numbers}")
print(f"Количество чётных чисел: {len(even_numbers)}")
