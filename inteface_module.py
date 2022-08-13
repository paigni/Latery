from check_module import inp_check
from service_module import max_cat, min_cat, max_play, min_play


def category_choice(cat):
    """Функция выводит список категорий и запрашивает ответ от пользователя"""
    for category, val in enumerate(cat.values(), 1):
        print(f'{category}:{val}')
    change_category = 'ds'

    while not inp_check(min_cat, max_cat, change_category):
        change_category = input(f"Выберите категорию из списка выше,категория вводится числом,которое не может быть "
                                f"больше {max_cat} и меньше {min_cat}"'\n')
        if inp_check(min_cat, max_cat, change_category):
            change_category_int = int(change_category)
            return cat[change_category_int]
        else:
            print("Неверный ввод,повторите попытку")


def number_of_players():
    """Функция запрашивает количество игроков, возвращает ввод от пользователя"""
    players_count = 'b'
    while not inp_check(min_play, max_play, players_count):
        players_count = input(f"Введите количество игроков,количество вводится числом,которое не может быть "
                              f"больше {max_play} и меньше {min_play}"'\n')
        if inp_check(min_play, max_play, players_count):
            int_players_count = int(players_count)
            return int_players_count
        else:
            print("Неверный ввод,повторите попытку")


def player_name(number):
    """Принимает количество игроков в качестве аргумента, возвращая список игроков"""
    players_name = []
    for count in range(0, number):
        players_score = 0
        players_name.append({f'player{count}': players_score})
    print(players_name)
    return players_name


def question_choice(max_ques):
    user_input = 'c'
    while not inp_check(1, max_ques, user_input):
        user_input = input(f"Введите номер вопроса,номер вводится числом,которое не может быть "
                           f"больше {max_ques} и меньше 1"'\n')
        if inp_check(1, max_ques, user_input):
            int_user_input = int(user_input)
            return int_user_input
        else:
            print("Неверный ввод,повторите попытку")
