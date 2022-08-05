import requests
from fuzzywuzzy import fuzz as fuzzy
from check_module import inp_check, check_categories
from service_module import question_values,categories

def category_choice():
    """Функция выводит список категорий и запрашивает ответ от пользователя"""
    for category,val in enumerate(categories.values(),1):
        print(f'{category}:{val}')

    change_category = input(f"Выберите категорию из списка выше"'\n')
    change_category_check_to_is_int = int(inp_check(change_category))
    change_category_check = check_categories(change_category_check_to_is_int)

    return categories[change_category_check]
cat = category_choice()

def number_of_players():
    """Функция запрашивает количество игроков,возвращает ввод от пользователя"""
    players_count = input(f"Введите количество игроков"'\n')
    players_count_check = int(inp_check(players_count))
    return players_count_check
num = number_of_players()

def player_name():
    players_name = []
    for count in range(0, num):
        players_name.append('player' + f'{count}')
    return players_name
play = player_name()

def players_score():
    count = 0
    players_score = {}
    for b in range(num):
        k = play[count]
        count +=1
        players_score[k] = 0
    return players_score
score = players_score()

def web_response():
    res = requests.get(
                           f"https://the-trivia-api.com/api/"
                           f"questions?categories={cat}"
                           f"&limit={num}"
                           )
    rest = res.json()
    print(rest) # del
    return rest
web = web_response()

def game():
    score = players_score()
    for question in web:
        for value in web:
            dif = value.get('difficulty')
            category = value.get('category')
            dif_value = question_values.get(dif)
            print (f'{category}:{dif_value}')
        user_input = input("Выберите номер вопроса")
        user_input_check = int(inp_check(user_input))
        questions = web[user_input_check - 1].get('question')
        dif = web[user_input_check - 1].get('difficulty')
        dif_value = question_values.get(dif)
        answers = web[user_input_check - 1].get('correctAnswer')
        print(dif_value, type(dif_value))
        count = 0
        players_answer = input(
            f"{play[count]} Ответьте пожалуйста на вопрос:"'\n'
            f"{questions}"
        )
        del web[user_input_check - 1]
        count=0


        if fuzzy.ratio(answers,players_answer)>75:
            print(f"игроку {play[count]} начисляется {dif_value} очков")
            score[play[count]] = dif_value
        else:
            while fuzzy.ratio(answers,players_answer) < 75 or count>= num-1:
                count += 1
                repeat_question = input(
                        f"Ход передаётся {play[count]} Ответьте пожалуйста на вопрос:"'\n'
                        f"{questions}")
                if fuzzy.ratio(answers, repeat_question) > 75:
                    print(
                            f"игроку {play[count]} начисляется {dif_value} очков")
                    score[play[count]] = dif_value
                    break
                if count>= num-1:
                    print('Никто не ответил на вопрос')
                    break




game()