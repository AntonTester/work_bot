from datetime import datetime
from datetime import datetime, timedelta

from enums.types import TypeSchedule
from objects.task import Task
from objects.tracker import Tracker


class TaskTools:
    @staticmethod
    def get_task_from_text(text):
        name, time_str, time_notification_str, diff_str = text.split('\n')
        time_task = datetime.strptime(time_str, '%d.%m.%y %H:%M')
        time_task = TaskTools.get_time(time_str)
        time_notification = int(time_notification_str)
        diff = int(diff_str)
        return Task(0, name, time_task, time_notification, TypeSchedule.ONCE.value, diff)

    @staticmethod
    def get_tracker_from_text(text):
        a, name, name_time, cost, count = text.split('\n')
        return Tracker(0, name, name_time, int(cost), int(count))

    @staticmethod
    def get_task(tasks, id):
        try:
            return list(filter(lambda it: int(it.id) == int(id), tasks))[0]
        except:
            return None

    @staticmethod
    def get_tracker(trackers, id):
        try:
            return list(filter(lambda it: int(it.id) == int(id), trackers))[0]
        except:
            return None

    @staticmethod
    def get_time(time_str):
        if '.' in time_str:
            return datetime.strptime(time_str, '%d.%m.%y %H:%M') - timedelta(hours=3)
        else:
            now = datetime.now()
            hour, minute = time_str.split(':')
            return datetime(now.year, now.month, now.day, int(hour), int(minute)) - timedelta(hours=3)

    @staticmethod
    def get_str_time(time, is_test=False):
        if is_test:
            return time.strftime('%Y-%m-%d %H:%M')
        else:
            return (time-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M')