from datetime import datetime

from enums.types import TypeSchedule
from objects.task import Task


class TaskTools:
    @staticmethod
    def get_task_from_text(text):
        name, time_str, time_notification_str, diff_str = text.split('\n')
        time_task = datetime.strptime(time_str, '%d.%m.%y %H:%M')
        time_notification = int(time_notification_str)
        diff = int(diff_str)
        return Task(0, name, time_task, time_notification, TypeSchedule.ONCE.value, diff)

    @staticmethod
    def get_task(tasks, id):
        try:
            return list(filter(lambda it: int(it.id) == int(id), tasks))[0]
        except:
            return None
