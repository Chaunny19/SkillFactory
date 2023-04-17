from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from keyboards import kb
from inline import PiM, KarateKido, CQ, F1, Neon, Ski, KiU, SO, Nex, Qube, TubeR


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start']) # Start Button
async def send_welcome(message: types.Message):
        await bot.send_message(message.from_user.id, "Добро пожаловать на игровой канал \nЯ твой бот дофамин и готов помочь тебе поиграть в различные игры \n Выбери любую игру:",
                        reply_markup=kb,
                        )


@dp.message_handler(lambda message: 'Karate Kido' in message.text)
async def send_game(message: types.Message):
        await bot.send_game(message.from_user.id, game_short_name='KarateKido', reply_markup=KarateKido)

@dp.message_handler(lambda message: 'MinecraftQuiz' in message.text)
async def send_game(message: types.Message):
        await bot.send_game(message.from_user.id, game_short_name='MinecraftQuiz', reply_markup=PiM)

@dp.message_handler(lambda message: 'Color Quest' in message.text)
async def send_game(message: types.Message):
    await bot.send_game(message.from_user.id, game_short_name='Color_Quest', reply_markup=CQ)
            
@dp.message_handler(lambda message: 'F1 Racer' in message.text)
async def send_game(message: types.Message):            
    await bot.send_game(message.from_user.id, game_short_name='F1_Racer', reply_markup=F1)
       
@dp.message_handler(lambda message: 'Tube Runner' in message.text)
async def send_game(message: types.Message):
    await bot.send_game(message.from_user.id, game_short_name='Tube_Runner', reply_markup=TubeR)
        
@dp.message_handler(lambda message: 'Hexonix' in message.text)
async def send_game(message: types.Message):
    await bot.send_game(message.from_user.id, game_short_name='Hexonix', reply_markup=Nex)

@dp.message_handler(lambda message: 'Qube 2048' in message.text)
async def send_game(message: types.Message):
    await bot.send_game(message.from_user.id, game_short_name='Qube_2048', reply_markup=Qube)

@dp.message_handler(lambda message: 'Space Orbit' in message.text)
async def send_game(message: types.Message):
    await bot.send_game(message.from_user.id, game_short_name='Space_Orbit', reply_markup=SO)
        
@dp.message_handler(lambda message: 'Keep it Up' in message.text)
async def send_game(message: types.Message):
    await bot.send_game(message.from_user.id, game_short_name='Keep_it_Up', reply_markup=KiU)
        
@dp.message_handler(lambda message: 'Groovy Ski' in message.text)
async def send_game(message: types.Message):
     await bot.send_game(message.from_user.id, game_short_name='Groovy_Ski', reply_markup=Ski)
        
@dp.message_handler(lambda message: 'Neon Blaster 2' in message.text)
async def send_game(message: types.Message):
        await bot.send_game(message.from_user.id, game_short_name='Neon_Blaster_2', reply_markup=Neon)

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda v: v.game_short_name == 'KarateKido')
async def process_callback_game(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/karatekid2-654b0e63ab7c67165b3e96521453f685ec08966c#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DiJVDbJaHHw2qH9q3U29_4gKPXIjssA0V4OZ1johPe-xEyLaNrf7pZiJXqZcYFPK0')
    

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda l: l.game_short_name == 'MinecraftQuiz')
async def process_callback_game_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://yandex.ru/games/app/212523?draft=true&lang=ru')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda q: q.game_short_name == 'Color_Quest')
async def process_callback_game_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://yandex.ru/games/app/212880?draft=true&lang=ru')


# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'F1_Racer')
async def process_callback_game_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/Q8PWil-869fa8a8abb2c2ff7cf3f3595d00a070cb83b961#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3Dn6utbLmVqHtp7FWDU1R9UN14P4UTBbdsCOCOqwJVirYXk2Nmmg3-WKTZwikYS2-A')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'Neon_Blaster_2')
async def process_callback_game_4(callback_query: types.CallbackQuery):
        # Установка счета в игре для пользователя

    # Отправка сообщения об успешном обновлении счета игрока
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/neonblast2-c95df69fb728210cc23bea297498022678ef32de#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DY-Py5Vf_egD58KmTEX8FZmNWH4T4j5iSn1bfed8orlOtwTvCqVnwA7r_08cuQKL7')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'Groovy_Ski')
async def process_callback_game_5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/CqlO4bdma-3b4da0e0cdb95cac9b52877612787d862905f794#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DBUtPr-Ek4gT3nPHW_7uJ-vnPPVdIt6QZXpATvpnLOzQljMj15oawnbj2nYGKTYGA')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'Keep_it_Up')
async def process_callback_game_5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/a3pyHGoadz-a973298ac96ea5009a9cc87e5ec87965b9dbdd1a#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DaBx3xzxuTdDbmD6MkdnuGs1dnL8P3ihRQnFDPDa9fA4gAoTj7XTAPuhNgbYmhXpB')
    
# обработчик callback-запросов для игр
@dp.callback_query_handler()
async def process_callback_game_5(callback_query: types.CallbackQuery):
    game_url = types.CallbackQuery(
         game_short_name = 'Space_Orbit',
    )
    await bot.set_game_score(user_id=callback_query.from_user.id,
                                 score=1,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 force=True)
    await bot.answer_callback_query(callback_query.id, game_url, url='https://prizes.gamee.com/game-bot/R4k6GrC-b502c0eb81aa0621e616d4bee62b663378e5b008#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DxBgO03eVe8esbbs5mMlS3A9IdnW3yufyjqyesyivgyszyoe--3p1qFZgMVZcSE9p')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'Hexonix')
async def process_callback_game_5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/hexonix-24a2d2a24df74f887f180aac3228d7e57ef8ee62#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DnJJJseKAxJi4ZEvPTKrAZUbelYmQ54JJEiMh1IVgtboQWBJgCLPscUMVXCccZ8xg')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'Qube_2048')
async def process_callback_game_5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/qube2048-34bc195bd294689f38756b28a61aeadfa50b5cb6#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D2tVMkhcFlYUosPtcWrZCx8aSSCVkfuuAeY6N2rkgXSp_VsYL_b_bvRg20ZZFAsvL')

# обработчик callback-запросов для игр
@dp.callback_query_handler(lambda h: h.game_short_name == 'Tube_Runner')
async def process_callback_game_5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url='https://prizes.gamee.com/game-bot/tuberunner-46bed7ad09b9364ff47eda7bfcfd19c9af29ac72#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DlXodb-P9-WGDeQ6ocpBtpi2TGfqdlEa7aDwScfsjLpQOdVTGfsMmZBHOOKcQ6oy6')

@dp.inline_handler()
async def handle_inline_query(inline_query: types.InlineQuery):
    # Создание объекта InlineQueryResultGame для игры
    game_1 = types.InlineQueryResultGame(
        id='game_1',
        game_short_name='MinecraftQuiz',
        reply_markup=PiM
    )
    game_2 = types.InlineQueryResultGame(
         id = 'Karate Kido 2',
         game_short_name='KarateKido',
         reply_markup=KarateKido
    )
    game_3 = types.InlineQueryResultGame(
         id = 'Color Quest',
         game_short_name='Color_Quest',
         reply_markup=CQ
    )
    game_4 = types.InlineQueryResultGame(
         id = 'F1 Racer',
         game_short_name='F1_Racer',
         reply_markup=F1
    )
    game_5 = types.InlineQueryResultGame(
         id = 'Tube Runner',
         game_short_name='Tube_Runner',
         reply_markup=TubeR
    )
    game_6 = types.InlineQueryResultGame(
         id = 'Hexonix',
         game_short_name='Hexonix',
         reply_markup=Nex
    )
    game_7 = types.InlineQueryResultGame(
         id = 'Qube 2048',
         game_short_name='Qube_2048',
         reply_markup=Qube
    )
    game_8 = types.InlineQueryResultGame(
         id = 'Space Orbit',
         game_short_name='Space_Orbit',
         reply_markup=SO
    )
    game_9 = types.InlineQueryResultGame(
         id = 'Keep it Up',
         game_short_name='Keep_it_Up',
         reply_markup=KiU
    )
    game_10 = types.InlineQueryResultGame(
         id = 'Groovy Ski',
         game_short_name='Groovy_Ski',
         reply_markup=Ski
    )
    game_11 = types.InlineQueryResultGame(
         id = 'Neon Blaster 2',
         game_short_name='Neon_Blaster_2',
         reply_markup=Neon
    )

    # Отправка ответа на inline-запрос
    await bot.answer_inline_query(inline_query.id, results=[game_1, game_2, game_3, game_4, game_5, game_6, game_7, game_8, game_9, game_10, game_11], cache_time=1)


@dp.message_handler()
async def error(message: types.Message):
    await message.answer('Извините, не понимаю о чем вы\nЧтобы начать играть выберите игру', reply_markup=kb)


executor.start_polling(dp, skip_updates = True)