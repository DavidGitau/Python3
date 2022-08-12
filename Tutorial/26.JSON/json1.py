import json

# Storing data in a file
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

with open('txt1', 'w') as f:
    json.dump(d, f)

# Retreiving data from a file 
with open('txt1', 'r') as f:
    d = json.load(f)
    print(d)
    print(json.dumps(d,indent=2))