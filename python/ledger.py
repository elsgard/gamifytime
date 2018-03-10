
class Ledger:
    entries = []
    def __init__(self):
        self.entries = []


    def getHoursForUserAndDay(self, userId, day):

        totalHours = 0

        for entry in self.entries:
            if entry.userId == userId and entry.date == today:
                totalHours = totalHours + entry.hours_logged
        return totalHours
