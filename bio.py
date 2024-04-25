import telebot
from telebot import types
import time
from googletrans import Translator
from config import TOKEN

translator = Translator()


bot = telebot.TeleBot(TOKEN)

src = 'en'
dest = 'ru'


@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, "Выберите команду:")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_creator = types.KeyboardButton('👨‍💻 Мое творчество')
    item_creator_bio = types.KeyboardButton('👤 Краткая информация о создателе:')
    item_github = types.KeyboardButton('🌐 Инстаграм')
    item_contact = types.KeyboardButton('📞 Мои контакты')
    item_translator = types.KeyboardButton('Переводчик 📄')
    markup.add(item_creator, item_creator_bio, item_github, item_contact, item_translator)

    bot.send_message(message.chat.id, 'Привет! Я бот. Нажмите на одну из кнопок, чтобы узнать больше.',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '👨‍💻 Мое творчество')
def creation(message):
    creation_info = ("Всем привет, короче говоря, я Султан, "
                     "думаю вы все меня знаете, а если нет, то нажмите на кнопку 'Краткая информация', "
                     "и узнаете об о мне. "
                     "\nЯ создавал этот бот потом и кровью, дечилем"
                     "\nНажми на '👤 Краткая информация о создателе:', чтобы узнать больше обо мне")
    bot.reply_to(message, creation_info)


@bot.message_handler(func=lambda message: message.text == '👤 Краткая информация о создателе:')
def creator_bio(message):
    creator_info = ("Меня зовут Султан, мне стукнет 24 скоро, короче, старость не в радость. Я не знаю "
                    "что рассказывать о себе, лучше расскажу что может сделать этот бот, он может стать переводчиком. "
                    "И рассказать немножко об о мне. А так я работал над этим ботом немало, так что буду рад услышать "
                    "ваши отзывы, а так ваще, из за того что у "
                    "меня было мало времени, я не успел добавить больше функционала")

    photo_path = '/home/acer/Downloads/msg930865454-232075.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=creator_info)


@bot.message_handler(func=lambda message: message.text == '🌐 Инстаграм')
def send_link(message):
    my_instagram = ("[Ссылка на Instagram](https://www.instagram.com/su1a.18/)\n Для связи со мной используйте "
                    "ссылку")
    caption = "[Ссылка на Instagram](https://www.instagram.com/su1a.18/)\nДля связи со мной используйте ссылку."
    photo_path = '/home/acer/Downloads/msg906622093-232486.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption, parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '📞 Мои контакты')
def contacts(message):
    bot.send_message(message.chat.id,
                     "Свяжитесь со мной при помощи: +996508018..",
                     parse_mode="Markdown")
    time.sleep(2)
    bot.send_message(message.chat.id, "Не пишите мне...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Шутка")
    time.sleep(2)
    bot.send_message(message.chat.id, "Пишите, разрешаю!")


@bot.message_handler(func=lambda m: True)
def translate_message(message):
    detected_lang = translator.detect(message.text).lang

    if detected_lang == 'ru':
        translated_text = translator.translate(message.text, dest='en', src='ru').text
    else:
        translated_text = translator.translate(message.text, dest='ru', src='en').text

    bot.send_message(message.chat.id, translated_text)


bot.polling()
