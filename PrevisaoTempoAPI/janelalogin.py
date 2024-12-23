import customtkinter as ctk
from PIL import Image
from janela import Janela, minha_fonte
from janelaprincipal import JanelaPrincipal


class JanelaLogin(Janela):
    def __init__(self):
        super().__init__()
        print("JanelaLogin iniciada")
        self.title("Login")

        self.background_image = Image.open("ceu.jpg")
        self.bg_image = ctk.CTkImage(light_image=self.background_image, size=(500, 300))
        self.background_label = ctk.CTkLabel(self, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(master=self, fg_color="#c1e8ff", border_width=30, border_color="#c1e8ff",
                                  corner_radius=0)
        self.frame.pack(padx=150, pady=40, fill="both", expand=True)

        self.texto = ctk.CTkLabel(master=self.frame, text="ClimaTempo", font=(minha_fonte, 20, "bold"))
        self.texto.pack(padx=10, pady=10)

        self.user = ctk.CTkEntry(master=self.frame, placeholder_text="Usuário", font=(minha_fonte, 12),
                                 border_color="white")
        self.user.pack(padx=20, pady=10)

        self.senha = ctk.CTkEntry(master=self.frame, placeholder_text="Senha", show="*", font=(minha_fonte, 12),
                                  border_color="white")
        self.senha.pack(padx=10, pady=10)

        # checkbox = ctk.CTkCheckBox(self, text="Lembrar login")
        # checkbox.place(padx=10, pady=10)

        self.botao = ctk.CTkButton(master=self.frame, text="Login", command=self.clique, corner_radius=32,
                                   fg_color="#023047", font=(minha_fonte, 13, "bold"))
        self.botao.pack(padx=10, pady=20)

        self.mensagem = ctk.CTkLabel(self, text="", font=(minha_fonte, 12))
        self.mensagem.pack()

    def clique(self):
        print("Fazer Login")
        user = self.user.get()
        senha = self.senha.get()

        with open("credenciais.txt", "r") as file:
            for line in file:
                dados_usuario = line.strip().split(",")
                if dados_usuario[0] == user and dados_usuario[1] == senha:
                    self.mensagem.configure(text="Login bem-sucedido!")

                    # Fecha a janela de Login
                    self.destroy()

                    # Abre uma nova janela principal
                    janelaprincipal = JanelaPrincipal()
                    janelaprincipal.mainloop()
                    break
            else:
                self.mensagem.configure(text="Credenciais inválidas.")
