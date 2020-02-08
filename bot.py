import requests
import vk_api
import datetime

vk_session = vk_api.VkApi(token='7e08864327faaafb6f4413c1860ae433c9f00c74ae233a46d87a0df9b7941b26040a9f87bd02986f4ac8d')

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 191424481)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        ev = event.object
        if ev.text == 'Глеб':
            if event.from_user:
                vk.messages.send(
                    peer_id=ev.peer_id,
                    random_id=0,
                    message='Гей'
                    )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=ev.peer_id,
                    random_id=0,
                    message='Гей'
                    )
        if ev.text == 'время' or ev.text == 'Время':
            now = datetime.datetime.now()
            if event.from_user:
                vk.messages.send(
                    peer_id=ev.peer_id,
                    random_id=0,
                    message='Московское время: ' + str(now.strftime("%H:%M"))
            )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=ev.peer_id,
                    random_id=0,
                    message='Московское время: ' + str(now.strftime("%H:%M"))
            )