from enum import Enum


class TypeSchedule(Enum):
    ONCE = 0
    EVERYDAY_1 = 1
    EVERYDAY_2 = 2
    EVERYDAY_3 = 3
    EVERYDAY_4 = 4
    WORK = 5

class Status(Enum):
    CREATE = 'create'
    TIME = 'time'
    DATE = 'date'
    NOTIFICATION = 'notification'
    SCHEDULE = 'schedule'
    DIFFICULTY = 'difficulty'
