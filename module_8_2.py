def personal_sum(numbers):
    result = 0  # Переменная для хранения суммы
    incorrect_data = 0  # Счетчик некорректных данных

    # Перебор элементов в коллекции numbers
    for number in numbers:
        try:
            result += float(number)  # Пытаемся добавить число к результату
        except (ValueError, TypeError):
            print(f'Некорректный тип данных для подсчёта суммы - {number}')  # Сообщение об ошибке
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных при ошибке

    return result, incorrect_data  # Возвращаем кортеж с результатом и счетчиком


def calculate_average(numbers):
    # Проверяем, является ли numbers корректной коллекцией (типы: list, tuple или set)
    if not isinstance(numbers, (list, tuple, set)):
        print('В numbers записан некорректный тип данных')
        return None

    # Получаем сумму и количество некорректных данных
    total_sum, incorrect_data = personal_sum(numbers)

    valid_data_count = len(numbers) - incorrect_data  # Количество корректных данных

    # Проверяем деление на ноль
    try:
        average = total_sum / valid_data_count  # Вычисляем среднее арифметическое
    except ZeroDivisionError:
        return 0  # Если нет корректных данных, возвращаем 0

    return average  # Возвращаем среднее арифметическое


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # некорректный тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа
print(f'Результат 3: {calculate_average(567)}')  # не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Все должны работать


