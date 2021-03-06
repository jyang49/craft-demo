import json
from random import *
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

for num in range(start, end):
    prefix = randint(1000, 9999)
    id = str(prefix) + '-' + str(num)

    data = {
        "id": id,
        "math": randint(50, 100),
        "physics": randint(50, 100)
    }
    json_str = json.dumps(data)

    #print('json_str: ' + json_str)
    #json_str = json.dumps(data, indent=2)

    file = id + '.txt'
    with open('out/' + file, 'w') as f:
        f.write(json_str)
