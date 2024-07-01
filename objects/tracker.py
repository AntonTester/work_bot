import datetime


class Tracker:
    def __init__(self, id, name, count_days, name_progress, cost, max_progress, progress=0,
                 date_create=datetime.datetime.now()):
        self.id = id
        self.name = name
        self.progress = progress
        self.max_progress = max_progress
        self.name_progress = name_progress
        self.cost = cost
        self.date_create = date_create
        self.count_days = count_days

    def add_time(self):
        self.progress += 1
        if self.progress >= self.max_progress:
            self.progress = self.max_progress

    def is_completed(self):
        return self.progress >= self.max_progress

    def is_loose(self):
        return ((datetime.datetime.now() - self.date_create).days > self.count_days) and self.progress != self.max_progress

    def set_loose(self):
        self.progress = self.max_progress
