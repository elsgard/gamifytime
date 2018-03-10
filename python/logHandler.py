
class LogHandler:

    def __init__(self):
        self.nextId = 0
        self.logs = []

    def createLog(data):
        logTuple = jsonToTuple(data)
        log = Log(self.nextId, logTuple.userId,
                    logTuple.ticketId, logTuple.hoursLogged, logTuple.description, logTuple.date)
        self.logs.append(log)
        self.nextId = self.nextId +1
    def readLog(logId):
        for log in self.logs:
            if log.id == logId:
                return log
        return None
    def updateLog(data):
        logTuple = jsonToTuple(data)
        for log in logs:
            if log.id == logTuple.id:
                log.userId = logTuple.userId
                log.ticketId = logTuple.ticketId
                log.hoursLogged = logTuple.hoursLogged
                log.description = logTuple.description
                log.date = logTuple.date
                return 1
        return None
    def deleteLog(logId):
        deleteId = -1
        for x in range(0,len(self.logs)):
            if self.logs[x].id == logId:
                deleteId = x
                break
        if deleteId > -1:
            return self.logs.pop(deleteId)
        return None


    def jsonToTuple(self, data):
        x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return x

    def getHoursForUserAndDay(self, userId, day):

        totalHours = 0

        for entry in self.entries:
            if entry.userId == userId and entry.date == today:
                totalHours = totalHours + entry.hours_logged
        return totalHours
