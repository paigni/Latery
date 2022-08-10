import requests

question_values = {'easy': 200, 'medium': 400, 'hard': 600}
categories = {
    1: 'film_and_tv',
    2: 'food_and_drink',
    3: 'geography',
    4: 'history',
    5: 'music',
    6: 'general_knowledge'
}

min_cat = 1
max_cat = 6
min_play = 2
max_play = 10

def web_response(cat, players):
    res = requests.get(
        f"https://the-trivia-api.com/api/"
        f"questions?categories={cat}"
        f"&limit={players}"
    )
    rest = res.json()
    print(rest)  # del
    return rest
