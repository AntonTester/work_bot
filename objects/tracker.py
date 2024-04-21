import datetime


class Tracker:
    def __init__(self, id, name, name_time, cost, max_count, count=0, date_create=datetime.datetime.now()):
        self.id = id
        self.name = name
        self.count = count
        self.max_count = max_count
        self.name_time = name_time
        self.cost = cost
        self.date_create = date_create

    def add_time(self):
        self.count += 1
        if self.count >= self.max_count:
            self.count = self.max_count

    def is_completed(self):
        return self.count >= self.max_count
    def set_loose(self):
        self.count = self.max_count
