import telebot
import copy
import pyowm

bot = telebot.TeleBot("1317940392:AAE87iwHH3PmezComeLN-gFx0epjZ2izqxQ", parse_mode=None)
owm = pyowm.OWM('a99967bc9ee70d5b4bd387902982f400', language = "RU")

def send__image():
    if 'облачно' in weather_info or 'пасмурно' in weather_info: 
        photo = open('img/photo1.webp', 'rb')
        bot.send_photo(message_id, photo)

    if 'ясно' in weather_info:
        photo = open('img/photo3.jpg', 'rb')
        bot.send_photo(message_id, photo)

    if 'дождь' in weather_info:
        photo = open('img/photo2.png', 'rb')
        bot.send_photo(message_id, photo)
    
    if 'туман' in weather_info:
        photo = open('img/photo5.jpg', 'rb')
        bot.send_photo(message_id, photo)

    if 'снег' in weather_info:
        photo = open('img/photo6.jpg', 'rb')
        bot.send_photo(message_id, photo)

    


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте " + message.from_user.first_name + '.  Бот для узнавания погоды готов работать. Укажите город, чтоб знать погоду в этой месности...')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global message_id
    global message_id
    global message1
    global weather_info
    print(message.from_user.first_name, message.text)

    message1 = copy.copy(message.text)
    message_id = copy.copy(message.chat.id)

    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')['temp']

        bot.send_message(message.from_user.id, "В местности " + message.text + " сейчас температура: " + str(temperature) + " по Цельсию.")
        bot.send_message(message.from_user.id,'Погода в указаном местности: ' + w.get_detailed_status())
        bot.send_message(message.from_user.id, 'Скорость ветра равна: ' + str(w.get_wind()['speed']) + ' м/с')

        weather_info = copy.copy(w.get_detailed_status())

        send__image()

        
    except:
        bot.send_message(message.from_user.id, "По вашему запросу ничего не найдено")

bot.polling()
    