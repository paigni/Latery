def inp_check(name_func):
    """Проверка ввода числового значения"""
    if name_func.isdigit():
        return name_func
    while not name_func.isdigit():
        repeat = input('Неверный ввод,повторите попытку'"\n")
        if repeat.isdigit():
            return repeat


def check_categories(number_of_category):
    """Проверка выбора категорий, если пользователь ввёл значение не из номера категории, предлагается ввести заново"""
    while number_of_category > 6 or number_of_category < 1:
        repeat = input('Вы выбрали пока недоступный номер категории,повторите ввод'"\n")
        check_repeat = int(inp_check(repeat))
        if 1 < check_repeat < 7:
            return check_repeat
    if 1 <= number_of_category <= 6:
        return number_of_category


def check_players_count(players_count):
    """Функция проверяет находится ли число в заданном диапазоне, если нет, возвращает ввод"""
    while players_count > 10 or players_count < 1:
        repeat = input('Количество игроков не может быть больше 10'"\n")
        check_repeat = int(inp_check(repeat))
        if 1 <= check_repeat <= 10:
            return check_repeat
        else:
            continue
    if 1 <= players_count <= 10:
        return players_count
