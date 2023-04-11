import telebot
from telebot import types
from read_pdf import pdf_to_mp3

# Токен необходимо получить у бота @Botfather
TOKEN = 'Ваш токен'

# Инициализируем бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    """ Функция приветствия пользователя в первый раз """
    bot.reply_to(message, 'Здарствуйте, я могу конвертировать PDF файлы в MP3 формат\n\
                 Отправьте мне файл в формате PDF')


@bot.message_handler(content_types=['document'])
def get_document(message):
    """
    Функция принимает у пользователя документ
    если его формат PDF то запрашивает основной язык
    для озвучки, иначе сообщает о некорректном формате
    """

    if message.document.file_name[len(message.document.file_name) - 4:] == '.pdf':

        # Инициализируем полученный документ
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Сохраняем его на локальный диск
        # Документ имеет одно имя за ненадобностью хранить на диске предыдущие
        pdf_path = 'pdf_book/book.pdf';
        with open(pdf_path, 'wb') as pdf:
            pdf.write(downloaded_file)

        # Панель управления для выбора языка
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("English")
        btn2 = types.KeyboardButton("Russian")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, 'Выберите язык', reply_markup=markup)

    else:
        bot.reply_to(message, 'Я ожидаю увидеть файл в формате PDF')


@bot.message_handler(content_types=["text"])
def send_audio(message):
    """
    Функция основываясь на выборе языка передает путь и языка в
    функцию конвертатора которая находится в файле read_pdf.py
    """
    if message.text.lower() == 'english':
        bot.reply_to(message, 'Пожалуйста подождите, идет обработка...')
        pdf_to_mp3('pdf_book/book.pdf', language='en')
        with open('mp3_book/audio.mp3', 'rb') as audio:
            bot.send_audio(message.from_user.id, audio, 'Ваша книга')

    elif message.text.lower() == 'russian':
        bot.reply_to(message, 'Пожалуйста подождите, идет обработка...')
        pdf_to_mp3('pdf_book/book.pdf', language='ru')
        with open('mp3_book/audio.mp3', 'rb') as audio:
            bot.send_audio(message.from_user.id, audio, 'Ваша книга')

    else:
        bot.reply_to(message, 'Я не совсем понял вас, выберите язык с панели упровления')


bot.polling()