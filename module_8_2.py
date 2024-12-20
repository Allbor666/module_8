def personal_sum(numbers):
    result = 0  # Переменная для хранения суммы
    incorrect_data = 0  # Счетчик некорректных данных

    # Перебор элементов в коллекции numbers
    for number in numbers:
        try:
            result += number  # Пытаемся добавить число к результату
        except TypeError:
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных при ошибке

    return result, incorrect_data  # Возвращаем кортеж с результатом и счетчиком


def calculate_average(numbers):
    # Проверяем, является ли numbers коллекцией (типа list, tuple или set)
    if not isinstance(numbers, (list, tuple, set)):
        print('В numbers записан некорректный тип данных')
        return None

    # Получаем сумму и количество некорректных данных
    total_sum, incorrect_data = personal_sum(numbers)

    valid_data_count = len(numbers) - incorrect_data  # Количество корректных данных

    try:
        # Вычисляем среднее арифметическое
        average = total_sum / valid_data_count
        return average
    except ZeroDivisionError:  # Обработка случаев деления на 0
        return 0

# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Ожидаемый вывод: сообщение о некорректном типе
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Ожидаемый вывод: 2.0 (среднее между 1 и 3)
print(f'Результат 3: {calculate_average(567)}')  # Ожидаемый вывод: сообщение о некорректном типе
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Ожидаемый вывод: 26.5 (среднее арифметическое)
