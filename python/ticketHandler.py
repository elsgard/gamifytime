
class TicketHandler:

    def __init__(self):
        self.nextId = 0
        self.tickets = []

    def createTicket(data):
        ticketTuple = jsonToTuple(data)
        ticket = Ticket(self.nextId, ticketTuple.name,
                    ticketTuple.totalPoints, ticketTuple.spentPoints)
        self.tickets.append(ticket)
        self.nextId = self.nextId +1
    def readticket(ticketId):
        for ticket in self.tickets:
            if ticket.id == ticketId:
                return ticket
        return None
    def updateticket(data):
        ticketTuple = jsonToTuple(data)
        for ticket in tickets:
            if ticket.id == ticketTuple.id:
                ticket.name = ticketTuple.name
                ticket.totalPoints = ticketTuple.totalPoints
                ticket.spentPoints
                return 1
        return None
    def deleteticket(ticketId):
        deleteId = -1
        for x in range(0,len(self.tickets)):
            if self.tickets[x].id == ticketId:
                deleteId = x
                break
        if deleteId > -1:
            return self.tickets.pop(deleteId)
        return None


    def jsonToTuple(self, data):
        x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return x
