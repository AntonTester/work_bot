import datetime


class Task:
    def __init__(self, id, name, time, time_notification, type_schedule, difficult):
        self.id = id
        self.name = name
        self.time = time
        self.time_notification = time_notification
        self.type_schedule = type_schedule
        self.count_remember = 0
        self.status = 0
        self.difficult = difficult

    def is_need_remember(self):
        now = datetime.datetime.now()
        time = self.time + datetime.timedelta(minutes=self.time_notification * self.count_remember)
        return time <= now
    def is_end_tries(self):
        return self.count_remember > 3

    def add_count_remember(self):
        self.count_remember += 1

    def set_failed(self):
        self.status = -1

    def set_complete(self):
        self.status = 1

