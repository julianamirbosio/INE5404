import customtkinter as ctk

minha_fonte = "noto sans"


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

print("Importação e configuração inicial realizadas")


class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()
        print("Janela iniciada")
        self.geometry("500x300")
        self.configure(fg_color="#ffffff")
