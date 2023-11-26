import random
import logging
from datetime import datetime

logging.basicConfig(filename='game_log.log', level=logging.DEBUG)

def logger(log_data):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - {log_data}"
    logging.debug(log_message)

def validate_input(input_str, input_type):
    while True:
        try:
            user_input = input(input_str)
            user_input = input_type(user_input)
            return user_input
        except ValueError:
            print("Неверный формат данных. Попробуйте еще раз.")

def generate_number(N):
    number = random.randint(1, N)
    logger(f"Сгенерировано загаданное число: {number}")
    return number

def check_guess(number, guess):
    logger(f"Пользователь ввел число: {guess}")
    if guess == number:
        return True
    elif guess < number:
        print("Загаданное число больше.")
        logger("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
        logger("Загаданное число меньше.")
    return False

def game():
    logger("--- Старт игры ---")
    N = validate_input("Введите верхнюю границу диапазона (N): ", int)
    k = validate_input("Введите количество попыток (k): ", int)
    number = generate_number(N)
    logger(f"Верхняя граница диапазона: {N}. Количество попыток: {k}")
    
    for i in range(k):
        guess = validate_input("Введите вашу попытку: ", int)
        if check_guess(number, guess):
            print("Вы угадали!")
            logger("Вы угадали!")
            break
    else:
        print("Попытки закончились.")
        logger("Попытки закончились.")

    print(f"Загаданное число: {number}")
    logger(f"Загаданное число: {number}")
    logger("--- Конец игры ---")

game()
