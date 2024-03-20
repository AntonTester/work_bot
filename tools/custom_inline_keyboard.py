import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from tools.string_tools import StringTools as st


class CustomInlineKeyboard:
    def __init__(self, is_row=True):
        self.kb_full = InlineKeyboardMarkup(row_width=3)
        self.is_row = is_row

    def add_buttons(self, buttons, callback_root="", is_shuffle=False):
        if is_shuffle:
            buttons = st.shuffle_dict(buttons)
        if self.is_row:
            btns = []
            self.kb_full.row()
            for name, callback in buttons.items():
                btn = InlineKeyboardButton(name, callback_data=f"{callback_root}{callback}")
                self.kb_full.insert(btn)
        else:
            for name, callback in buttons.items():
                btn = InlineKeyboardButton(name, callback_data=f"{callback_root}{callback}")
                self.kb_full.add(btn)

    def add_switch_buton(self, name, text=""):
       btn = InlineKeyboardButton(name, switch_inline_query_current_chat=text)
       self.kb_full.add(btn)

    def add_web(self):  # создание клавиатуры с webapp кнопкой
        webAppTest = WebAppInfo(url="https://telegram.mihailgok.ru")  # создаем webappinfo - формат хранения url
        one_butt = InlineKeyboardButton(text="Тестовая страница", web_app=webAppTest)  # создаем кнопку типа webapp
        self.kb_full.add(one_butt)  # добавляем кнопки в клавиатуру
