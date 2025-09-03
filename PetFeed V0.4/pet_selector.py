import json

def load_pet_id(pet_id):
    with open('json/pets.json', 'r', encoding='utf-8') as f:
        pets = json.load(f)

    if pet_id not in pets:
        raise ValueError(f"Pet '{pet_id}' não encontrado no arquivo!")

    return pets[pet_id]['img']
