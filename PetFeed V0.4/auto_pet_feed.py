from alimentar_pet import BotPet
from pet_selector import load_pet_id
import time

def start_pet_feed():
    # Pergunta qual pet escolher aqui dentro
    escolha = escolher_pet()

    bot = BotPet(load_pet_id(escolha))

    print("Iniciando...")
    while True:
        time.sleep(5)
        if bot.fullxp():
            print("XP cheio, saindo do loop...")
            break
        bot.alimentar_pet()
        print("Recomeçando...")

    print('Bot pausado')

def escolher_pet():
    import questionary
    escolha = questionary.select(
        "Selecione o pet:",
        choices=[
            {"name": "🐯 Tigre", "value": "tiger"},
            {"name": "🐉 Dragão", "value": "dragon"},
            {"name": "🦄 Unicórnio", "value": "unicorn"},
            {"name": "🦁 Leão", "value": "lion"},
            {"name": "🐰 Coelho", "value": "rabbit"},
            {"name": "🦅 Grifo", "value": "griff"},
            {"name": "🦊 Raposa", "value": "fox"}
        ]
    ).ask()

    if escolha is None:
        print("Seleção cancelada pelo usuário.")
        import sys
        sys.exit()

    return escolha
