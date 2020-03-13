#!/usr/bin/env python3
import json
import pprint

data = {
    'name': 'KGHM',
    'cena': 200,
    'ilosc': 10,
    'na_parkiecie': True,
    'wlasciciel': None
}

json_str = json.dumps(data)
print(json_str)

data1 = json.loads(json_str)
pprint.pprint(data1, indent=4, width=20)

l = [1, 2, 3, 4]
#l.append(l)
pprint.pprint(l)
l_json = json.dumps(l)

with open('json_data.json', 'rb') as f:
    data3 = json.load(f)

print(data3)

class JClass:
    def __init__(self):
        self._name = 'JClass'
        self._count = 4444

    def jrestore(self, data):
        self.__dict__ = data

    def jsave(self):
        return json.dumps(self.__dict__)

jo = JClass()
print(jo.jsave())
