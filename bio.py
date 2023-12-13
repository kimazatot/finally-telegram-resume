import telebot

TOKEN = '6891129145:AAF-iw2W_EsDlajLTLPwq1EPMyu1J1h1WGQ'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['menu'])
def menu(update, message):
    bot.send_message(message.chat.id, "Выберите команду:")


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот. Напишите /creator, чтобы узнать обо мне.')


@bot.message_handler(commands=['creator'])
def creator(message):
    create_info = "Меня создал человек, который любит программирование и технологии. " \
                   "Я был создан для поиска некоторой информации." \
                   "\nНапиши /creator_bio, чтобы узнать больше о моем создателе"
    bot.reply_to(message, create_info)


@bot.message_handler(commands=['creator_bio'])
def creator_bio(message):
    creator_info = "Всем привет! Меня зовут Адинай, мне 17 и я молодой разработчик, но профессионал в своем деле!" \
        "\nЕсть парочка недоделанных проектов, один из них сайт, другой, прототип тг бота, во время карантина, для онлайн-заказов, вам стоит взглянуть /github"

    photo_path = '/home/acer/Downloads/ade.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=creator_info)


@bot.message_handler(commands=['github'])
def send_link(message):
    bot.send_message(message.chat.id, "[Ссылка на GitHub](https://github.com/kimazatot)\n Для связи со мной используйте команду /contact", parse_mode="Markdown")


@bot.message_handler(commands=['contact'])
def contacts(message):
    bot.send_message(message.chat.id, "Свяжитесь со мной при помощи:\n[kimazatot@gmail.com](mailto:kimazatot@gmail.com)\n+996503551110", parse_mode="Markdown")


bot.polling()



