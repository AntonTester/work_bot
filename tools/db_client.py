import sqlite3 as sl
from datetime import datetime, timedelta
from random import randint

from objects import task
from objects.task import Task
from objects.tracker import Tracker
from objects.user import User
from tools.task_tools import TaskTools


class DbClient:
    def __init__(self):
        self.con = sl.connect('game.db')

    def get_tasks(self):
        cur = self.con.cursor()
        cur.execute(f"SELECT id, name, time, type_schedule, type_notification, last_completed FROM tasks WHERE status=0")
        tasks = []
        for row in cur.fetchall():
            id = row[0]
            name = row[1]
            time = datetime.strptime(row[2], '%Y-%m-%d %H:%M')
            type_schedule = row[3]
            type_notification = row[4]
            last_completed = datetime.strptime(row[5], '%Y-%m-%d %H:%M')
            tasks.append(Task(id, name,  time,  type_notification,type_schedule, 1, last_completed))

        return tasks

    def get_trackers(self):
        cur = self.con.cursor()
        cur.execute(f"SELECT id, name, name_time, cost, max_count, count, date_create FROM trackers")
        tasks = []
        for row in cur.fetchall():
            id = row[0]
            name = row[1]
            name_time = row[2]
            cost = int(row[3])
            max_count = int(row[4])
            count = int(row[5])
            time = datetime.strptime(row[6], '%Y-%m-%d %H:%M')
            tasks.append(Tracker(id, name,  name_time,  cost, max_count, count, time))

        return list(filter(lambda i: not i.is_completed(), tasks))

    def get_rating(self, id):
        cur = self.con.cursor()
        cur.execute(f"SELECT sum(estimate) FROM votes WHERE hotel_id={id}")
        row = cur.fetchall()[0]

        return int(row[0])

    def get_user(self, login):
        cur = self.con.cursor()
        cur.execute(f"SELECT name, login, spree, rate FROM players WHERE login='{login}'")
        row = cur.fetchall()[0]
        name = row[0]
        login = row[1]
        spree = row[2]
        rate = row[3]

        return User(login, name, rate, spree)

    def add_new_task(self, task):
        last_completed = TaskTools.get_str_time(datetime.now()
                                                .replace(hour=task.datetime.hour, minute=task.datetime.minute))
        time = TaskTools.get_str_time(task.datetime)
        sql = (
            f'INSERT INTO tasks (name, time, type_schedule, type_notification, difficult, last_completed) VALUES '
            f'("{task.name}", "{time}", {task.type_schedule}, {task.time_notification}, {task.difficult}, "{last_completed}")')

        self.con.execute(sql)
        self.con.commit()

    def add_new_tracker(self, tracker):
        time = TaskTools.get_str_time(tracker.date_create)
        sql = (
            f'INSERT INTO trackers (name, name_time, cost, max_count, date_create) VALUES '
            f'("{tracker.name}", "{tracker.name_time}", {tracker.cost}, {tracker.max_count}, "{time}")')

        self.con.execute(sql)
        self.con.commit()

    def add_new_user(self, user):
        sql = f'INSERT INTO players (name, login) VALUES ("{user.name}", "{user.login}")'

        self.con.execute(sql)
        self.con.commit()



    def update_user(self, user):
        cur = self.con.cursor()
        sql = f"UPDATE players SET spree={user.spree}, rate={user.rate} WHERE login='{user.login}'"
        cur.execute(sql)
        self.con.commit()

    def update_tracker(self, trackers):
        for tracker in trackers:
            cur = self.con.cursor()
            sql = f"UPDATE trackers SET count={tracker.count} WHERE id='{tracker.id}'"
            cur.execute(sql)
            self.con.commit()

    def update_task(self, tasks):
        for task in tasks:
            cur = self.con.cursor()
            sql = (f"UPDATE tasks SET status={task.status}, last_completed='{TaskTools.get_str_time(task.last_completed)}' "
                   f"WHERE id='{task.id}'")
            cur.execute(sql)
            self.con.commit()

    def check_user(self, id, name):
        cur = self.con.cursor()
        sql = f"SELECT * FROM players WHERE login='{id}'"
        cur.execute(sql)
        count = len(cur.fetchall())
        rows = cur.fetchall()
        if count == 0:
            self.add_new_user(User(id, name))
