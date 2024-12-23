import requests

# link = f"https://history.openweathermap.org/data/2.5/aggregated/day?q={self.cidade}&month=
# {self.mes}&day={self.dia}&appid={self.API_KEY}"
class TempoInfo:
    def __init__(self, cidade):
        self.cidade = cidade.lower()
        self.API_KEY = "be5262bb9542a7bd5c9ab5595dcdd364"
        self.link = f"https://api.openweathermap.org/data/2.5/weather?q={self.cidade}&appid={self.API_KEY}&lang=pt-br"

    def requisicao(self):
        requisicao = requests.get(self.link)
        if requisicao.status_code != 200:
            return "Erro ao acessar a API. Verifique o nome da cidade e tente novamente."

        requisicao_dic = requisicao.json()

        # Retorna as informações
        nome_cidade = requisicao_dic['name']
        #pais = requisicao_dic['country']

        descricao_do_tempo = (requisicao_dic['weather'][0]['description']).capitalize()

        temperatura = "{:.1f}".format(round((requisicao_dic['main']['temp'] - 273.15), 1)).replace('.', ',')
        temperatura = f"{temperatura}°C"

        sensacao = "{:.1f}".format(round((requisicao_dic['main']['feels_like'] - 273.15), 1)).replace('.', ',')
        sensacao = f"{sensacao}°"

        temp_min = "{:.1f}".format(round((requisicao_dic['main']['temp_min'] - 273.15), 1)).replace('.', ',')
        temp_min = f"{temp_min}°"

        temp_max = "{:.1f}".format(round((requisicao_dic['main']['temp_max'] - 273.15), 1)).replace('.', ',')
        temp_max = f"{temp_max}°"

        umidade = requisicao_dic['main']['humidity']

        informacoes = {'cidade': nome_cidade,
                       'descricao': descricao_do_tempo,
                       'temperatura': temperatura,
                       'sensacao': sensacao,
                       'temp_min': temp_min,
                       'temp_max': temp_max,
                       'umidade': umidade}

        return informacoes

# Exemplo
'''cidade = input("Digite o nome da cidade: ")
previsao = TempoInfo(cidade)
resultado = previsao.requisicao()
print(resultado)'''