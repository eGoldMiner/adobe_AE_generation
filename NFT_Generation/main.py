import json
from random import randint
import random

'''
#   1 miner format JSON

{
    "id": 1,
    "assets_name": ["Elrond Crown", "T1_red", "Aviator", "Red", "Green shirt", "Storm", "Jewelry"],
    "surname": ["crown", "T1_re", "aviator", "red", "green_shirt", "storm", "jewelry"],
}

'''

def create_json(id, assets, filename, coordinates):
    json.dumps()

def get_rnd(asset):
    return random.choices(asset['list'], asset['weights'])

file = open('assets.json')
data = json.load(file)
data_helmet = data['layers'][0]
data_beard = data['layers'][1]
data_eyes = data['layers'][2]
data_pickaxes = data['layers'][3]
data_clothes = data['layers'][4]
data_background = data['layers'][5]
data_accessories = data['layers'][6]


#creation de nos 3 NFTs custom manuellement
# 4 à 203       private sale, pickaxe rare
# 204 à 7000    public sale

index_pierres = 0
id_pierres = [random.randint(0,6997), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000), 
    random.randint(0,7000)]


#private sale
id = 0
all_miners = []
for i in range(6997):
    helmet = get_rnd(data_helmet)[0]
    beard = get_rnd(data_beard)[0]
    eyes = get_rnd(data_eyes)[0]
    if id < 200:
        pickaxe = 0
    else:
        pickaxe = get_rnd(data_pickaxes)[0]
    clothes = get_rnd(data_clothes)[0]
    background = get_rnd(data_background)[0]
    accessory = get_rnd(data_accessories)[0]

    if id in id_pierres:
        accessory = index_pierres + 6
        index_pierres = index_pierres + 1
        id_pierres.remove(id)

    assets_name = [data_helmet['values'][helmet], 
            data_beard['values'][beard],
            data_eyes['values'][eyes],
            data_pickaxes['values'][pickaxe],
            data_clothes['values'][clothes],
            data_background['values'][background],
            data_accessories['values'][accessory]]

    filename = [data_helmet['surname'][helmet], 
            data_beard['surname'][beard],
            data_eyes['surname'][eyes],
            data_pickaxes['surname'][pickaxe],
            data_clothes['surname'][clothes],
            data_background['surname'][background],
            data_accessories['surname'][accessory]]


    # Serializing json
    all_miners.append({"id":id, "assets":assets_name, "surname":filename})
    # json_object = json.dumps({"Miners": {"id":id, "assets":assets_name, "files":filename, "coordinates":coordinates}}, indent = 4)

    id = id + 1


with open('data.json', 'w') as outfile:
    json.dump(all_miners, outfile, indent=4)