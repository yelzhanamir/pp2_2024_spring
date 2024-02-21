import json 
file_path = r'C:\KBTU\json-data.py.json'
with open(file_path, 'r') as file:
    data = json.load(file)


interfaces = data['imdata']


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)


for interface in interfaces:
    attributes = interface['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))

