import datetime


class Task:
    def __init__(self, id, name, datetime, time_notification, type_schedule, difficult):
        self.id = id
        self.name = name
        self.datetime = datetime
        self.time_notification = time_notification
        self.type_schedule = type_schedule
        self.count_remember = -1
        self.status = 0
        self.difficult = difficult

    def is_need_remember(self):
        now = datetime.datetime.now()
        if self.type_schedule == 0:
            time = self.datetime + datetime.timedelta(minutes=self.time_notification * self.count_remember)
            return time <= now

    def is_end_tries(self):
        return self.count_remember > 2

    def add_count_remember(self):
        self.count_remember += 1

    def set_failed(self):
        self.status = -1

    def set_complete(self):
        self.status = 1
