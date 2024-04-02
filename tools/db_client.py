import sqlite3 as sl
from datetime import datetime, timedelta
from random import randint

from objects.task import Task
from objects.user import User


class DbClient:
    def __init__(self):
        self.con = sl.connect('game.db')

    def get_tasks(self):
        cur = self.con.cursor()
        cur.execute(f"SELECT id, name, time, type_schedule, type_notification FROM tasks WHERE status=0")
        tasks = []
        for row in cur.fetchall():
            id = row[0]
            name = row[1]
            time = datetime.strptime(row[2], '%Y-%m-%d %H:%M')
            type_schedule = row[3]
            type_notification = row[4]
            tasks.append(Task(id, name,  time,  type_notification,type_schedule, 1))

        return tasks

    def add_new_task(self, task):
        task.datetime = (task.datetime-timedelta(hours=3)).strftime('%Y-%m-%d %H:%M')

        sql = (
            f'INSERT INTO tasks (name, time, type_schedule, type_notification, difficult) VALUES ("{task.name}", "{task.datetime}", '
            f'{task.type_schedule}, {task.time_notification}, {task.difficult})')

        self.con.execute(sql)
        self.con.commit()

    def add_new_user(self, user):
        sql = f'INSERT INTO players (name, login) VALUES ("{user.name}", "{user.login}")'

        self.con.execute(sql)
        self.con.commit()

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


    def update_user(self, user):
        cur = self.con.cursor()
        sql = f"UPDATE players SET spree={user.spree}, rate={user.rate} WHERE login='{user.login}'"
        cur.execute(sql)
        self.con.commit()

    def update_task(self, tasks):
        for task in tasks:
            cur = self.con.cursor()
            sql = f"UPDATE tasks SET status={task.status} WHERE id='{task.id}'"
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
