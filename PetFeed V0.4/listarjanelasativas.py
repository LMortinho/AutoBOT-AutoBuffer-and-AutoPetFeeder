import win32gui
import questionary

class ListarJanelasAtivasClass:
    @staticmethod
    def listar_janelas_ativas():
        janelas = []

        def callback(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd):
                titulo = win32gui.GetWindowText(hwnd)
                if titulo:
                    janelas.append((titulo, hwnd))

        win32gui.EnumWindows(callback, None)
        return janelas

    @staticmethod
    def escolher_janela():
        janelas = ListarJanelasAtivasClass.listar_janelas_ativas()
        if not janelas:
            print("Nenhuma janela ativa encontrada.")
            return None

        escolhas = [{"name": titulo, "value": hwnd} for titulo, hwnd in janelas]
        hwnd_escolhido = questionary.select(
            "Selecione a janela para usar o Auto Healer:",
            choices=escolhas
        ).ask()

        return hwnd_escolhido
