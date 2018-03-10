import json

class LedgerEntry:

    def __init__(self, id, user_id, hours_logged, description, date):
        self.id = id
        self.user_id = user_id
        self.hours_logged = hours_logged
        self.description = description
        self.date = date

    def toJSON(self):
        return json.dumps(self.__dict__)
