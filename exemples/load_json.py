import pprint
import json

with open('json.json') as f:
  data = json.load(f)

print(data)
pprint.pprint(data)