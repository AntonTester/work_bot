import ctypes
import datetime
import math
import random
from time import strftime

from enums.types import Status
from tools.strings import CfgMessages as cm
from tools.task_tools import TaskTools


class StringTools:
    @staticmethod
    def generate_dict(keys, default_value):
        new_dict = {}
        for key in keys:
            new_dict[key] = default_value
        return new_dict

    @staticmethod
    def get_text_instruction(status):
        if status == Status.TIME.value:
            return 'Выберите время выполнения задачи'
        elif status == Status.SCHEDULE.value:
            return 'Выберите периодичность задачи'
        elif status == Status.DATE.value:
            return 'Выберите дату'
        elif status == Status.DIFFICULTY.value:
            return 'Выберите сложность задачи'
        elif status == Status.NOTIFICATION.value:
            return 'Выберите частоту напоминания'
        else:
            return ''

    @staticmethod
    def shuffle_dict(dicts):
        keys = list(dicts.keys())
        random.shuffle(keys)

        temp_dict = dict()
        for key in keys:
            temp_dict.update({key: dicts[key]})
        return temp_dict

    @staticmethod
    def get_rate_name(rate):
        name = ''

        if rate == 2000:
            name = 'Новоприбывший'
        elif rate > 10000:
            name = 'Легенда Продуктивности'
        elif rate > 9000:
            name = 'Легенда Продуктивности'
        elif rate > 8000:
            name = 'Легенда Продуктивности'
        elif rate > 7000:
            name = 'Легенда Продуктивности'
        elif rate > 6000:
            name = 'Легенда Продуктивности'
        elif rate > 5000:
            name = 'Легенда Продуктивности'
        elif rate > 4000:
            name = 'Легенда Продуктивности'
        elif rate > 3000:
            name = 'Целеустремленный'
        elif rate > 2000:
            name = 'Энжоер'
        elif rate < 0:
            name = 'Дерьмо'
        elif rate < 1000:
            name = 'Ничтожество'
        elif rate < 1500:
            name = 'Скуфф'
        elif rate < 2000:
            name = 'Омежка'
        return name

    @staticmethod
    def get_lobby(players):
        player_names = StringTools.get_list_names(players)
        text = f"Игра \"Монополия\"\n\n" \
               f"Игроки: \n\n{player_names}\n"
        return text

    @staticmethod
    def get_list_names(players):
        res = ''
        for player in players:
            res += f"🥴 {player.name}\n"
        return res

    @staticmethod
    def get_progress(max, current):
        res = ''
        count_green = math.floor((current / max) * 10)
        for i in range(0, 10):
            if count_green > i:
                res += '🟩'
            else:
                res += '🟥'
        return res

    @staticmethod
    def get_alert_current_player(name):
        return cm.ALERT_PLAYER.replace('%name%', name)

    @staticmethod
    def get_result_dice(name, result):
        return cm.RESULT_DICE.replace('%name%', name).replace('%result%', result)

    @staticmethod
    def get_tracker_info(tracker):
        return (f'Ваш трекер - {tracker.name}'
                f'\n\nПрогресс: *({tracker.count}/{tracker.max_count})*'
                f'\n{StringTools.get_progress(tracker.max_count, tracker.count)}'
                f'\n\nПрошло дней: *{(datetime.datetime.now() - tracker.date_create).days}*')

    @staticmethod
    def get_task_info(task):
        return (f'*{task.name}*\n'
                f'Дата: *{TaskTools.get_str_time_text(task.datetime)}*\n'
                '\n'
                )

    @staticmethod
    def get_color_player(color_type):
        color_type = color_type.value
        colors = ['🟥', '🟨', '🟩', '🟪']
        return colors[color_type]

    @staticmethod
    def get_color_house(color_type):
        color_type = int(color_type.value)
        colors = ['🟤', '🟠', '🔵', '🟡', '🚘', '👨🏻‍🔧', '🟢', '🔴', '🟣', '⚫️']
        return colors[color_type]

    @staticmethod
    def get_emoji_on_field(number, players):
        found_players = list(filter(lambda i: i.position == number, players))
        if len(found_players) > 1:
            return '👨‍👩‍👦‍👦'
        elif len(found_players) == 1:
            return found_players[0].emoji
        else:
            return '⬜'

    @staticmethod
    def get_map(map, players):
        res = ''
        for num, cell in enumerate(map.cells):
            emoji = StringTools.get_emoji_on_field(num, players)
            mods_text = ''
            if emoji == '⬜':
                emoji = '⬜' if cell.host is None else cell.host.color

            if cell.is_system:
                mods_text = '*'
            elif emoji != '⬜':
                mods_text = '_'

            if cell.is_system:
                res += f'{emoji}{mods_text}{cell.house.name}{mods_text}\n'
            else:
                res += f'{emoji}{StringTools.get_color_house(cell.house.type)} {cell.house.name}\n'
        return res
