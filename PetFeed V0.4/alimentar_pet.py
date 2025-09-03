import windowsAPI
import traceback
import time

class BotPet:
    def __init__(self, pet_img: str):
        self.petfeed_img = 'assets/flyff/petfeed.png'
        self.pet_img = f'assets/flyff/{pet_img}.png'
        self.fullxp_img = 'assets/flyff/fullxp.png'
        self.pet_equipado = self.verificar_pet_equipado()  # Verifica logo no início
        self.VK_3 = 0x33  # Tecla '3'
        self.VK_5 = 0x35  # Tecla '5'

    def verificar_pet_equipado(self):
        return windowsAPI.encontrar_imagem(self.pet_img) is not None

    def toggle_pet(self):
        print('Equipando/Desequipando Pet')
        windowsAPI.pressionar_tecla(self.VK_5)
        self.pet_equipado = not self.pet_equipado
        time.sleep(2)

    def pet_is_equiped(self):
        if not windowsAPI.encontrar_imagem(self.pet_img):
            print('Pet estava desequipado...')
            self.toggle_pet()
            time.sleep(2)
        else:
            print('Pet já está equipado')

    def fullxp(self):
        if windowsAPI.encontrar_imagem(self.fullxp_img, confidence=0.97):
            print('XP do pet chegou a 99.99%. Encerrando alimentação')
            self.toggle_pet()
            return True
        return False

    def alimentar_pet(self):
        try:
            if windowsAPI.encontrar_imagem(self.petfeed_img):
                self.pet_is_equiped()
                print("Petfeed encontrado. Alimentando o pet...")
                windowsAPI.pressionar_tecla(self.VK_3)
            else:
                if windowsAPI.encontrar_imagem(self.pet_img):
                    print("Petfeed não encontrado. Desequipando pet...")
                    self.toggle_pet()
                else:
                    print("Petfeed não encontrado. (Pet já está desequipado)")
        except Exception as e:
            traceback.print_exc()