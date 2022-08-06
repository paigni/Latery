from fuzzywuzzy import fuzz as fuzzy
from service_module1 import web_response, question_values, categories
from check_module import inp_check
from inteface_module import player_name, number_of_players, players_score, category_choice


def game():
    """Основная функция, в которой происходит процесс игры, на выходе возвращает словарь типа игрок-очки
    (ещё не дописана)"""
    cat = category_choice(categories)
    num = number_of_players()
    play = player_name(num)
    score = players_score(play, num)
    web = web_response(cat, num)
    for question in web:
        for value in web:
            dif = value.get('difficulty')
            category = value.get('category')
            dif_value = question_values.get(dif)
            print(f'{category}:{dif_value}')
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
        count = 0

        if fuzzy.ratio(answers, players_answer) > 75:
            print(f"игроку {play[count]} начисляется {dif_value} очков")
            score[play[count]] = dif_value
        else:
            while fuzzy.ratio(answers, players_answer) < 75 or count >= num - 1:
                count += 1
                repeat_question = input(
                    f"Ход передаётся {play[count]} Ответьте пожалуйста на вопрос:"'\n'
                    f"{questions}")
                if fuzzy.ratio(answers, repeat_question) > 75:
                    print(
                        f"игроку {play[count]} начисляется {dif_value} очков")
                    score[play[count]] = dif_value
                    break
                if count >= num - 1:
                    print(f'Никто не ответил на вопрос,правильный ответ {answers}')
                    break


game()
