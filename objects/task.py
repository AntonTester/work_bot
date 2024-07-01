import datetime


class Task:
    def __init__(self, id, name, datetime, time_notification, type_schedule, difficult, last_completed, transfers=0):
        self.id = id
        self.name = name
        self.datetime = datetime
        self.time_notification = time_notification
        self.type_schedule = type_schedule
        self.count_remember = -1
        self.status = 0
        self.difficult = difficult
        self.last_completed = last_completed
        self.transfers = transfers

    def is_need_remember(self):
        now = datetime.datetime.now()
        transfer = (60 * self.transfers)
        if self.type_schedule == 0:
            time = self.datetime + datetime.timedelta(minutes=self.time_notification * self.count_remember + transfer)
            return time <= now
        elif self.type_schedule in [1, 2, 3, 4]:
            return (self.last_completed
                    + datetime.timedelta(days=self.type_schedule, minutes=self.time_notification * self.count_remember + transfer)
                    + datetime.timedelta()) <= now
        elif self.type_schedule == 5:
            if datetime.datetime.now().weekday() in [0, 1, 2, 3, 4] and self.last_completed.day != datetime.datetime.now().day:
                current_date = datetime.datetime.now().replace(hour=self.last_completed.hour,
                                                               minute=self.last_completed.minute+transfer)
                return current_date + datetime.timedelta(minutes=self.time_notification * self.count_remember)


    def is_end_tries(self):
        return self.count_remember > 2

    def add_count_remember(self):
        self.count_remember += 1
    def transfer(self):
        self.count_remember = -1
        self.transfers += 1

    def set_failed(self):
        self.status = -1

    def set_complete(self):
        self.transfers = 0
        if self.type_schedule == 0:
            self.status = 1
        else:
            self.last_completed = datetime.datetime.now().replace(hour=self.datetime.hour, minute=self.datetime.minute)
