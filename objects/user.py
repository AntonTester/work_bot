import datetime


class User:
    def __init__(self,  login, name, rate, spree):
        self.name = name
        self.login = login
        self.rate = rate
        self.spree = spree
        self.last_change = 0

    def loose_task(self):
        print(self.rate)
        self.last_change = int(10 * (1 + self.spree/4))
        self.rate -= self.last_change
        self.spree = 0
        print(self.rate)

    def complete_task(self, task):
        self.spree += task.difficult
        if self.spree > 20:
            self.spree = 20
        self.last_change = int(10 * (1 + (task.difficult * (self.spree/20))))
        self.rate += self.last_change

    def loose_tracker(self, tracker):
        self.spree = 0
        self.last_change = int(tracker.cost*1.5)
        self.rate += self.last_change
    def complete_tracker(self, tracker):
        self.spree += 5
        self.last_change = int(tracker.cost)
        self.rate += self.last_change

