def inp_check(name_func):
    """Проверка ввода числового значения"""
    if name_func.isdigit():
        return True
    if not name_func.isdigit():
        return False


def check_range(min,max,user_input):
    """Проверка выбора категорий, если пользователь ввёл значение не из номера категории, предлагается ввести заново"""
    if user_input > max or min < user_input:
        return False
    if min <= user_input <= max:
        return True
