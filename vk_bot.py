import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import settings
import commands

# send function
def write_msg(user_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

# this code for work with bot
vk_session = vk_api.VkApi(token = settings.vk_bot_token) # your vk token
longpoll = VkLongPoll(vk_session)
print('(ИИ)СуС готов к работе')

# message sendler
def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text.lower()
                array_request = request.split(' ')
                if array_request[0] == 'привет' or array_request[0] == 'здарова':
                    write_msg(event.user_id, 'Здарова Дружище\nПиши "Помощь" чтобы увидеть список того, что я умею')
                elif array_request[0] == 'помощь':
                    write_msg(event.user_id, 'Полезные команды:\n\
                                                    1. Погода\n\
                                                    2. Вероятность ...(Инфа только в %)\n\
                                                    3. Инфа ...\n\
                                                    4. Перевод ...\n\
                                                    5. Мперевод ...')
                elif array_request[0] == 'погода':
                    write_msg(event.user_id, commands.open_weather_map_service())
                elif array_request[0] == 'вероятность':
                    write_msg(event.user_id,'"' + request[12:] + '" ' + commands.probability_number())
                elif array_request[0] == 'инфа':
                    write_msg(event.user_id, '"' + request[5:] + '" Ответ: ' + commands.get_info())
                elif array_request[0] == 'перевод':
                    write_msg(event.user_id, commands.translate(request))
                elif array_request[0] == 'мперевод':
                    write_msg(event.user_id, commands.mem_translate(request))
                else:
                    write_msg(event.user_id, 'Не понял вашего ответа...\n"Помощь" в помощь')