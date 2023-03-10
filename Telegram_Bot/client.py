from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from keyboards import kb
from inline import ikb


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать на игровой канал \nЯ твой бот дофамин и готов помочь тебе поиграть в различные игры \n Выбери любую игру:",
                        reply_markup=kb,
                        )

@dp.message_handler()
async def send_game(message: types.Message):
    if await message.answer("Pro_in_Minecraft"):
        await bot.send_game(message.from_user.id,
                        game_short_name="Pro_in_Minecraft",)
    
@dp.callback_query_handler()
async def game(callback: types.CallbackQuery):
    await callback.answer(url = "https://yandex.ru/games/app/212523?draft=true&lang=ru")







executor.start_polling(dp, skip_updates = True)