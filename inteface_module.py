from check_module import inp_check, check_range
from service_module import max_cat,min_cat,max_play,min_play


def category_choice(cat):
    """Функция выводит список категорий и запрашивает ответ от пользователя"""
    for category, val in enumerate(cat.values(), 1):
        print(f'{category}:{val}')
    change_category = input(f"Выберите категорию из списка выше"'\n')
    check_user_input = inp_check(change_category)
    check_user_input = int(check_user_input)
    change_category_check = check_range(min_cat,max_cat,check_user_input)
    if check_user_input == True and change_category_check == True:
        return cat[change_category_check]
    while check_user_input == False or change_category_check == False:
        repeat_user_input = input(f"Повторите ввод,категория указывается в цифрах и не может быть больше"
                                  f" {max_cat} и меньше {min_cat}" '\n')
        check_repeat = inp_check(repeat_user_input)
        if check_repeat != False:
            repeat_user_input = int(check_repeat)
            change_category_check = check_range(min_cat,max_cat,repeat_user_input)
            if change_category_check != False:
                return cat[change_category_check]


def number_of_players():
    """Функция запрашивает количество игроков, возвращает ввод от пользователя"""
    players_count = input(f"Введите количество игроков"'\n')
    players_count_check = inp_check(players_count)
    players_count_check = int(players_count_check)
    check_input_range = check_range(min_play, max_play, players_count_check)
    if players_count_check != False and check_input_range != False:
        return players_count_check
    while players_count_check == False or check_input_range == False:
        repeat_user_input = input(f"Повторите ввод,количество игроков указывается в цифрах и не может быть больше"
                                  f" {max_play} и меньше {min_play}" '\n')
        check_repeat = inp_check(repeat_user_input)
        if check_repeat != False:
            repeat_user_input = int(check_repeat)
            change_category_check = check_range(min_play, max_play, repeat_user_input)
            if change_category_check != False:
                return repeat_user_input


def player_name(number):
    """Принимает количество игроков в качестве аргумента, возвращая список игроков"""
    players_name = []
    for count in range(0, number):
        players_score = 0
        players_name.append({f'player{count}':players_score})
    print(players_name)
    return players_name
