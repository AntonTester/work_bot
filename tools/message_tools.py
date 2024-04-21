from random import randint

from enums.types import Status
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
    def get_keyboard_tracker(id, type):
        btns = {f"Добавить 1 {type}": "add",
                "Завершить": "end"
                }

        kb = CustomInlineKeyboard()
        kb.add_buttons(btns, f"tracker_{id}_")
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

    @staticmethod
    def get_keyboard_step(status):
        btns = {}

        if status == Status.SCHEDULE.value:
            btns = {'Разово': 'once',
                    'Ежедневно': 'everyday_1',
                    'Каждые 2 дня': 'everyday_2',
                    'Каждые 3 дня': 'everyday_3',
                    'Каждые 4 дня': 'everyday_4',
                    'По будням': 'work'
                    }
        elif status == Status.DATE.value:
            btns = {'Сегодня': 'today',
                    'Завтра': 'tomorrow'}
        elif status == Status.NOTIFICATION.value:
            btns = {'5 минут': 'noti_5',
                    '10 минут': 'noti_10',
                    '15 минут': 'noti_15',
                    '20 минут': 'noti_20'
                    }
        elif status == Status.DIFFICULTY.value:
            btns = {'Легко': 'diff_1',
                    'Нормально': 'diff_2',
                    'Сложно': 'diff_3'
                    }
        elif status == Status.TIME.value:
            btns = {'8:00': 'time_8',
                    '9:00': 'time_9',
                    '10:00': 'time_10',
                    '11:00': 'time_11',
                    '12:00': 'time_12',
                    '13:00': 'time_13',
                    '14:00': 'time_14',
                    '15:00': 'time_15',
                    '16:00': 'time_16',
                    '17:00': 'time_17',
                    '18:00': 'time_18',
                    '19:00': 'time_19',
                    '20:00': 'time_20',
                    '21:00': 'time_21',
                    '22:00': 'time_22',
                    '23:00': 'time_23',
                    }

        kb = CustomInlineKeyboard(False)
        kb.add_buttons(btns, f"task_")
        return kb.kb_full
