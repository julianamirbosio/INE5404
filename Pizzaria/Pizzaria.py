class Cliente():
    def __init__(self, nome, telefone, bairro, rua, numero):
        self.nome = nome
        self.telefone = telefone
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.endereco = ', '.join([self.bairro, self.rua, self.numero])
        self.primeiro_nome = (self.nome.split())[0]


class Funcionario():
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email


class Pizza():
    def __init__(self, sabor, preco_P, preco_M, preco_G, preco_F, ingredientes):
        self.sabor = sabor
        self.preco_P = preco_P
        self.preco_M = preco_M
        self.preco_G = preco_G
        self.preco_F = preco_F
        self.ingredientes = ingredientes


class Pizzaria():
    def __init__(self):
        self.clientes = []
        self.funcionarios = []
        self.pizzas = []
        self.pedidos = []

    def menu(self):
        print()
        print("================ MENU DO SISTEMA =================")
        print("     1 - Cadastrar Cliente")
        print("     2 - Cadastrar Funcionário")
        print("     3 - Fazer um pedido")
        print("     4 - Administrar")
        print("     5 - Sair")
        print("==================================================")

    def menu_adm(self):
        print()
        print("-------------- Menu Administrativo ---------------")
        print("     1 - Adicionar um item ao cardápio")
        print("     2 - Remover um item do cardápio")
        print("     3 - Consultar Cardápio")
        print("     4 - Consultar lista de Pedidos")
        print("     5 - Consultar lista de Clientes")
        print("             * Remover Cliente")
        print("     6 - Consultar lista de Funcionários")
        print("             * Remover Funcionario")
        print("     7 - Sair do modo administrador")
        print("--------------------------------------------------")

    def cardapio(self):
        print()
        print("==================== CARDÁPIO ====================")
        if self.pizzas == []:
            print()
            print("Ops! Parece que não temos nenhuma pizza cadastrada ainda :(")
        else:
            for index, pizza in enumerate(self.pizzas, start=1):
                print(f"{index}. {pizza.sabor}")
                print(f"Ingredientes: {', '.join(pizza.ingredientes)}.")
                print(f"// P: R${pizza.preco_P:.2f} // M: R${pizza.preco_M:.2f} // "
                      f"G: R${pizza.preco_G:.2f} // F: R${pizza.preco_F:.2f} //")
                print()
        print("==================================================")

    def buscar_funcionario_por_cpf(self, cpf):
        for i in self.funcionarios:
            if i.cpf == cpf:
                return True
        return False

    def buscar_cliente_por_telefone(self, telefone):
        for cliente in self.clientes:
            if cliente.telefone == telefone:
                return cliente
        return None

    def buscar_pizza_por_index(self, num):
        for pizza in self.pizzas:
            if self.pizzas.index(pizza) == (num - 1):
                return pizza
        return None

    def remover_pizza(self, sabor):
        for pizza in self.pizzas:
            if pizza.sabor.lower().strip() == sabor.lower().strip():
                self.pizzas.remove(pizza)
                print(f"Pizza '{pizza.sabor}' removida do cardápio.")
                return
        print(f"Pizza '{sabor}' não encontrada no cardápio.")

    def remover_cliente(self):
        while True:
            telefone = input("Digite o telefone do cliente que deseja remover: ")
            if len(telefone) == 11 and telefone.isdigit():
                telefone = "({}) {}-{}".format(telefone[:2], telefone[2:7], telefone[8:])
                break
            else:
                print("Número de telefone inválido. \n"
                      "Por favor insira um número válido (11 números): ")
        for cliente in self.clientes:
            if cliente.telefone == telefone:
                self.clientes.remove(cliente)
                print("Cliente removido.")
                return
        print("Cliente não encontrado.")

    def remover_funcionario(self, cpf_do_removedor):
        while True:
            cpf = input("Digite o CPF do funcionário que deseja remover: ")
            if len(cpf) == 11 and cpf.isdigit():
                cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
                break
            else:
                print("CPF inválido. Por favor insira um número válido (11 números): ")
        for funcionario in self.clientes:
            if funcionario.cpf == cpf:
                if funcionario.cpf == cpf_do_removedor:
                    print("Você não pode remover a si próprio.")
                    return
                else:
                    self.funcionarios.remove(funcionario)
                    print("Funcionário removido.")
                    return
        print("Funcionário não encontrado.")

    def mostrar_pedidos(self):
        print("----- Lista de Pedidos -----")
        print()
        if self.pedidos == []:
            print("Não há pedidos cadastrados.")
        else:
            for pedido in self.pedidos:
                print(f"============= PEDIDO Nº{self.pedidos.index(pedido) + 1} =============")
                print(f"Cliente....: {pedido.cliente.nome}")
                print(f"Telefone...: {pedido.cliente.telefone}")
                print(f"Endereço...: {pedido.cliente.endereco}")
                print("--------------------------------------------------")
                print(f"Pizza......: {pedido.pizza.sabor}")
                print(f"Tamanho....: {pedido.tamanho}")
                print(f"Preço......: R${pedido.preco_tamanho:.2f}")
                print(f"Adicionais.: {pedido.adicional}")
                print(f"Quantidade.: {pedido.quantidade}")
                print("--------------------------------------------------")
                print(f"Valor Total: R${pedido.valor_total:.2f}")
                print("==================================================")
                print()

    def mostrar_clientes(self):
        print("--------------- Lista de Clientes ----------------")
        print()
        if self.clientes == []:
            print("Não há clientes cadastrados.")
        else:
            for cliente in self.clientes:
                print(f"Nome: {cliente.nome}")
                print(f"Telefone: {cliente.telefone}")
                print(f"Endereço: {cliente.endereco}")
        print("--------------------------------------------------")

    def mostrar_funcionarios(self):
        print("------------- Lista de Funcionários --------------")
        print()
        if self.funcionarios == []:
            print("Não há funcionários cadastrados.")
        else:
            for funcionario in self.funcionarios:
                print(f"Nome: {funcionario.nome}")
                print(f"CPF: {funcionario.cpf}")
                print(f"Telefone: {funcionario.telefone}")
                print(f"E-mail: {funcionario.email}")
        print("--------------------------------------------------")


class Pedido():
    def __init__(self, cliente, pizza, tamanho, quantidade, adicional):
        self.cliente = cliente
        self.pizza = pizza
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.adicional = adicional
        # Mapeamento dos preços dos tamanhos de pizza
        self.preco_por_tamanho = {
            'P': self.pizza.preco_P,
            'M': self.pizza.preco_M,
            'G': self.pizza.preco_G,
            'F': self.pizza.preco_F
        }
        # Calcula o preço do tamanho da pizza
        self.preco_tamanho = self.preco_por_tamanho.get(self.tamanho, 0)
        self.valor_total = (self.preco_tamanho * self.quantidade) + (self.adicional * 0.5) + 7.00

    def gerar_nota(self):
        print()
        print("================== Nota Fiscal ===================")
        print(f"Cliente....: {self.cliente.nome}")
        print(f"Telefone...: {self.cliente.telefone}")
        print(f"Endereço...: {self.cliente.endereco}")
        print("==================================================")
        print(f"Pizza......: {self.pizza.sabor}")
        print(f"Tamanho....: {self.tamanho}")
        print(f"Preço......: R${self.preco_tamanho:.2f}")
        print(f"Adicionais.: {self.adicional}")
        print(f"Quantidade.: {self.quantidade}")
        print(f"Delivery...: R$7,00")
        print("-------------------------------------------------")
        print(f"Valor Total: R${self.valor_total:.2f}")
        print("=================================================")
        print("Obrigado pela preferência! :)")


pizzas = [
    Pizza("Calabresa", 30.00, 35.00, 40.00, 45.00,
          ['calabresa', 'queijo mussarela', 'tomate', 'cebola', 'azeitona',
           'orégano']),
    Pizza("Mussarela", 25.00, 30.00, 35.00, 40.00,
          ['queijo mussarela', 'tomate', 'azeitona', 'manjericão']),
    Pizza("Portuguesa", 32.00, 37.00, 42.00, 47.00,
          ['queijo mussarela', 'presunto', 'tomate', 'ovo', 'cebola', 'azeitona']),
    Pizza("Vegetariana", 30.00, 35.00, 40.00, 45.00,
          ['queijo', 'brócolis', 'palmito', 'tomate', 'cebola']),
    Pizza("Quatro Queijos", 32.00, 37.00, 42.00, 47.00,
          ['queijo mussarela', 'queijo parmesão', 'queijo gorgonzola',
           'queijo provolone', 'orégano']),
    Pizza("Frango com catupiry", 28.00, 33.00, 38.00, 43.00,
          ['frango', 'queijo mussarela', 'catupiry', 'tomate', 'cebola'])
]

# Instanciando a pizzaria apenas uma vez
pizzaria = Pizzaria()

# adiciono os sabores de pizza à pizzaria
for p in pizzas:
    pizzaria.pizzas.append(p)

aberto = True
print("==================================================")
print(" * * * * * * * * * * PIZZARIA * * * * * * * * * * ")
print("==================================================")
print("                Seja bem-vindo(a)!")

while aberto:
    pizzaria.menu()

    opcao = int(input("Digite a opção desejada: "))
    # Verifico se a opção é válida
    while opcao not in [1, 2, 3, 4, 5]:
        print("Opção inválida!")
        opcao = int(input("Digite a opção desejada: "))
        print()
    print()

    if opcao == 1:
        print("-------------- CADASTRO DE CLIENTE ---------------")
        nome = input("Nome completo: ")
        while True:
            telefone = input("Telefone: ").strip()
            # Verifico se o número é válido, caso sim, formato para o modo "(XX) XXXXX-XXXX"
            if len(telefone) == 11 and telefone.isdigit():
                telefone = "({}) {}-{}".format(telefone[:2], telefone[2:7], telefone[8:])
                break
            elif any(cliente.telefone == telefone for cliente in pizzaria.clientes):
                print("Cliente já cadastrado.")
            else:
                print("Número de telefone inválido. Por favor insira um número válido (11 números): ")
        bairro = input("Bairro: ")
        rua = input("Rua: ")
        numero = input("Numero + complemento: ")
        cliente = Cliente(nome, telefone, bairro, rua, numero)
        pizzaria.clientes.append(cliente)
        print("--------------------------------------------------")
        print("         Cliente cadastrado com sucesso!          ")
        print("--------------------------------------------------")
        print()

    if opcao == 2:
        print("------------ CADASTRO DE FUNCIONÁRIO -------------")
        nome = input("Nome completo: ")
        while True:
            # Verifico se o cpf é válido, caso sim, formato para o modo "XXX.XXX.XXX-XX"
            cpf = input("CPF (apenas números): ").strip()
            if len(cpf) == 11 and cpf.isdigit():
                cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
                break
            elif any(funcionario.cpf == cpf for funcionario in pizzaria.funcionarios):
                print("Funcionário já cadastrado.")
            else:
                print("CPF inválido. Por favor insira um CPF válido (11 números): ")
        while True:
            # Verifico se o número é válido, caso sim, formato para o modo "(XX) XXXXX-XXXX"
            telefone = input("Telefone: ").strip()
            if len(telefone) == 11 and telefone.isdigit():
                telefone = "({}) {}-{}".format(telefone[:2], telefone[2:7], telefone[8:])
                break
            else:
                print("Número de telefone inválido. Por favor insira um número válido (11 números): ")
        email = input("Email: ")

        funcionario = Funcionario(nome, cpf, telefone, email)
        pizzaria.funcionarios.append(funcionario)
        print("---------------------------------------------------")
        print("        Funcionário cadastrado com sucesso!        ")
        print("---------------------------------------------------")

    if opcao == 3:
        print("--------------------- PEDIDO ---------------------")
        print("Para acessar como cliente, insira seu número \n"
              "de telefone:")
        pdd = True
        while pdd:
            while True:
                telefone_cliente = input("Telefone: ").strip()
                # Verifico se o número é válido, caso sim, formato para o modo "(XX) XXXXX-XXXX"
                if len(telefone_cliente) == 11 and telefone_cliente.isdigit():
                    telefone_cliente = "({}) {}-{}".format(telefone_cliente[:2],
                                                           telefone_cliente[2:7],
                                                           telefone_cliente[8:])
                    break
                else:
                    print("Número de telefone inválido. "
                          "Por favor insira um número válido (11 números) ")

            # A função busca o objeto cliente correspondente ao telefone e
            # se ele estiver cadastrado, o retorna à variàvel comprador
            comprador = pizzaria.buscar_cliente_por_telefone(telefone_cliente)
            if comprador == None:
                print("Cliente não cadastrado.")
                print("Cadastre-se para fazer um pedido.")
                print()
                pdd = False
            else:
                print("Cliente encontrado!")
                print(f"Olá {comprador.primeiro_nome}! Como é bom te ver por aqui!")
                print()
                print("Aqui está o nosso cardápio:")
                pizzaria.cardapio()

                n_escolha = int(input("Digite o número da pizza que você deseja: "))
                while n_escolha not in range(len(pizzaria.pizzas) + 1):
                    print("Opção inválida!")
                    n_escolha = int(input("Digite o número da pizza que você deseja: "))

                # A função busca o objeto pizza correspondente ao index e
                # o retorna à variàvel pedido
                pedido = pizzaria.buscar_pizza_por_index(n_escolha)
                if pedido:
                    print(f"Você escolheu a pizza {pedido.sabor}!")
                    print()
                    tamanho = input("Tamanhos: \n"
                                    "P - Pequena \n"
                                    "M - Média \n"
                                    "G - Grande \n"
                                    "F - Família: \n"
                                    "Insira o tamanho da sua pizza (P, M, G ou F): ").upper()
                    while tamanho not in ['P', 'M', 'G', 'F']:
                        print("Opção inválida!")
                        tamanho = input("Insira o tamanho da sua pizza (P, M, G ou F): ").upper()
                    print()
                    quantidade = int(input("Digite a quantidade de pizzas: "))
                    print()
                    add = input("Deseja sachês adicionais por R$0,50 a unidade? (s/n): ").lower()
                    if add == 's':
                        adicional = int(input("Quantos? "))
                    else:
                        adicional = 0
                    print()
                    print("Taxa fixa para delivery de R$7,00")
                    confirma = input(f"Tudo pronto {comprador.primeiro_nome}, "
                                     f"deseja confirmar o pedido? (s/n): ").lower().strip()
                    if confirma == 's':
                        pedido_final = Pedido(comprador, pedido, tamanho, quantidade, adicional)
                        pizzaria.pedidos.append(pedido_final)
                        pedido_final.gerar_nota()
                    else:
                        print("Que pena! Esperamos te ver novamente...")
                    pdd = False
                else:
                    print("Não encontramos a pizza desejada.")

    if opcao == 4:
        print("----------------- ADMINISTRAÇÃO ------------------")
        adm = True
        while adm:
            while True:
                print("Para entrar no modo administrador, confirme \n"
                      "sua identidade como funcionário pelo seu cpf:")
                cpf = input()
                if len(cpf) == 11 and cpf.isdigit():
                    cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
                    break
                else:
                    print("CPF inválido. Por favor insira um CPF válido (11 números) ")
            print()
            if pizzaria.buscar_funcionario_por_cpf(cpf):
                while True:
                    pizzaria.menu_adm()
                    print()
                    comando = int(input("Insira o comando desejado: "))
                    while comando not in [1, 2, 3, 4, 5, 6, 7]:
                        print("Comando inválido.")
                        comando = int(input("Insira o comando desejado: "))
                        print()

                    if comando == 1:
                        print("* Adicionar novo sabor de pizza: *")
                        print("Insira as informações do novo sabor: ")
                        novo_sabor = input("Sabor: ").capitalize()
                        preco_p = float(input("Preço do tamanho pequeno: "))
                        preco_m = float(input("Preço do tamanho médio: "))
                        preco_g = float(input("Preço do tamanho grande: "))
                        preco_f = float(input("Preço do tamanho família: "))
                        ingredientes = input("Ingredientes [separados por espaço]: ").split()
                        ingredientes = ', '.join(ingredientes)
                        nova_pizza = Pizza(novo_sabor, preco_p, preco_m, preco_g, preco_f, ingredientes)
                        pizzaria.pizzas.append(nova_pizza)

                    if comando == 2:
                        print("* Remover um sabor de pizza: *")
                        sabor_remover = input("Insira o sabor da pizza a ser removida: ")
                        pizzaria.remover_pizza(sabor_remover)
                        print()

                    if comando == 3:
                        pizzaria.cardapio()

                    if comando == 4:
                        pizzaria.mostrar_pedidos()

                    if comando == 5:
                        pizzaria.mostrar_clientes()
                        comando1 = input("Deseja remover um cliente da lista? (s/n)").strip().lower()
                        if comando1 == 's':
                            pizzaria.remover_cliente()
                        else:
                            print("Ok, voltando ao menu administrativo...")
                        print()

                    if comando == 6:
                        pizzaria.mostrar_funcionarios()
                        comando2 = input("Deseja remover um funcionário da lista? (s/n): ").strip().lower()
                        if comando2 == 's':
                            pizzaria.remover_funcionario(cpf)
                        else:
                            print("Ok, voltando ao menu administrativo...")
                        print()

                    if comando == 7:
                        adm = False
            else:
                print("Este cpf não consta na lista de funcionários")
                print("Redirecionando para o menu...")
                adm = False

    if opcao == 5:
        aberto = False
        print("Obrigado por visitar a Pizzaria!")
