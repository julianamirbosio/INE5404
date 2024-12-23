class Cliente:
    def __init__(self, nome, cpf, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Estacionamento:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def remover_carro(self, placa):
        for carro in self.carros:
            if carro['placa'] == placa:
                self.carros.remove(carro)

    def verificar_disponibilidade(self, placa):
        for carro in self.carros:
            if carro['placa'] == placa and carro['disponibilidade']:
                return True
        return False


    def mostrar_carros(self):
        if self.carros == []:
            print("Parece que não há carros no Estacionamento. :(")
        else:
            for carro in self.carros:
                print(
                      "------------------------------------------------------------------------"
                  )
                print(f"Modelo: {carro['modelo']}")
                print(f"Ano: {carro['ano']}")
                print(f"Diária: R${carro['diaria']}")
                print(
                      f"Disponibilidade: {'Disponível' if carro['disponibilidade'] else 'Indisponível'}"
                  )
                print(f"Câmbio: {carro['cambio']}")
                print(f"Combustível: {carro['combustivel']}")
                print(f"Ar condicionado: {'Sim' if carro['ar'] else 'Não'}")
                print(f"Capacidade de passageiros: {carro['pessoas']}")
                print(f"Placa: {carro['placa']}")

class Aluguel:
    def __init__(self, cliente, carro, dias, cadeirinha=False):
        self.cliente = cliente
        self.carro = carro
        self.dias = dias
        self.cadeirinha = cadeirinha
        self.valor = dias * (carro['diaria'] + (5 if cadeirinha else 0)) + 80 + 30

    def InfoContrato(self):
        print(
            "============================== CONTRATO ================================"
        )
        print(f"Nome do Locatário..........: {self.cliente.nome}")
        print(f"CPF........................: {self.cliente.cpf}")
        print(f"Email......................: {self.cliente.email}")
        print(f"Endereco...................: {self.cliente.endereco}")
        print(f"Marca/Modelo/Ano do carro..: {self.carro['modelo']} / {self.carro['ano']}")
        print(f"Tipo de combustível........: {self.carro['combustivel']}")
        print(f"Valor da diária............: R${self.carro['diaria']:.2f}")
        print(f"Dias.......................: {self.dias}")
        print(
            "----------------------------- Adicionais -------------------------------"
        )
        print("Seguro.....................: R$80.00")
        print("Limpeza....................: R$30.00")
        print(
            f"Cadeirinha infantil........: {'Sim' if self.cadeirinha else 'Não'}")
        print(
            "------------------------------------------------------------------------"
        )
        print(f"Valor......................: R${self.valor:.2f}")
        print(
            "========================================================================"
        )

veiculos = [
    {'placa': 'MCO-8696', 'modelo': 'Honda Civic', 'ano': '2020', 'diaria': 150.95, 'cambio': 'Manual', 'ar': True, 'pessoas': 5, 'disponibilidade': False, 'combustivel': 'Gasolina'},
    {'placa': 'JEU-3892', 'modelo': 'Fiat Mobi', 'ano': '2018', 'diaria': 70.95, 'cambio': 'Manual', 'ar': True, 'pessoas': 5, 'disponibilidade': True, 'combustivel': 'Gasolina'},
    {'placa': 'OSH-9829', 'modelo': 'Fiat Argo', 'ano': '2017', 'diaria': 75.95, 'cambio': 'Manual', 'ar': True, 'pessoas': 5, 'disponibilidade': False, 'combustivel': 'Gasolina'},
    {'placa': 'MAH-5198', 'modelo': 'Hyundai HB20S', 'ano': '2021', 'diaria': 90.95, 'cambio': 'Automático', 'ar': True, 'pessoas': 5, 'disponibilidade': True, 'combustivel': 'Flex'},
    {'placa': 'JSU-6152', 'modelo': 'Renault Sandero', 'ano': '2017', 'diaria': 111.95, 'cambio': 'Manual', 'ar': True, 'pessoas': 5, 'disponibilidade': True, 'combustivel': 'Gasolina'},
    {'placa': 'WUB-5276', 'modelo': 'Citroen C4', 'ano': '2019', 'diaria': 133.95, 'cambio': 'Automático', 'ar': True, 'pessoas': 5, 'disponibilidade': True,'combustivel': 'Gasolina'},
    {'placa': 'OAJ-9175', 'modelo': 'Volkswagen Gol', 'ano': '2018', 'diaria': 120.95, 'cambio': 'Manual', 'ar': True, 'pessoas': 5, 'disponibilidade': True, 'combustivel': 'Gasolina'}
]

# Adicionando carros ao estacionamento
estacionamento = Estacionamento()
for veiculo in veiculos:
    estacionamento.adicionar_carro(veiculo)

while True:
    print(
    "=========================== ALUGUEL DE CARRO ==========================="
  )
    print("Seja bem-vindo ao nosso estacionamento!")
    cliente_funcionario = input("Indentifique-se como cliente ou funcionário "
                            "(cliente/funcionario): ")

    if cliente_funcionario.lower().strip() == "cliente":
        print(
        "------------------------- Cadastro de cliente --------------------------"
    )
        print("Insira as informações requeridas: ")
        print()
        nome = input("Nome completo do locatário: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        endereco = input("Endereço: ")
        primeiro_nome = nome.split()[0]
        cliente = Cliente(nome, cpf, email, endereco)
        print(
          "------------------------------------------------------------------------"
        )
        print("Aqui está a Lista de carros disponíveis: ")
        estacionamento.mostrar_carros()
        print(
          "------------------------------------------------------------------------"
        )
        print()
    
        carro_escolhido = input("Insira a placa do carro que deseja alugar: ").upper().strip()
        while carro_escolhido not in [carro['placa'] for carro in estacionamento.carros]:
            print("Carro não encontrado. Tente novamente.")
            print()
            carro_escolhido = input("Insira a placa do carro que deseja alugar: ").upper().strip()
    
        while not estacionamento.verificar_disponibilidade(carro_escolhido):
            print("Carro indisponível. ")
            print()
            carro_escolhido = input("Insira a placa do carro que deseja alugar: ").upper().strip()
          
        print("Carro disponível. ")
        for carro in estacionamento.carros:
            if carro['placa'] == carro_escolhido:
              carro_escolhido = carro
              break
        print()
    
        dias = int(input("Por quantos dias deseja alugar o carro? "))
        print()
    
        print(
            "----------------------------- Adicionais -------------------------------"
        )
        print()
        print("Será cobrada a taxa de limpeza com valor tabelado em R$30,00 "
              "conjuntamente com a taxa de seguro com valor tabelado em R$80,00.")
        print()
        cadeirinha = input("Deseja adicionar cadeirinha infantil por um adicional "
                           "de R$5,00 ao dia? (s/n): ")
        print(
            "------------------------------------------------------------------------"
        )
        print()
        if cadeirinha.lower().strip() == "s":
            cadeirinha = True
        else:
            cadeirinha = False
    
        confirma = input(f"Tudo pronto {primeiro_nome}! Deseja fechar o contrato? (s/n): ")
        print()
        if confirma.lower() == "n":
            print("Que pena, volte sempre!")
            break
        else:
            aluguel_cliente = Aluguel(cliente, carro_escolhido, dias, cadeirinha)
            aluguel_cliente.InfoContrato()
            print("Muito obrigado pela preferência, volte sempre! :)")
            break 
  
    else:
        print(
        "------------------------------------------------------------------------"
    )
        # O modo funcionário é um looping infinito para que possamos guardar os carros e depois usar como cliente
        while True:
            comando = input('Digite "novo" para adicionar outro carro,'
                          ' "remover" para remover um carro,'
                          ' "lista" para ver a lista de carros'
                          ' ou "sair" para sair do modo funcionário: ').strip()
                          
            opcoes = ["novo", "remover", "lista", "sair"]
            while comando.lower() not in opcoes:
                comando = input("Comando inválido. Tente novamente: ")
      
            while comando.lower() == "novo":
                print(
                    "-------------------------- Cadastro de carro ---------------------------"
                )
                placa = input("Placa do carro: ")
                modelo = input("Modelo do carro: ")
                ano = input("Ano do carro: ")
                diaria = float(input("Diária do carro: "))
                disponibilidade = input("O carro está disponível? (s/n): ")
                disponibilidade = True if disponibilidade.lower() == "s" else False
                cambio = input("Tipo de câmbio do carro: ")
                ar = input("O carro possui ar condicionado? (s/n): ")
                ar = True if ar.lower() == "s" else False
                pessoas = int(input("Capacidade de passageiros: "))
                combustivel = input("Tipo de combustível do carro: ")
            
                estacionamento.adicionar_carro({'placa': placa, 'modelo': modelo, 'ano': ano, 
                                                'diaria': diaria, 'cambio': cambio, 'ar': ar, 
                                                'pessoas': pessoas, 'disponibilidade': disponibilidade,
                                                'combustivel': combustivel})
                print(
                "------------------------------------------------------------------------"
            )
                print("O novo carro foi adicionado ao estacionamento com sucesso! ")
                print(
                "------------------------------------------------------------------------"
            )
                comando = input('Digite "novo" para adicionar outro carro,'
                                ' "remover" para remover um carro,'
                                ' "lista" para ver a lista de carros'
                                ' ou "sair" para sair do modo funcionário: ').strip()
      
            if comando.lower() == "lista":
                print(
                    "------------------------------------------------------------------------"
                )
                print("Aqui está a Lista de carros disponíveis: ")
                print(
                    "------------------------------------------------------------------------"
                )
                estacionamento.mostrar_carros()
                print(
                    "------------------------------------------------------------------------"
                )
            
            if comando.lower() == "remover":
                placa = input("Insira a placa do carro que deseja remover: ").upper().strip()
                print(
                    "------------------------------------------------------------------------"
                )
                estacionamento.remover_carro(placa)
                print("O carro foi removido do estacionamento com sucesso! ")
                print()
                
            if comando.lower() == "sair":
                print("Saindo do modo funcionário...")
                print()
                break
