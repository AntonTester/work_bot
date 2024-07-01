import datetime

from tools.bot_client import BotClient
from tools.strings import CfgMessages as cm
from tools.message_tools import KeyboardTools as mt
from tools.string_tools import StringTools as st, StringTools


class Commentator:
    def __init__(self, bot, chat_id):
        self.bt = BotClient(bot)
        self.chat_id = chat_id
        self.chat_punish_id = -1001783638936
        self.messages = []

    async def show_alert(self, task, user):
        await self.bt.send_text(self.chat_id, f"Напоминаю, нужно сделать следующую задачу:\n\n"
                                              f"*{task.name}*\n\nУ тебя осталось ещё {3 - task.count_remember} напоминания",
                                mt.get_keyboard_task(task.id, user.count_diamonds))

    async def show_good_alert(self, user):
        await self.bt.send_text(self.chat_id, f"Вы выполнили задачу! Вы получили {user.last_change_rate} рейтинга "
                                              f"и {user.last_change_diamonds} 💎!\n\n"
                                              f"Ваш рейтинг - *{user.rate}*\n"
                                              f"Ваш баланс - *{user.count_diamonds}*💎\n\n"
                                              f"Ваше звание - *{StringTools.get_rate_name(user.rate)}*")
    async def show_transfer_alert(self, user):
        await self.bt.send_text(self.chat_id, f"Вы успешно перенесли задачу на час! У вас осталось {user.count_diamonds} 💎!")

    async def show_evil_alert(self, user):
        await self.bt.send_text(self.chat_id, f"Вы провалили задачу! Вы потеряли {user.last_change_rate} рейтинга.\n\n"
                                              f"Ваш рейтинг - *{user.rate}*\n\n"
                                              f"Ваше звание - *{StringTools.get_rate_name(user.rate)}*")

    async def show_punish(self):
        await self.bt.send_text(self.chat_punish_id,
                                f"Антон не выполнил задачу! Он заслуживает всеобщего осуждения и порицания! ")

    async def show_success(self):
        await self.bt.send_text(self.chat_id, f"Я записал твою задачу!")

    async def show_success_tracker(self):
        await self.bt.send_text(self.chat_id, f"Я записал твой трекер!")

    async def show_updated_tracker(self, tracker, message_id):
        await self.bt.edit_text(self.chat_id, message_id, st.get_tracker_info(tracker),
                                mt.get_keyboard_tracker(tracker.id, tracker.name_progress))

    async def show_trackers(self, trackers):
        for tracker in trackers:
            await self.bt.send_text(self.chat_id, st.get_tracker_info(tracker), mt.get_keyboard_tracker(tracker.id, tracker.name_progress))

    async def show_tasks(self, tasks):
        msg = ''
        for task in tasks:
            msg += st.get_task_info(task)
        await self.bt.send_text(self.chat_id, msg)

    async def show_step_instruction(self, status):
        await self.bt.send_text(self.chat_id, StringTools.get_text_instruction(status), mt.get_keyboard_step(status))

    async def show_instruction(self):
        await self.bt.send_text(self.chat_id, f"Отправь мне задачу! Формат: \n"
                                              f"*Название*\n"
                                              f"*Время*\n"
                                              f"*Сложность (Легко, Средне, Сложно)*\n"
                                              f"*Частота напоминания (Редко, Часто, Постоянно)*")

    async def show_instruction_tracker(self):
        await self.bt.send_text(self.chat_id, f"Отправь мне задачу! Формат: \n"
                                              f"*Трекер*\n"
                                              f"*Название*\n"
                                              f"*Количество дней на выполнение*\n"
                                              f"*Название времени*\n"
                                              f"*Цена*\n"
                                              f"*Количество времени*")
