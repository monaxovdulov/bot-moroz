import requests
from settings import TOKEN
import time
import random

URL = 'https://api.telegram.org/bot'

replics = ["привет", "как дела?", "кто ты?", "с новым годом", "с новым годом!"]
answers = [
    ['привет', 'ЗДАРОВА', 'ХАЙ'],
    ["НОРМ", "ХОРОШО", "КУЛ"],
    ["ты", "я робот, как и ты ", "Павел Дуров"],
    ["C новым годом", "ПОЗДРАВЛЯЮ ТЕБЯ"],
    ["С новым счастьем!"]
]


def send_message(text, chat_id):
    requests.get(f"{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}")

def get_updates(offset=0):
    result = requests.get(f'{URL}{TOKEN}/getUpdates?offset={offset}').json()
    return result['result']


update_id = get_updates()[-1]['update_id']  # Присваиваем ID последнего отправленного сообщения боту
while True:
    time.sleep(2)
    messages = get_updates(update_id)  # Получаем обновления
    for message in messages:
        # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
        if update_id < message['update_id']:
            update_id = message['update_id']  # Присваиваем ID последнего отправленного сообщения боту

            chat_id_current_message = message['message']['chat']['id']
            message_user = message['message']['text'].lower()
            if message_user in replics:
                random_answer = random.choice(answers[replics.index(message_user)])
                send_message(random_answer, chat_id_current_message)
            else:
                send_message("Я вас понял, но сказать мне нечего", chat_id_current_message)
            print(f"ID пользователя: {message['message']['chat']['id']}, Сообщение: {message['message']['text']}")



