import datetime


class Task:
    def __init__(self, id, name, datetime, time_notification, type_schedule, difficult, last_completed):
        self.id = id
        self.name = name
        self.datetime = datetime
        self.time_notification = time_notification
        self.type_schedule = type_schedule
        self.count_remember = -5
        self.status = 0
        self.difficult = difficult
        self.last_completed = last_completed

    def is_need_remember(self):
        now = datetime.datetime.now()
        if self.type_schedule == 0:
            time = self.datetime + datetime.timedelta(minutes=self.time_notification * self.count_remember)
            return time <= now
        elif self.type_schedule in [1, 2, 3, 4]:
            return (self.last_completed
                    + datetime.timedelta(days=self.type_schedule)
                    + datetime.timedelta(minutes=self.time_notification * self.count_remember)) <= now
        elif self.type_schedule == 5:
            if datetime.datetime.now().weekday() in [0, 1, 2, 3, 4] and self.last_completed.day != datetime.datetime.now().day:
                current_date = datetime.datetime.now().replace(hour=self.last_completed.hour,
                                                   minute=self.last_completed.minute)
                return current_date + datetime.timedelta(minutes=self.time_notification * self.count_remember)


    def is_end_tries(self):
        return self.count_remember > 2

    def add_count_remember(self):
        self.count_remember += 1

    def set_failed(self):
        self.status = -1

    def set_complete(self):
        if self.type_schedule == 0:
            self.status = 1
        else:
            self.last_completed = datetime.datetime.now().replace(hour=self.datetime.hour, minute=self.datetime.minute)
