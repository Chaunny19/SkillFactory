from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


KarateKido = InlineKeyboardMarkup(row_width=2)
PiM = InlineKeyboardMarkup(row_width=1)
CQ = InlineKeyboardMarkup(row_width=2)
F1 = InlineKeyboardMarkup(row_width=2)
Neon = InlineKeyboardMarkup(row_width=2)
Ski = InlineKeyboardMarkup(row_width=2)
KiU = InlineKeyboardMarkup(row_width=2)
SO = InlineKeyboardMarkup(row_width=2)
Nex = InlineKeyboardMarkup(row_width=2)
Qube = InlineKeyboardMarkup(row_width=2)
TubeR = InlineKeyboardMarkup(row_width=2)

btn1 = InlineKeyboardButton(text="Играть в Karate Kido 2", callback_game='KarateKido')
btn2 = InlineKeyboardButton(text='Играть в MinecraftQuiz', callback_game='MinecraftQuiz')
btn3 = InlineKeyboardButton(text='Играть в Color Quest', callback_game='Color_Quest')
btn4 = InlineKeyboardButton(text='Играть в F1 Racer', callback_game='F1_Racer')
btn5 = InlineKeyboardButton(text='Играть в Neon Blaster 2', callback_game='Neon_Blaster_2')
btn6 = InlineKeyboardButton(text='Играть в Groovy Ski', callback_game='Groovy_Ski')
btn7 = InlineKeyboardButton(text='Играть в Keep it Up', callback_game='Keep_it_Up')
btn8 = InlineKeyboardButton(text='Играть в Space Orbit', callback_game='Space_Orbit')
btn9 = InlineKeyboardButton(text='Играть в Hexonix', callback_game='Nexonix')
btn10 = InlineKeyboardButton(text='Играть в Qube 2048', callback_game='Qube_2048')
btn11 = InlineKeyboardButton(text='Играть в Tube Runner', callback_game='Tube_Runner')
KarateKido.add(btn1)
PiM.add(btn2)
CQ.add(btn3)
F1.add(btn4)
Neon.add(btn5)
Ski.add(btn6)
KiU.add(btn7)
SO.add(btn8)
Nex.add(btn9)
Qube.add(btn10)
TubeR.add(btn11)
