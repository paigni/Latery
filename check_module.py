from fuzzywuzzy import fuzz as fuzzy


def inp_check(min_count, max_count, name_func):
    """Проверка ввода числового значения и заданного диапазона"""
    if name_func.isdigit():
        name_func = int(name_func)
        if min_count <= name_func <= max_count:
            return True
        return False


def check_answer(answ, play_answ):
    if fuzzy.ratio(answ, play_answ) > 75:
        return True
    return False
