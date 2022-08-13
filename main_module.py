from service_module import web_response, question_values, categories
from inteface_module import player_name, number_of_players, category_choice, question_choice
from check_module import check_answer

def game():
    """Основная функция, в которой происходит процесс игры, на выходе возвращает словарь типа игрок-очки
    (ещё не дописана)"""
    cat = category_choice(categories)
    num = number_of_players()
    questions_and_answers = web_response(cat, num)
    play = player_name(num)
    it_count = 0
    pl_count = 0
    while not questions_and_answers == []:
        play_copy = play.copy()
        max_ques = len(questions_and_answers)
        print(questions_and_answers)
        if max_ques > 1:
            for value in questions_and_answers:
                dif = value.get('difficulty')
                category = value.get('category')
                dif_value = question_values.get(dif)
                print(f'{category}:{dif_value}')

        quesstion_choice = question_choice(max_ques)
        questions = questions_and_answers[quesstion_choice - 1].get('question')
        dif = questions_and_answers[quesstion_choice - 1].get('difficulty')
        dif_value = question_values.get(dif)
        answers = questions_and_answers[quesstion_choice - 1].get('correctAnswer')

        players_answer = 'e'
        del questions_and_answers[quesstion_choice - 1]
        count = it_count
        current_player = play[count]
        player_names = list(current_player.keys())
        player_names = player_names[0]

        while not check_answer(answers, players_answer) or play_copy == []:
            players_answer = input(
                f"{player_names} Ответьте пожалуйста на вопрос:"'\n'
                f"{questions}"
            )
            play_copy.remove(current_player)
            if check_answer(answers, players_answer):
                print(
                    f"игроку {player_names} начисляется {dif_value} очков"
                )
                current_player[player_names] += dif_value
                break
            if not play_copy:
                print(f'Никто не ответил на вопрос,правильный ответ {answers}')
                break
            current_player = play_copy[0]
            player_names = list(current_player.keys())
            player_names = player_names[0]
        it_count += 1

    for points in play:
        players_point = points[f'player{pl_count}']
        print(f'У игрока player{pl_count} - {players_point}  очков')
        pl_count += 1



game()
