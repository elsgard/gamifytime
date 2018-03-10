import json

class Log:

    def __init__(self, id, userId, ticketId, hoursLogged, description, date):
        self.id = id
        self.userId = user_id
        self.ticketId = ticketId
        self.hoursLogged = hoursLogged
        self.description = description
        self.date = date

    def toJSON(self):
        return json.dumps(self.__dict__)
