import json

def create_character(data):
    return {
        "name": data["nome"],
        "health": data["vida"],
        "attack": data["ataque"],
        "class": data["classe"],
    }

def attack(attacker, defender):
    defender["health"] -= attacker["attack"]
    print(f"{attacker['name']} Ataca {defender['name']} e Causa {attacker['attack']} de Dano!")

def special(character, others):
    if character["class"] == "Guerreiro":
        target = others[0]  
        damage = character["attack"] + 15
        target["health"] -= damage
        print(f"{character['name']} usa Golpe Poderoso em {target['name']} e Causa {damage} de Dano!")
    elif character["class"] == "Mago":
        heal = 25
        character["health"] += heal
        print(f"{character['name']} usa Cura e Ganha {heal} Pontos de Vida!")
    elif character["class"] == "Arqueiro":
        damage = 15
        for enemy in others:
            if enemy != character:
                enemy["health"] -= damage
        print(f"{character['name']} usa Chuva de Flechas e Causa {damage} de Dano a Todos os Inimigos!")

def load_characters(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [create_character(entry) for entry in data]

def sort_characters_by_health(characters):
    return sorted(characters, key=lambda char: char["health"])

characters = load_characters('C:\\Users\\catia\\OneDrive\\Ambiente de Trabalho\\FPSemana06\\personagens.json')
print(f"{len(characters)} Personagens Entram em Batalha!")

characters = sort_characters_by_health(characters)

for char in characters:
    print(f"{char['name']} {char['health']}")

attack(characters[0], characters[1])
print(f"{characters[1]['name']} {characters[1]['health']}")

attack(characters[1], characters[2])
print(f"{characters[2]['name']} {characters[2]['health']}")

attack(characters[2], characters[0])
print(f"{characters[0]['name']} {characters[0]['health']}")

special(characters[0], characters[1:])
print(f"{characters[0]['name']} {characters[0]['health']}")

special(characters[1], characters)
for char in characters:
    print(f"{char['name']} {char['health']}")

special(characters[2], [characters[1]])
print(f"{characters[1]['name']} {characters[1]['health']}")
