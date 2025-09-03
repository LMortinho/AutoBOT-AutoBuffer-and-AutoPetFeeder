from thread_hotkey import iniciar_thread_hotkey
from windowsAPI import enviar_tecla_para_janela
from listarjanelasativas import ListarJanelasAtivasClass
import json
import time

buff_hotkey_pressed = False
buff_em_execucao = False

def on_hotkey_pressed():
    global buff_hotkey_pressed, buff_em_execucao
    if buff_em_execucao:
        print("Buffs em execução, aguarde...")
    else:
        print("Hotkey Numpad 5 pressionada!")
        buff_hotkey_pressed = True

def AutoBuffs(hwnd):
    global buff_em_execucao
    buff_em_execucao = True

    print("Executando AutoBuffs...")

    try:
        with open("json/buffs.json", "r", encoding="utf-8") as f:
            buffs_por_barra = json.load(f)

        for barra, buffs in buffs_por_barra.items():
            if not buffs:
                continue

            codigo_barra = 0x70 + (int(barra[1:]) - 1)
            enviar_tecla_para_janela(hwnd, codigo_barra)
            time.sleep(0.5)

            for buff in buffs:
                tecla = buff["key"]
                enviar_tecla_para_janela(hwnd, ord(tecla))
                print(f"Buff: {buff['skill']} (tecla {tecla}) enviado.")
                time.sleep(1.8)

    except Exception as e:
        print(f"Erro ao executar buffs: {e}")

    print("Buffs concluídos.")
    buff_em_execucao = False

def botHealer():
    global buff_hotkey_pressed

    hwnd = ListarJanelasAtivasClass.escolher_janela()
    if hwnd is None:
        print("Nenhuma janela foi selecionada.")
        return

    iniciar_thread_hotkey(on_hotkey_pressed)

    print("Janela selecionada. Iniciando heal...")

    try:
        while True:
            if buff_hotkey_pressed:
                AutoBuffs(hwnd)
                buff_hotkey_pressed = False
                print("Voltando ao heal...")

            enviar_tecla_para_janela(hwnd, 0x31)  # tecla '1'
            print("Tecla '1' enviada.")
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("Auto Healer pausado pelo usuário.")

def start_auto_healer():
    botHealer()
