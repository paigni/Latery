def inp_check(name_func):
    """Проверка ввода числового значения"""
    if name_func.isdigit() == True:
        return name_func
    if name_func.isdigit() == False:
        return False


def check_range(min,max,user_input):
    """Проверка выбора категорий, если пользователь ввёл значение не из номера категории, предлагается ввести заново"""
    if user_input > max or min > user_input:
        return False
    if min <= user_input <= max:
        return user_input
