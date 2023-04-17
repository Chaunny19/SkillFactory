from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)

b1 = KeyboardButton("MinecraftQuz")
b2 = KeyboardButton("Karate Kido 2")
b3 = KeyboardButton("Color Quest")
b4 = KeyboardButton("F1 Racer")
b5 = KeyboardButton("Neon Blaster 2")
b6 = KeyboardButton("Groovy Ski")
b7 = KeyboardButton("Keep it Up")
b8 = KeyboardButton("Space Orbit")
b9 = KeyboardButton("Hexonix")
b10 = KeyboardButton("Qube 2048")
b11 = KeyboardButton("Tube Runner")
kb.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11)