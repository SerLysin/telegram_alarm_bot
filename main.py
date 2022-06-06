# coding: utf8
from telegram.ext import Updater, CommandHandler
import telegram


from telethon import TelegramClient, events, sync

#init part
api_id = 11639393
api_hash = 'e1abe4fb2a169e4c8a3081442d81a7d3'
client = TelegramClient('anon', api_id, api_hash)

user_input_channel = 'https://t.me/testtest958' #change server to test

list_cities = ["Київ", "Донецьк", "Луганськ", "Тернопіль", "Одеса", "Житомир", "Дніпро", "Львів", "Івано-Франківськ", "Харків", "Вінниця", "Рівне", "Хмельницький", "Запоріжжя", "Луцьк", "Полтава", "Чернівці", "Черкаси", "Ужгород", "Миколаїв", "Кропивницький", "Суми", "Чернігів", "Херсон"]
list_regions = ["Київська", "Львівська", "Івано-Франківська", "Тернопільська", "Дніпропетровська", "Харківська", "Вінницька", "Рівненська", "Хмельницька", "Одеська", "Запорізька", "Волинська", "Полтавська", "Чернівецька", "Черкаська", "Закарпатська", "Миколаївська", "Кіровоградська", "Житомирська", "Сумська", "Чернігівська", "Херсонська", "Донецька", "Луганська"]

@client.on(events.NewMessage(chats=user_input_channel))
async def my_event_handler(event):
    msg = event.raw_text.split(' ')

    is_down = False
    city_region = ""

    #check if alaram is down in the region
    for word in msg:
        if "відбій" in word:
            is_down = True
        if "Відбій" in word:
            is_down = True


    for word in msg:
        if "м." in word:
            for i in msg:
                if i in list_cities:
                    city_region = "м. "+i
                    break
                else:
                    continue
        elif "область" in word:
            for i in msg:
                if i in list_regions:
                    city_region = i + " область"
                    #print(i)
                    break
                else:
                    continue

    if is_down:
        print("У " + city_region + " відбій повітряної тривоги. Можна повертатись додому!")
    else:
        print("У " + city_region + " оголошена повітряна тривога. Йдіть в укриття!")

client.start()
client.run_until_disconnected()

