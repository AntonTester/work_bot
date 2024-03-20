import asyncio
import logging
import threading
import time
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types

from enums.types import TypeNotification, TypeSchedule
from gameplay.commentator import Commentator
from objects.task import Task
from tools.db_client import DbClient
from tools.task_tools import TaskTools

# Configure logging
logging.basicConfig(level=logging.INFO)
# API_TOKEN = '5318895791:AAG4zi5nqkVyY3erbpi0lIUPPuMaIQMxCwg'

API_TOKEN = '5470429630:AAHarmYA5wa-RrbaE-QtamdCuVHtAciso4g'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
commentator = Commentator(bot, 505644694)
db = DbClient()
user = db.get_user('floppa_tonn')
tasks = db.get_tasks()
status = ''

@dp.message_handler(commands='e')
async def lobby(message):
    print(message)
    global status
    status = 'create'
    await commentator.show_instruction()

@dp.message_handler()
async def lobby(message):
    print(message)
    global tasks
    db.check_user(message.chat.username, message.chat.first_name)
    task = TaskTools.get_task_from_text(message.text)
    db.add_new_task(task)
    tasks = db.get_tasks()
    await commentator.show_success()


async def check_tasks():
    is_changed = False
    while True:
        for task in tasks:
            if task.is_need_remember() and task.status == 0:
                task.add_count_remember()
                if task.is_end_tries():
                    is_changed = True
                    task.set_failed()
                    user.loose_task()
                    await commentator.show_evil_alert(user)
                    await commentator.show_punish()
                else:
                    await commentator.show_alert(task)
        if is_changed:
            is_changed = False
            db.update_user(user)
            db.update_task(tasks)

        await asyncio.sleep(2)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('success'))
async def cancel(callback_query: types.CallbackQuery):
    id = callback_query.data.split('_')[1]
    task = TaskTools.get_task(tasks, id)
    task.set_complete()
    user.complete_task(task)
    db.update_task(tasks)
    db.update_user(user)
    await commentator.show_good_alert(user)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(check_tasks())
    executor.start_polling(dp, skip_updates=True)
