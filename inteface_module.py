from check_module import inp_check, check_categories, check_players_count


def category_choice(cat):
    """Функция выводит список категорий и запрашивает ответ от пользователя"""
    for category, val in enumerate(cat.values(), 1):
        print(f'{category}:{val}')

    change_category = input(f"Выберите категорию из списка выше"'\n')
    check_user_input = inp_check(change_category)
    change_category_check_to_is_int = int(check_user_input)
    change_category_check = check_categories(change_category_check_to_is_int)
    return cat[change_category_check]


def number_of_players():
    """Функция запрашивает количество игроков, возвращает ввод от пользователя"""
    players_count = input(f"Введите количество игроков"'\n')
    players_count_check = check_players_count(int(inp_check(players_count)))
    return players_count_check


def player_name(number):
    """Принимает количество игроков в качестве аргумента, возвращая список игроков"""
    players_name = []
    for count in range(0, number):
        players_name.append('player' + f'{count}')
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