import threading
import keyboard

def iniciar_thread_hotkey(callback):
    def escutar_hotkey():
        while True:
            keyboard.wait('num 5')
            callback()

    thread = threading.Thread(target=escutar_hotkey, daemon=True)
    thread.start()
