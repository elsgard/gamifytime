import logHandler
import log
import ticket
import ticketHandler
import user
import userHandler

import pointCalculator

import json
from collections import namedtuple

data = '{"name": "John Smith", "id": 1, "totalPoints": 0, "spentPoints":0}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

print x.name, x.id, x.totalPoints, x.spentPoints
