import win32gui
import win32con
import time
import pyautogui
import ctypes

def build_lparam(key, is_keyup=False, repeat_count=1):
    # Get scan code da tecla virtual (VK)
    scan_code = ctypes.windll.user32.MapVirtualKeyW(key, 0)

    # Flags
    extended = 0
    context_code = 0
    previous_state = 0
    transition_state = 0

    if is_keyup:
        transition_state = 1
        previous_state = 1

    lparam = (repeat_count & 0xFFFF)           # repeat count (16 bits)
    lparam |= (scan_code << 16)                # scan code (bits 16-23)
    lparam |= (extended << 24)                  # extended key flag (bit 24)
    lparam |= (context_code << 29)              # context code (bit 29)
    lparam |= (previous_state << 30)            # previous key state (bit 30)
    lparam |= (transition_state << 31)          # transition state (bit 31)

    return lparam

def encontrar_imagem(caminho_imagem, confidence=0.7):
    try:
        pos = pyautogui.locateOnScreen(caminho_imagem, confidence=confidence)
        if pos:
            return True
        return False
    except pyautogui.ImageNotFoundException:
        return False

# Enviar tecla global (para janela em foco)
def pressionar_tecla(vk):
    ctypes.windll.user32.keybd_event(vk, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(vk, 0, 2, 0)

# Enviar tecla para janela específica (via hwnd)
def enviar_tecla_para_janela(hwnd, tecla):
    lparam_down = build_lparam(tecla, is_keyup=False)
    lparam_up = build_lparam(tecla, is_keyup=True)

    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, tecla, lparam_down)
    time.sleep(0.05)  # tempo de tecla pressionada
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, tecla, lparam_up)