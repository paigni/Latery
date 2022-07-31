import requests
from fuzzywuzzy import fuzz as fuzzy

def interface():

    categories = {1: 'film_and_tv',
                  2: 'food_and_drink',
                  3: 'geography',
                  4: 'history',
                  5: 'music',
                  6: 'general_knowledge'
                  }
    question_values = {'easy':200,'medium':400,'hard':600}

    players_name = []

    for category,val in enumerate(categories.values(),1):
        print(f'{category}:{val}')

    change_category = int(input(f"Выберите категорию из списка выше"'\n'))
    players_count = int(input(f"Введите количество игроков во игроков"'\n'))

    for count in range(0, players_count):
        players_name.append('player' + f'{count}')


    res = requests.get(
                           f"https://the-trivia-api.com/api/"
                           f"questions?categories={categories[change_category]}"
                           f"&limit={players_count}"
                           )
    rest = res.json()
    print(rest) # del

    for question in rest:
        for value in rest:
            dif = value.get('difficulty')
            category = value.get('category')
            dif_value = question_values.get(dif)
            print (f'{category}:{dif_value}')

        user_input= int(input("Выберите номер вопроса"))
        questions = rest[user_input-1].get('question')
        dif = rest[user_input-1].get('difficulty')
        dif_value = question_values.get(dif)
        answers = rest[user_input-1].get('correctAnswer')
        print(dif_value,type(dif_value))
        count = 0
        players_answer = input(
                            f"{players_name[count]} Ответьте пожалуйста на вопрос:"'\n'
                            f"{questions}"
                            )
        del rest[user_input]
        if fuzzy.ratio(answers,players_answer)>75:
            players_name_point = {players_name[count]:dif_value}
            print(f"игроку {players_name[count]} начисляется {dif_value} очков")
        else:
            while fuzzy.ratio(answers,players_answer) > 75:
                count += 1
                repeat_question = input(
                    f"Ход передаётся {players_name[count]} Ответьте пожалуйста на вопрос:"'\n'
                    f"{questions}")
                if fuzzy.ratio(answers, repeat_question) > 75:
                    players_name_point = {players_name[count]: dif_value}
                    print(
                        f"игроку {players_name[count]} начисляется {dif_value} очков")
                    break
                else:
                    continue




a = interface()


