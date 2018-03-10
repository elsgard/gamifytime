import json

class Ticket:

    def __init__(self, id, name, description, totalHours):
        self.id = id
        self.name = name
        self.description = description
        self.estimatedHours = estimatedHours
        self.spentHours = 0

    def toJSON(self):
        return json.dumps(self.__dict__)
