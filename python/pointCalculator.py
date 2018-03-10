import ledger
import datetime

class PointCalculator:

    def __init__(self):
        self.ledger = ledger.Ledger()

    def calculatePointsForDay(userId):
        points = 0
        today = datetime.date.today()
        hours = ledger.getHoursForUserAndDay(userId, today)
        multiplier, bonus = getCurrentMultiplierAndBonusForUser(userId)

        points = hours
        points = round(points*bonus)
        points = points*multiplier
        return points

    def getCurrentMultiplierForUser(userId):
        nrOfDays = 0;

        date = datetime.date.today();
        hours = ledger.getHoursForUserAndDay(userId, date)
        while hours >= 8:
            nrOfDays = nrOfDays +1
            date = date - timedelta(days=1)
            hours = ledger.getHoursForUserAndDay(userId, date)

        if nrOfDays == 0:
            return 1,1
        elif nrOfDays >=1 and nrOfDays < 5:
            return 1,1.1
        elif nrOfDays >=5 and nrOfDays < 15:
            return 2,1.25
        else:
            return 4,2
