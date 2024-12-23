import customtkinter as ctk
from WeatherAPI import TempoInfo
from janela import Janela, minha_fonte
from datetime import datetime

lupa = "\U0001F50D"
marcador_local = "\U0001F4CD"
# Símbolos Unicode para o clima
nuvem = "\u2601"
chuva = "\U0001F327"
sol = "\u2600"
nuvem_com_sol = "\u26C5"
neve = "\U0001F328"
vento = "\U0001F32C"
tempestade = "\U0001F329"
raio = "\u26A1"

class JanelaPrincipal(Janela):
    def __init__(self):
        super().__init__()
        print("Janela Principal iniciada")
        self.title("ClimaTempo")

        # Configurando os widgets
        self.cidade = ctk.CTkEntry(self, placeholder_text="Insira aqui uma cidade!", width=365, height=24,
                                   corner_radius=12, font=(minha_fonte, 12), fg_color="#d9d9d9",
                                   border_color="#d9d9d9",text_color="#4f4d4d")
        self.cidade.place(x=22, y=12)

        self.data_inicio_label = ctk.CTkLabel(self, text="Data Início:",  width=80, height=15,
                                              font=(minha_fonte, 12, "bold"), text_color="#393939")
        self.data_inicio_label.place(x=24, y=42)

        self.data_fim_label = ctk.CTkLabel(self, text="Data Fim:", width=80, height=15,
                                           font=(minha_fonte, 12, "bold"),text_color="#393939")
        self.data_fim_label.place(x=225, y=42)

        self.data_inicio = ctk.CTkEntry(self, placeholder_text="DD/MM/AAAA",  width=165, height=24,
                                        corner_radius=12, fg_color="#d9d9d9", border_color="#d9d9d9",
                                        text_color="#4f4d4d")
        self.data_inicio.place(x=22, y=62)

        self.data_fim = ctk.CTkEntry(self, placeholder_text="DD/MM/AAAA", width=165, height=24,
                                     corner_radius=12, fg_color="#d9d9d9", border_color="#d9d9d9",
                                     text_color="#4f4d4d")
        self.data_fim.place(x=222, y=62)

        self.botao = ctk.CTkButton(self, text=lupa, font=(minha_fonte, 25), command=self.buscar_cidade,
                                   corner_radius=25, width=20,
                                   height=74, fg_color="#023047")
        self.botao.place(x=402, y=12)

        # Área para exibir os resultados
        self.resultados_frame = ctk.CTkFrame(self, width=454, height=194, corner_radius=10, fg_color="#d9d9d9",
                                             border_color="#d9d9d9")

        self.mensagem = ctk.CTkLabel(self, text="", font=(minha_fonte, 14))
        self.mensagem.place(x=88, y=185)

        self.cidade_nome_label = ctk.CTkLabel(self.resultados_frame, text="",
                                              font=(minha_fonte, 36))
        self.cidade_nome_label.place(x=59, y=13)

        self.temperatura_label = ctk.CTkLabel(self.resultados_frame, text="",
                                              font=(minha_fonte, 40))
        self.temperatura_label.place(x=299, y=18)

        self.previsao_label = ctk.CTkLabel(self.resultados_frame, text="",
                                           font=(minha_fonte, 20))
        self.previsao_label.place(x=59, y=54)

        self.sensacao_label = ctk.CTkLabel(self.resultados_frame, text="",
                                           font=(minha_fonte, 20))
        self.sensacao_label.place(x=32, y=97)

        self.maxmin_label = ctk.CTkLabel(self.resultados_frame, text="",
                                           font=(minha_fonte, 20))
        self.maxmin_label.place(x=32, y=121)

        self.umidade_label = ctk.CTkLabel(self.resultados_frame, text="",
                                          font=(minha_fonte, 16))
        self.umidade_label.place(x=32, y=143)

        self.marcador = ctk.CTkLabel(self.resultados_frame, text=marcador_local,
                                     font=(minha_fonte, 35))
        self.clima = ctk.CTkLabel(self.resultados_frame, text="",
                                     font=(minha_fonte, 96))
        self.clima.place(x=309, y=64)

    def buscar_cidade(self):
        cidade = self.cidade.get()
        data_inicio = self.data_inicio.get()
        data_fim = self.data_fim.get()

        # Processar as datas
        try:
            data_inicio_formatada = datetime.strptime(data_inicio, '%d/%m/%Y')
            data_fim_formatada = datetime.strptime(data_fim, '%d/%m/%Y')
        except ValueError:
            self.mensagem.configure(text="Formato de data inválido!")
            return

        procura = TempoInfo(cidade)
        dados = procura.requisicao()

        if dados:
            try:
                self.mensagem.destroy()
                self.resultados_frame.place(x=24, y=112)
                self.marcador.place(x=6, y=21)
                self.cidade_nome_label.configure(text=dados['cidade'])
                self.temperatura_label.configure(text=dados['temperatura'])
                self.previsao_label.configure(text=dados['descricao'])
                self.sensacao_label.configure(text=f"Sensação térmica de {dados['sensacao']}")
                self.maxmin_label.configure(text=f"Max: {dados['temp_max']} / Min: {dados['temp_min']}")
                self.umidade_label.configure(text=f"Umidade: {dados['umidade']} %")

                if dados['descricao'].lower() in ["clear sky"]:
                    self.clima.configure(text=sol, text_color="#ff9900")
                    self.resultados_frame.configure(fg_color="#B5DBFF")

                elif dados['descricao'].lower() in ["few clouds", "scattered clouds", "broken clouds",
                                                  "overcast clouds"]:
                    self.clima.configure(text=nuvem, text_color="white")
                    self.resultados_frame.configure(fg_color="#A5A5A5")

                elif dados['descricao'].lower() in ["light rain", "moderate rain", "heavy intensity rain",
                                                  "very heavy rain", "extreme rain", "freezing rain",
                                                  "light intensity shower rain", "shower rain",
                                                  "heavy intensity shower rain", "ragged shower rain"]:
                    self.clima.configure(text=chuva, text_color="white")
                    self.resultados_frame.configure(fg_color="#6A7799")

                elif dados['descricao'].lower() in ["light snow", "snow", "heavy snow", "sleet",
                                                  "light shower sleet", "shower sleet", "light rain and snow",
                                                  "rain and snow", "light shower snow", "shower snow",
                                                  "heavy shower snow"]:
                    self.clima.configure(text=neve, text_color="white")
                    self.resultados_frame.configure(fg_color="#E3E8FF")

                elif dados['descricao'].lower() in ["thunderstorm with light rain", "thunderstorm with rain",
                                                  "thunderstorm with heavy rain", "light thunderstorm",
                                                  "thunderstorm", "heavy thunderstorm", "ragged thunderstorm",
                                                  "thunderstorm with light drizzle", "thunderstorm with drizzle",
                                                  "thunderstorm with heavy drizzle"]:
                    self.clima.configure(text=tempestade, text_color="white")
                    self.resultados_frame.configure(fg_color="#303d4b")

                else:
                    self.clima.configure(text=vento, text_color="white")
                    self.resultados_frame.configure(fg_color="#C2CCFF")

            except ValueError:
                self.resultados_frame.destroy()
                self.mensagem.configure(text="Não encontramos o que você está procurando :(")