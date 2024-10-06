import telebot
from telebot import types
from pathlib import Path



bot = telebot.TeleBot('6447507555:AAG_qa0y0wJa948Czo_jDcMImu3iMxl2gNM')

def menu_of_compositions():
    markup = types.InlineKeyboardMarkup()
    btn01 = types.InlineKeyboardButton('Huomentuoppi', callback_data='menu_of_compositions_selected_Huomentuoppi')
    btn02 = types.InlineKeyboardButton('Malselv-Hallingen', callback_data='menu_of_compositions_selected_MalselvHallingen')
    btn03 = types.InlineKeyboardButton('Retu-Matin', callback_data='menu_of_compositions_selected_RetuMatin')
    btn04 = types.InlineKeyboardButton('Taman-Kylan', callback_data='menu_of_compositions_selected_TamanKylan')
    markup.row(btn01, btn03)
    markup.row(btn02, btn04)
    return markup

def menu_of_Huomentuoppi():
    markup = types.InlineKeyboardMarkup()
    btn01 = types.InlineKeyboardButton('🎵 3 скрипка', callback_data='notes_Huomentuoppi_3_violin')
    btn02 = types.InlineKeyboardButton('🎵 Баян', callback_data='notes_Huomentuoppi_accordion')
    btn03 = types.InlineKeyboardButton('🎵 Гитара', callback_data='notes_Huomentuoppi_guitar')
    btnAudio = types.InlineKeyboardButton('🔊 Послушать', callback_data='audio_Huomentuoppi')
    markup.row(btn01, btn03)
    markup.row(btn02, btnAudio)
    return markup

def menu_of_MalselvHallingen():
    markup = types.InlineKeyboardMarkup()
    btn01 = types.InlineKeyboardButton('🎵 3 скрипка', callback_data='notes_MalselvHallingen_3_violin')
    btn02 = types.InlineKeyboardButton('🎵 Гитара', callback_data='notes_MalselvHallingen_guitar')
    btnAudio = types.InlineKeyboardButton('🔊 Послушать', callback_data='audio_MalselvHallingen')
    markup.row(btn01, btn02)
    markup.row(btnAudio)
    return markup

def menu_of_RetuMatin():
    markup = types.InlineKeyboardMarkup()
    btn01 = types.InlineKeyboardButton('🎵 1 скрипка', callback_data='notes_RetuMatin_1_violin')
    btn02 = types.InlineKeyboardButton('🎵 Гитара', callback_data='notes_RetuMatin_guitar')
    btnAudio = types.InlineKeyboardButton('🔊 Послушать', callback_data='audio_RetuMatin')
    markup.row(btn01, btn02)
    markup.row(btnAudio)
    return markup

def menu_of_TamanKylan():
    markup = types.InlineKeyboardMarkup()
    btn01 = types.InlineKeyboardButton('🎵 3 скрипка', callback_data='notes_TamanKylan_3_violin')
    btn02 = types.InlineKeyboardButton('🎵 Баян', callback_data='notes_TamanKylan_accordion')
    btn03 = types.InlineKeyboardButton('🎵 Гитара', callback_data='notes_TamanKylan_guitar')
    btn04 = types.InlineKeyboardButton('🎵 Контрабас', callback_data='notes_TamanKylan_double_bass')
    markup.row(btn01, btn03)
    markup.row(btn02, btn04)
    return markup


@bot.message_handler(commands=['start'])
def send_menu_of_compositions(msg):
    markup = menu_of_compositions()
    bot.send_message(msg.chat.id, 'Выберите композицию ⬇️', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('menu_of_compositions_selected_'))
def replace_menu_of_compositions(call):

    if call.data == 'menu_of_compositions_selected_Huomentuoppi':
        message_text = 'Выбрана *Huomentuoppi*\nРазмер 3/4\n🎵 - _скачать ноты_\n🔊 - _послушать аудио_'
        markup = menu_of_Huomentuoppi()

    elif call.data == 'menu_of_compositions_selected_MalselvHallingen':
        message_text = 'Выбрана *Malselv-Hallingen*\nРазмер 2/4\n🎵 - _скачать ноты_\n🔊 - _послушать аудио_'
        markup = menu_of_MalselvHallingen()

    elif call.data == 'menu_of_compositions_selected_RetuMatin':
        message_text = 'Выбрана *Retu-Matin Polkka*\nРазмер 2/4\n🎵 - _скачать ноты_\n🔊 - _послушать аудио_'
        markup = menu_of_RetuMatin()

    elif call.data == 'menu_of_compositions_selected_TamanKylan':
        message_text = 'Выбрана *Taman-Kylan Polkka*\nРазмер 2/4\n🎵 - _скачать ноты_\n🔊 - _послушать аудио_'
        markup = menu_of_TamanKylan()

    btn_back = types.InlineKeyboardButton('⬅️ Назад', callback_data='menu_of_compositions')
    markup.row(btn_back)

    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text=message_text, 
                          parse_mode='Markdown', 
                          reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('menu_of_compositions'))
def replace_menu_of_composition(call):
    markup = menu_of_compositions()
    message_text = 'Выберите композицию ⬇️'
    bot.edit_message_text(chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          text=message_text, 
                          reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('notes_'))
def replace_menu_download(call):

    # Huomentuoppi
    if call.data == 'notes_Huomentuoppi_3_violin':
        message_text = '3 скрипка Huomentuoppi'
        photo_path = Path('notes/huomentuoppi/Huomentuoppi_3_violin.jpg')
    elif call.data == 'notes_Huomentuoppi_accordion':
        message_text = 'Баян Huomentuoppi'
        photo_path = Path('notes/huomentuoppi/Huomentuoppi_accordion.jpg')
    elif call.data == 'notes_Huomentuoppi_guitar':
        message_text = 'Гитара Huomentuoppi'
        photo_path = Path('notes/huomentuoppi/Huomentuoppi_guitar.jpg')
    # Malselv-Hallingen
    elif call.data == 'notes_MalselvHallingen_3_violin':
        message_text = '3 скрипка Malselv-Hallingen'
        photo_path = Path('notes/malselv_hallingen/Malselv_Hallingen_3_violin.jpg')
    elif call.data == 'notes_MalselvHallingen_guitar':
        message_text = 'Гитара Malselv-Hallingen'
        photo_path = Path('notes/malselv_hallingen/Malselv_Hallingen_guitar.jpg')
    # Retu-Matin
    elif call.data == 'notes_RetuMatin_1_violin':
        message_text = '1 скрипка Retu-Matin Polkka'
        photo_path = Path('notes/retu_matin/RetuMatin_1_violin.jpg')
    elif call.data == 'notes_RetuMatin_guitar':
        message_text = 'Гитара Retu-Matin Polkka'
        photo_path = Path('notes/retu_matin/RetuMatin_guitar.jpg')
    # Taman Kylan
    elif call.data == 'notes_TamanKylan_3_violin':
        message_text = '3 скрипка Taman-Kylan Polkka'
        photo_path = Path('notes/taman_kylan/Taman_Kylan_3_violin.jpg')
    elif call.data == 'notes_TamanKylan_accordion':
        message_text = 'Баян Taman-Kylan Polkka'
        photo_path = Path('notes/taman_kylan/Taman_Kylan_accordion.jpg')
    elif call.data == 'notes_TamanKylan_guitar':
        message_text = 'Гитара Taman-Kylan Polkka'
        photo_path = Path('notes/taman_kylan/Taman_Kylan_guitar.jpg')
    elif call.data == 'notes_TamanKylan_double_bass':
        message_text = 'Контрабас Taman-Kylan Polkka'
        photo_path = Path('notes/taman_kylan/Taman_Kylan_double_bass.jpg')

    script_dir = Path(__file__).parent # Путь до текущего файла (conbrio_bot.py)
    file_path = script_dir / photo_path # relative_path - путь от текущего файла (conbrio_bot.py) до .jpg

    with open(file_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=message_text)



@bot.callback_query_handler(func=lambda call: call.data.startswith('audio_'))
def send_audio(call):

    # Huomentuoppi
    if call.data == 'audio_Huomentuoppi':
        message_text = 'Аудиозапись Huomentuoppi'
        audio_path = Path('notes/huomentuoppi/Huomentuoppi.mp3')
    # Malselv-Hallingen
    elif call.data == 'audio_MalselvHallingen':
        message_text = 'Аудиозапись Malselv-Hallingen'
        audio_path = Path('notes/malselv_hallingen/MalselvHallingen.mp3')
    # Retu-Matin
    elif call.data == 'audio_RetuMatin':
        message_text = 'Аудиозапись Retu-Matin Polkka'
        audio_path = Path('notes/retu_matin/RetuMatin.mp3')


    script_dir = Path(__file__).parent
    file_path = script_dir / audio_path

    with open(file_path, 'rb') as audio:
        bot.send_audio(call.message.chat.id, audio, caption=message_text)


# ЗАПУСК БОТА
# Бот сам перезапускается, если возникает ошибка
# или потеря соединения с сервером Telegram
bot.infinity_polling()