import json

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.totalPoints = 0
        self.spentPoints = 0

    def toJSON(self):
        return json.dumps(self.__dict__())
