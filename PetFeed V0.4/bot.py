import questionary
import os
import sys
from auto_pet_feed import start_pet_feed
from healer import start_auto_healer
from configs import start_configs

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    limpar_console()
    escolha = questionary.select(
        "Selecione o menu:",
        choices=["Auto Pet Feed", "Auto Healer", "Configs"]
    ).ask()

    if escolha is None:
        print("Operação cancelada pelo usuário.")
        sys.exit()

    if escolha == "Auto Pet Feed":
        start_pet_feed()
    elif escolha == "Auto Healer":
        start_auto_healer()
    elif escolha == "Configs":
        start_configs()

start()
