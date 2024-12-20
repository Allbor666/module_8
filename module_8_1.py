def add_everything_up(a, b):
    # Проверяем, являются ли оба аргумента числами
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return round(a + b, 3)  # Округляем результат до 3 знаков после запятой
    else:
        # Если типы разные, соединяем их в строку
        return str(a) + str(b)

# Примеры вызовов функции
print(add_everything_up(123.456, 'строка'))  # Ожидаемый вывод: '123.456строка'
print(add_everything_up('яблоко', 4215))      # Ожидаемый вывод: 'яблоко4215'
print(add_everything_up(123.456, 7))           # Ожидаемый вывод: 130.456        