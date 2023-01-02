from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import base as cfg

'''******KeyboardButton'''
b1 = KeyboardButton("ПРОДОЛЖИТЬ")
kb_klient = ReplyKeyboardMarkup(resize_keyboard = True)
'''******KeyboardButton'''

'''******InlineKeyboardButton'''
mainmenu = InlineKeyboardMarkup(row_widh=2)
btnmaint = InlineKeyboardMarkup(row_widh=1)
btnios=InlineKeyboardButton(text="ios", callback_data="btnos") 
btnand = InlineKeyboardButton(text="android", callback_data="btnandroid")
btnmain = InlineKeyboardButton(text = "Получить", callback_data="btnmain")
'''******InlineKeyboardButton'''
'''******btnsubs******'''
def showChannels():
    keyboardbtn = InlineKeyboardMarkup(row_width=1)
    for channel in cfg.sponsors:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keyboardbtn.insert(btn)
    btnDoneSub = InlineKeyboardButton(text="Проверить подписку", callback_data="btndone")
    keyboardbtn.insert(btnDoneSub)
    return keyboardbtn
'''******btnsubs******'''
kb_klient.add(b1) 
mainmenu.add(btnios).add(btnand)
btnmaint.add(btnmain)