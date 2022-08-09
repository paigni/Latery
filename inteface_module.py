from check_module import inp_check, check_range


def category_choice(cat):
    """Функция выводит список категорий и запрашивает ответ от пользователя"""
    for category, val in enumerate(cat.values(), 1):
        print(f'{category}:{val}')
    max_cat = 6
    min_cat = 1
    change_category = input(f"Выберите категорию из списка выше"'\n')
    check_user_input = inp_check(change_category)
    if check_user_input == True:
        change_category_check_to_is_int = int(check_user_input)
        change_category_check = check_range(min_cat,max_cat,change_category_check_to_is_int)
        return cat[change_category_check]
    if check_user_input == False:
        repeat = input("Повтторите ввод")
        change_category_check_to_is_int = int(repeat)
        change_category_check = check_range(min_cat,max_cat,change_category_check_to_is_int)
        return cat[change_category_check]


def number_of_players():
    """Функция запрашивает количество игроков, возвращает ввод от пользователя"""
    min_play = 2
    max_play = 10
    players_count = input(f"Введите количество игроков"'\n')
    players_count_check = inp_check(players_count)
    if players_count_check == True:
        players_count_check_1 = int(players_count_check)
        change_category_check = check_range(min_play,max_play,players_count_check_1)
        return players_count


    return players_count_check


def player_name(number):
    """Принимает количество игроков в качестве аргумента, возвращая список игроков"""
    players_name = []
    for count in range(0, number):
        players_name.append(f'player{count}')
    return players_name


def players_score(pla, num):
    """Принимает список игроков и их количество как аргументы, возвращая словарь с названием игроков
    по стандарту делая количество очков равным 0"""
    count = 0
    players_score = {}
    for b in range(num):
        k = pla[count]
        count += 1
        players_score[k] = 0
    return players_score