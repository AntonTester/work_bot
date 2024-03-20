from pymongo import MongoClient

from games_object.color_profile import ColorProfile
from games_object.rate import Rating


class JsonTools:
    @staticmethod
    def color_player_to_json(player):
        return {
            "uid": player.uid,
            "name": player.name,
            "rating": {
                "mmr": player.rating.mmr
            },
        }

    @staticmethod
    def json_to_color_player(json):
        player = ColorProfile(json["uid"], json["name"], 3)
        player.rating = Rating(json["rating"]["mmr"])
        return player


