import json

class Ticket:

    def __init__(self, id, name, description, totalHours):
        self.id = id
        self.name = name
        self.description = description
        self.totalHours = totalHours
        self.remainingHours = totalHours

    def toJSON(self):
        return json.dumps(self.__dict__)
