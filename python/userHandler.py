
class UserHandler:

    def __init__(self):
        self.nextId = 0
        self.users = []

    def createUser(data):
        userTuple = jsonToTuple(data)
        user = User(self.nextId, userTuple.name,
                    userTuple.totalPoints, userTuple.spentPoints)
        self.users.append(user)
        self.nextId = self.nextId +1
    def readUser(userId):
        for user in self.users:
            if user.id == userId:
                return user
        return None
    def updateUser(data):
        userTuple = jsonToTuple(data)
        for user in users:
            if user.id == userTuple.id:
                user.name = userTuple.name
                user.totalPoints = userTuple.totalPoints
                user.spentPoints
                return 1
        return None
    def deleteUser(UserId):
        deleteId = -1
        for x in range(0,len(self.users)):
            if self.users[x].id == userId:
                deleteId = x
                break
        if deleteId > -1:
            return self.users.pop(deleteId)
        return None


    def jsonToTuple(self, data):
        x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return x
