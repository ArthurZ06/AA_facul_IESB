# Importa o módulo 'functions' com funções criadas no projeto
# Importa as listas 'product', 'client' e 'request' do banco de dados
# Importa a função 'sleep' para pausar a execução por alguns segundos
# Importa a classe 'Pedido' usada para criar objetos de pedidos

from services import functions
from services.database import product, client, request
from time import sleep
from entities.classes import Pedido

# Cria um loop infinito que mantém o programa rodando até que o usuário escolha sair
while True:
    print('\033[35mCOFFEE SHOPS TIA ROSA\033[m')

    # Mostra o menu principal com as opções disponíveis
    print('''
\033[36m1 - Cadastro de produtos
2 - Cadastro de clientes
3 - Registrar pedido
4 - Mostrar pedidos\033[m
\033[31m5 - Remover pedido
999 - Encerra o programa\033[m
''')

    # Tenta converter a escolha do usuário para número inteiro
    try:
        option = int(input('Escolha uma opção: '))
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print('\033[31mOpção inválida! Digite um número.\033[m')
        sleep(2)
        continue  # Volta ao início do loop

    # Opção para encerrar o programa
    if option == 999:
        print('\n\033[33mObrigado por utilizar o programa\033[m')
        break  # Encerra o loop

    # ================= CADASTRO DE PRODUTOS =================
    elif option == 1:
        while True:
            print('\n\033[36mCadastro de produtos\033[m\n')
            try:
                choice = int(input('''\033[33m
0 - Voltar ao menu principal
1 - Mostrar produtos
2 - Adicionar produtos
3 - Remover produtos\033[m
Digite aqui: '''))
            except ValueError:
                print('\033[31mEntrada inválida! Digite um número.\033[m')
                sleep(1)
                continue

            # Voltar para o menu principal
            if choice == 0:
                break

            # Mostrar lista de produtos cadastrados
            elif choice == 1:
                if product:
                    print('\033[32mProdutos cadastrados:\033[m')
                    for produto in product:
                        print(produto)
                else:
                    print('\033[31mNenhum produto cadastrado.\033[m')
                sleep(2)

            # Adicionar novo produto
            elif choice == 2:
                add_product = input('Nome do produto: ')
                functions.addProduct(add_product)  # Chama função para adicionar
                print('\033[32mProduto cadastrado com sucesso!\033[m')
                print('Produtos atuais:', product)
                sleep(2)

            # Remover produto existente
            elif choice == 3:
                print('Produtos atuais:', product)
                remove_product = input('Nome do produto para remover ou o índice: ')
                functions.removeProduct(remove_product)
                print('Produtos atualizados:', product)
                sleep(2)

            else:
                print('\033[31mOpção inválida.\033[m')
                sleep(1)

    # ================= CADASTRO DE CLIENTES =================
    elif option == 2:
        while True:
            print('\n\033[36mCadastro de clientes\033[m')
            try:
                choice = int(input('''\033[33m
0 - Voltar ao menu principal
1 - Mostrar clientes
2 - Adicionar clientes
3 - Remover clientes\033[m
Digite aqui: '''))
            except ValueError:
                print('\033[31mEntrada inválida! Digite um número.\033[m')
                sleep(1)
                continue

            if choice == 0:
                break

            # Mostrar clientes cadastrados
            elif choice == 1:
                if client:
                    print('\033[32mClientes cadastrados:\033[m')
                    for clientes in client:
                        print(clientes)
                else:
                    print('\033[31mNenhum cliente cadastrado.\033[m')
                sleep(2)

            # Adicionar cliente
            elif choice == 2:
                add_client = input('Nome do cliente: ')
                functions.cadastrarCliente(add_client)
                print('\033[32mCliente cadastrado com sucesso!\033[m')
                print(f'Clientes atuais: {client}')
                sleep(2)

            # Remover cliente
            elif choice == 3:
                print(f'Clientes atuais: {client}')
                remove_client = input('Nome do cliente ou índice para remover: ')
                functions.removerCliente(remove_client)
                print(f'Clientes atualizados: {client}')
                sleep(2)

            else:
                print('\033[31mOpção inválida.\033[m')
                sleep(1)

    # ================= REGISTRAR PEDIDO =================
    elif option == 3:
        # Impede registro se não houver clientes cadastrados
        if not client:
            print('\033[31mNão há clientes cadastrados!\033[m')
            sleep(2)
            continue

        # Impede registro se não houver produtos cadastrados
        if not product:
            print('\033[31mNão há produtos cadastrados!\033[m')
            sleep(2)
            continue

        # Lista clientes para o usuário escolher
        print("\nClientes disponíveis:")
        for i, c in enumerate(client):
            print(f"{i} - {c}")

        try:
            cliente_index = int(input("Escolha o cliente pelo número: "))
            cliente_nome = client[cliente_index]
        except (ValueError, IndexError):
            print('\033[31mCliente inválido.\033[m')
            sleep(1)
            continue

        # Cria um novo pedido para o cliente escolhido
        pedido = Pedido(cliente_nome)

        while True:
            # Lista produtos para adicionar ao pedido
            print("\nProdutos disponíveis:")
            for i, p in enumerate(product):
                print(f"{i} - {p}")

            try:
                prod_index = int(input("Escolha o produto pelo número (ou escreva -1 para finalizar): "))
                if prod_index == -1:  # Sai do loop de adição
                    break
                produto_nome = product[prod_index]
                preco = float(input(f"Digite o preço de '{produto_nome}': R$ "))
            except (ValueError, IndexError):
                print('\033[31mEntrada inválida.\033[m')
                continue

            # Adiciona o produto no pedido
            pedido.adicionar_item(produto_nome, preco)

        # Exibe resumo do pedido
        pedido.exibir_pedido()
        request.append(pedido)  # Salva o pedido na lista
        print("\033[32mPedido registrado com sucesso!\033[m")
        sleep(2)

    # ================= MOSTRAR PEDIDOS =================
    elif option == 4:
        if not request:
            print("\033[31mNenhum pedido registrado.\033[m")
        else:
            print("\n\033[36mPedidos registrados:\033[m")
            for i, pedido in enumerate(request, start=1):
                print(f"\n--- Pedido {i} ---")
                pedido.exibir_pedido()
                print()
        sleep(2)

    # ================= REMOVER PEDIDO =================
    elif option == 5:
        if not request:
            print("\033[31mNenhum pedido registrado para remover.\033[m")
            sleep(2)
            continue

        # Lista pedidos para escolher qual remover
        print("\n\033[36mPedidos registrados:\033[m")
        for i, pedido in enumerate(request):
            print(f"{i} - Cliente: {pedido.cliente}, Total: R$ {pedido.total:.2f}")

        try:
            index_remover = int(input("\nDigite o número do pedido que deseja remover: "))
            if 0 <= index_remover < len(request):
                removido = request.pop(index_remover)
                print(f"\033[32mPedido do cliente '{removido.cliente}' removido com sucesso!\033[m")
            else:
                print("\033[31mÍndice inválido.\033[m")
        except ValueError:
            print("\033[31mEntrada inválida.\033[m")
        sleep(2)
