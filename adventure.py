import sys
import json
from description import *

if len(sys.argv) < 2:
    print("Please provide a filename")
    sys.exit()

filename = sys.argv[1]

# Open the JSON file
with open(filename) as f:
    # Load the data from the file using the `load()` method
    map_data = json.load(f)
    
print(WELCOME)

print(map_data[0]["name"])

