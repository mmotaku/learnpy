import json

f = open('sample.json')
sample = f.read()
f.close()

print(sample)
super_heroes = json.loads(sample)

print(super_heroes['secretBase'])
print(super_heroes['members'][2]['powers'][3])

sum = super_heroes['members'][0]['age'] + super_heroes['members'][1][
    'age'] + super_heroes['members'][2]['age']
print(sum)
