import ledgerEntry as le
import ledger
import pointCalculator
import ticket
import user
import json
from collections import namedtuple
import userHandler

data = '{"name": "John Smith", "id": 1, "totalPoints": 0, "spentPoints":0}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

print x.name, x.id, x.totalPoints, x.spentPoints
