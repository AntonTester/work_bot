from random import randint

from tools.custom_inline_keyboard import CustomInlineKeyboard
from tools.string_tools import StringTools as st


class KeyboardTools:
    @staticmethod
    def get_keyboard_host(name_game=''):
        btns = {"Присоединиться": "join",
                "Начать": "start"
                }

        kb = CustomInlineKeyboard()
        kb.add_buttons(btns, "host_")
        return kb.kb_full
    @staticmethod
    def get_keyboard_round(name_game=''):
        btns = {"🎲Бросить кубик": "dice"
                }

        kb = CustomInlineKeyboard()
        kb.add_buttons(btns, "")
        return kb.kb_full

    @staticmethod
    def get_keyboard_task(task_id):
        btns = {"🎲Сделал": f"_{task_id}"
                }

        kb = CustomInlineKeyboard()
        kb.add_buttons(btns, f"success")
        return kb.kb_full
