import ctypes
import random

from enums.type_fields import TypeArea
from objects.house import House
from objects.map_cell import MapCell

from tools.strings import HouseNames


class Config:

    cells = [
        MapCell(House(HouseNames.START, TypeArea.START), is_system=True),
        MapCell(House(HouseNames.BAR_1, TypeArea.BAR, 60, 2, 50)),
        MapCell(House(HouseNames.TREASURE, TypeArea.TREASURE), is_system=True),
        MapCell(House(HouseNames.BAR_2, TypeArea.BAR, 100, 4, 50)),
        MapCell(House(HouseNames.TAX, TypeArea.TAX), is_system=True),
        MapCell(House(HouseNames.TRANSPORT_1, TypeArea.TRANSPORT, 200, 25, 0)),
        MapCell(House(HouseNames.FOOD_1, TypeArea.FOOD, 100, 6, 50)),
        MapCell(House(HouseNames.CHANCE, TypeArea.CHANCE), is_system=True),
        MapCell(House(HouseNames.FOOD_2, TypeArea.FOOD, 100, 6, 50)),
        MapCell(House(HouseNames.FOOD_3, TypeArea.FOOD, 120, 8, 50)),

        MapCell(House(HouseNames.PRISON, TypeArea.PRISON), is_system=True),
        MapCell(House(HouseNames.STUDY_1, TypeArea.STUDY, 140, 10, 100)),
        MapCell(House(HouseNames.SERVICE_1, TypeArea.SERVICE, 150, 1, 0)),
        MapCell(House(HouseNames.STUDY_2, TypeArea.STUDY, 140, 10, 100)),
        MapCell(House(HouseNames.STUDY_3, TypeArea.STUDY, 160, 12, 100)),
        MapCell(House(HouseNames.TRANSPORT_2, TypeArea.TRANSPORT, 200, 25, 0)),
        MapCell(House(HouseNames.REST_1, TypeArea.REST, 180, 14, 100)),
        MapCell(House(HouseNames.TREASURE, TypeArea.TREASURE), is_system=True),
        MapCell(House(HouseNames.REST_2, TypeArea.REST, 180, 14, 100)),
        MapCell(House(HouseNames.REST_3, TypeArea.REST, 200, 16, 100)),

        MapCell(House(HouseNames.PARKING, TypeArea.PARKING), is_system=True),
        MapCell(House(HouseNames.SEX_1, TypeArea.SEX, 220, 18, 150)),
        MapCell(House(HouseNames.CHANCE, TypeArea.CHANCE), is_system=True),
        MapCell(House(HouseNames.SEX_2, TypeArea.SEX, 220, 18, 150)),
        MapCell(House(HouseNames.SEX_3, TypeArea.SEX, 240, 20, 150)),
        MapCell(House(HouseNames.TRANSPORT_3, TypeArea.TRANSPORT, 200, 25, 0)),
        MapCell(House(HouseNames.SPORT_1, TypeArea.SPORT, 260, 22, 150)),
        MapCell(House(HouseNames.SPORT_2, TypeArea.SPORT, 260, 22, 150)),
        MapCell(House(HouseNames.SERVICE_2, TypeArea.SERVICE, 150, 1, 0)),
        MapCell(House(HouseNames.SPORT_3, TypeArea.SPORT, 280, 24, 150)),

        MapCell(House(HouseNames.ARREST, TypeArea.ARREST), is_system=True),
        MapCell(House(HouseNames.OFFICE_1, TypeArea.OFFICE, 300, 26, 200)),
        MapCell(House(HouseNames.OFFICE_2, TypeArea.OFFICE, 300, 26, 200)),
        MapCell(House(HouseNames.TREASURE, TypeArea.TREASURE), is_system=True),
        MapCell(House(HouseNames.OFFICE_3, TypeArea.OFFICE, 320, 28, 200)),
        MapCell(House(HouseNames.TRANSPORT_4, TypeArea.TRANSPORT, 200, 25, 0)),
        MapCell(House(HouseNames.CHANCE, TypeArea.CHANCE), is_system=True),
        MapCell(House(HouseNames.ELITE_1, TypeArea.ELITE, 350, 35, 200)),
        MapCell(House(HouseNames.PAY, TypeArea.PAY), is_system=True),
        MapCell(House(HouseNames.ELITE_2, TypeArea.ELITE, 400, 50, 200)),

    ]


