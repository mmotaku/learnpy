import json

f = open('sample.json')
sample = f.read()
f.close()

print(sample)
super_heroes = json.loads(sample)

print(super_heroes['active'])
print(super_heroes['members'][1]['powers'][2])
