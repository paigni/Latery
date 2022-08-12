def inp_check(min_count,max_count,name_func):
    """Проверка ввода числового значения и заданного диапазона"""
    if name_func.isdigit():
        name_func = int(name_func)
        if name_func > max_count or min_count > name_func:
            return False
        return True