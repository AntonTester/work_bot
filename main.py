import asyncio
import logging
import threading
import time
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, executor, types

from enums.types import TypeSchedule, Status
from gameplay.commentator import Commentator
from objects.task import Task
from tools.db_client import DbClient
from tools.task_tools import TaskTools

# Configure logging
logging.basicConfig(level=logging.INFO)
API_TOKEN = '5470429630:AAHarmYA5wa-RrbaE-QtamdCuVHtAciso4g'
#API_TOKEN = '6451320447:AAEFDSNhzpm3Z9ahajLrzi4JbHBaohFrfRE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
commentator = Commentator(bot, 505644694)
db = DbClient()
user = db.get_user('floppa_tonn')
tasks = db.get_tasks()
trackers = db.get_trackers()
status = 'create'
current_task = Task(0, '', 0, 0, 0, 0, None)

@dp.message_handler(commands="r")
async def cancel(message):
    global trackers
    trackers = db.get_trackers()
    await commentator.show_trackers(trackers)
@dp.message_handler(commands="l")
async def cancel(message):
    await commentator.show_tasks(tasks)
@dp.message_handler(commands="rr")
async def cancel(message):
    await commentator.show_instruction_tracker()

@dp.message_handler()
async def lobby(message):
    print(message)
    global status, trackers
    status = 'create'
    if message.chat.id > 0:
        if 'Трекер' in message.text:
            tracker = TaskTools.get_tracker_from_text(message.text)
            db.add_new_tracker(tracker)
            trackers = db.get_trackers()
            await commentator.show_success_tracker()
        else:
            if status == Status.CREATE.value:
                current_task.name = message.text
                status = Status.SCHEDULE.value

            await commentator.show_step_instruction(status)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('task'))
async def lobby(callback_query: types.CallbackQuery):
    global status, tasks
    data = callback_query.data.split('_')[1]

    if data == 'once':
        status = Status.DATE.value
    elif data == 'everyday':
        num = int(callback_query.data.split('_')[2])
        if num == 1:
            current_task.type_schedule = TypeSchedule.EVERYDAY_1.value
        elif num == 2:
            current_task.type_schedule = TypeSchedule.EVERYDAY_2.value
        elif num == 3:
            current_task.type_schedule = TypeSchedule.EVERYDAY_3.value
        current_task.datetime = datetime.today().replace(hour=0, minute=0)
        status = Status.TIME.value
    elif data == 'work':
        current_task.type_schedule = TypeSchedule.WORK.value
        status = Status.TIME.value
        current_task.datetime = datetime.today().replace(hour=0, minute=0)
    elif data == 'today':
        current_task.datetime = datetime.today().replace(hour=0, minute=0)
        status = Status.TIME.value
    elif data == 'tomorrow':
        current_task.datetime = datetime.today().replace(hour=0, minute=0) + timedelta(days=1)
        status = Status.TIME.value
    elif data == 'time':
        hours = callback_query.data.split('_')[2]
        current_task.datetime = current_task.datetime + timedelta(hours=int(hours))
        status = Status.NOTIFICATION.value
    elif data == 'noti':
        value = callback_query.data.split('_')[2]
        current_task.time_notification = int(value)
        status = Status.DIFFICULTY.value
    elif data == 'diff':
        diff = callback_query.data.split('_')[2]
        current_task.difficult = int(diff)
    if data == 'diff':
        db.check_user(callback_query['from'].username, callback_query['from'].first_name)
        db.add_new_task(current_task)
        tasks = db.get_tasks()
        status = 'create'
        await commentator.show_success()
    else:
        await commentator.show_step_instruction(status)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('tracker'))
async def lobby(callback_query: types.CallbackQuery):
    global status, tasks
    data, action = callback_query.data.split('_')[1:3]
    tracker = TaskTools.get_tracker(trackers, int(data))
    if action == 'add':
        tracker.add_time()
        await commentator.show_updated_tracker(tracker, callback_query.message.message_id)
    else:
        if tracker.is_completed():
            user.complete_tracker(tracker)
            await commentator.show_good_alert(user)
        else:
            user.loose_tracker(tracker)
            tracker.set_loose()
            await commentator.show_evil_alert(user)
    db.update_tracker(trackers)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('success'))
async def cancel(callback_query: types.CallbackQuery):
    id = callback_query.data.split('_')[1]
    task = TaskTools.get_task(tasks, id)
    task.set_complete()
    user.complete_task(task)
    db.update_task(tasks)
    db.update_user(user)
    await commentator.show_good_alert(user)


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


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(check_tasks())
    executor.start_polling(dp, skip_updates=True)
