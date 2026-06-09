# ЗАДАНИЕ ДЛЯ КОМАНДЫ 2.
# Этот файл является главным файлом игры.
# Здесь нужно соединить все функции из других файлов и сделать игровой цикл.
# Проверь себя: после реализации запусти python main.py.
# Если игра запускается, показывает правила, вопросы и итог, значит файл main.py работает.

# Эта строка подключает стандартный модуль random, чтобы перемешивать вопросы.
import random

# Эта строка подключает файл data.py, где лежат вопросы для игры.
import data

# Эта строка берёт из файла config.py начальное количество жизней.
from config import LIVES

# Эта строка берёт функции правил и итогов из файла rules_results.py.
from rules_results import show_rules, show_results

# Эта строка берёт функции вопроса, ввода и проверки ответа из файла question_answer.py.
from question_answer import show_question, get_choice, process_answer


# Эта функция должна содержать основной игровой цикл.
def game_loop():
    # Шаг 1: скопируй список data.cases в новую переменную через data.cases[:].
    # Шаг 2: перемешай новую переменную с помощью random.shuffle().
    # Шаг 3: запиши количество вопросов в переменную total.
    # Шаг 4: создай переменные lives, score, correct и question_num.
    # Шаг 5: запусти цикл for case in shuffled.
    # Шаг 6: внутри цикла увеличивай question_num на 1.
    # Шаг 7: вызывай show_question(), чтобы показать вопрос.
    # Шаг 8: вызывай get_choice(), чтобы получить ответ игрока.
    # Шаг 9: вызывай process_answer(), чтобы обновить lives, score и correct.
    # Шаг 10: если lives стало 0, выведи сообщение о конце игры и останови цикл через break.
    # Шаг 11: если жизни остались, жди Enter перед следующим вопросом.
    # Шаг 12: верни correct, score, lives, total.
    # Проверка: когда другие функции готовы, запусти python main.py и сыграй несколько ходов.

    cases = data.data[:]
    random.shuffle(cases)

    total = len(cases)
    lives = LIVES
    score = 0
    correct = 0
    question_num = 0
    
    for case in cases:
        question_num += 1
        show_question(question_num, case, total, lives, score)
        player_choice = get_choice()
        lives, score, correct = process_answer(player_choice, case, lives, score, correct)

        if lives == 0:
            print("Игра окончена! У вас закончились жизни.")
            break
        input("Нажмите Enter для следующего вопроса...")
    return correct, score, lives, total

    


# Эта функция должна собрать игру из готовых частей.
def play():
    # Шаг 1: вызови show_rules(), чтобы показать правила.
    # Шаг 2: вызови game_loop() и сохрани четыре результата.
    # Шаг 3: передай эти четыре результата в show_results().
    # Проверка: в этой функции не должно быть сложной логики, только сборка игры из готовых частей.
    
    show_rules()
    correct, score, lives, total = game_loop()
    show_results(correct, score, lives, total)

# Здесь ученик должен включить запуск игры после реализации функций.
# Подсказка: когда все функции готовы, нужно раскомментировать строку ниже.
# Проверка: после раскомментирования команда python main.py должна запускать игру.
# play()


game_loop()