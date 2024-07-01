import datetime


class User:
    def __init__(self, login, name, rate, spree, count_diamonds):
        self.name = name
        self.login = login
        self.rate = rate
        self.spree = spree
        self.last_change_rate = 0
        self.last_change_diamonds = 0
        self.count_diamonds = count_diamonds

    def loose_task(self):
        self.last_change = int(10 * (1 + self.spree / 4))
        self.rate -= self.last_change
        self.spree = 0

    def use_diamond(self):
        if self.count_diamonds > 0:
            self.count_diamonds -= 1

    def complete_task(self, task):
        self.spree += task.difficult
        if self.spree > 20:
            self.spree = 20
        self.last_change_rate = int(10 * (1 + (task.difficult * (self.spree / 20))))
        self.last_change_diamonds = 2 * task.difficult
        self.rate += self.last_change_rate
        self.count_diamonds += self.last_change_diamonds

    def loose_tracker(self, tracker):
        self.spree = 0
        self.last_change_rate = int(tracker.cost * 1.5)
        #self.rate -= self.last_change_rate

    def complete_tracker(self, tracker):
        self.spree += 5
        self.last_change_rate = int(tracker.cost)
        self.rate += self.last_change

    def is_has_diamond(self):
        return self.count_diamonds > 0
