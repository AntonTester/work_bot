from enum import Enum


class TypeNotification(Enum):
    OFTEN = 1
    AVERAGE = 5
    RARELY = 30

class TypeSchedule(Enum):
    EVERYDAY = 0
    ONCE = 1
