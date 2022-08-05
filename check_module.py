def inp_check(name_func):
    if name_func.isdigit() == True:
        return name_func
    while name_func.isdigit() == False:
        repeat = input('Неверный ввод,повторите попытку'"\n")
        if repeat.isdigit() == True:
            return repeat
        if repeat.isdigit() == False:
            continue

def check_categories(number_of_category):
    while number_of_category > 6 or number_of_category<1:
        repeat = input('Вы выбрали пока недоступный номер категории,повторите ввод'"\n")
        check_repeat = int(inp_check(repeat))
        if 1<check_repeat <7:
            return check_repeat
        if check_repeat >6 :
            continue
        if check_repeat<1:
            continue
    if number_of_category>= 1 and number_of_category <= 6:
        return number_of_category

def check_players_count(players_count):
    while players_count > 10 or players_count < 1:
        repeat = input('Вы выбрали пока недоступный номер категории,повторите ввод'"\n")
        check_repeat = int(inp_check(repeat))
        if 1<check_repeat <10:
            return check_repeat
        if check_repeat >10 :
            continue
        if check_repeat<1:
            continue
    if players_count>= 1 and players_count <= 10:
        return players_count
