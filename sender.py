import datetime
import time
import sys
import schedule
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Скоро понадобится загрузить библиотеки
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# Введите ваш Twilio Account SID и Auth Token
account_sid = 'AC86747cceed0e4a385263f0a615b31157'
auth_token = '136be5a15dc8611b0122a8851453f473'
# Путь к драйверу браузера Chrome
# chromedriver_path = 'chromedriver.exe'
#
# # Открываем браузер и переходим на страницу WhatsApp Web
# driver = webdriver.Chrome(chromedriver_path)
# driver.get("https://web.whatsapp.com/")

# Введите номер отправителя и список номеров получателей
from_number = '+16204459618'  # Ваш Twilio номер телефона
to_numbers = ["+996771478853", "+996556500169"]
name_first = to_numbers[0] = 'Артур Дуйшеев'
name_d = to_numbers[1] = 'Алмаз'
# Список номров получателей

# Список дат для отправки сообщений
dates = ["2023-04-22", "2023-06-15", "2023-08-21"]


# Функция отправки SMS-сообщения
def send_message(message, to_number):
    # относится к вцап
    # input("Please scan the QR code and press Enter to continue...")
    client = Client(account_sid, auth_token)
    try:
        client.messages.create(
            body=message,
            from_=from_number,
            to=to_number,
        )
        if to_number == '+996771478853':
            print(message, "вы поздравили человека под именем {}".format(name_first))
        elif to_number == '+996556500169':
            print(message, "вы поздравили человека под именем {}".format(name_d))
    except TwilioRestException:
        print("Произошла ошибка при отправке сообщения")


# Функция планирования отправки SMS-сообщения
def schedule_message():
    message = 'С днем рождения!'
    time.sleep(5)

    for date in dates:
        for to_number in to_numbers:
            send_time = datetime.datetime.strptime(date + ' 9:00:00', '%Y-%m-%d %H:%M:%S')
            schedule.every().day.at(send_time.strftime('%H:%M:%S')).do(send_message, message, to_number)


if __name__ == '__main__':
    # Планируем отправку SMS-сообщений
    schedule_message()

    # Бесконечный цикл, чтобы программа продолжала работать
    while True:
        try:
            print("ищу иммениника...")
            time.sleep(3)
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Программа завершена")
            sys.exit()
        except Exception as e:
            print("Произошла непредвиденная ошибка, мы ее решим в скором времени", e)
            continue
