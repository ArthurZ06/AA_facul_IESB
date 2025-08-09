# imports funções que eu criei database e sleep
from services import functions
from services.database import product, client, request

from time import sleep
from entities.classes import Pedido

# criando um laço infinito
while True:
    print('\033[35mCOFFEE SHOPS TIA ROSA\033[m')
    print('''
\033[36m1 - Cadastro de produtos
2 - Cadastro de clientes
3 - Registrar pedido
4 - Mostrar pedidos\033[m
\033[31m5 - Remover pedido
999 - Encerra o programa\033[m
''')

    try:
        option = int(input('Escolha uma opção: '))
    except ValueError:
        print('\033[31mOpção inválida! Digite um número.\033[m')
        sleep(2)
        continue

    if option == 999:
        print('\n\033[33mObrigado por utilizar o programa\033[m')
        break

    elif option == 1:  # Cadastro de produtos
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

            if choice == 0:
                break

            elif choice == 1:
                if product:
                    print('\033[32mProdutos cadastrados:\033[m')
                    for produto in product:
                        print(produto)
                else:
                    print('\033[31mNenhum produto cadastrado.\033[m')
                sleep(2)

            elif choice == 2:
                add_product = input('Nome do produto: ')
                functions.addProduct(add_product)
                print('\033[32mProduto cadastrado com sucesso!\033[m')
                print('Produtos atuais:', product)
                sleep(2)

            elif choice == 3:
                print('Produtos atuais:', product)
                remove_product = input('Nome do produto para remover ou o índice: ')
                functions.removeProduct(remove_product)
                print('Produtos atualizados:', product)
                sleep(2)

            else:
                print('\033[31mOpção inválida.\033[m')
                sleep(1)

    elif option == 2:  # Cadastro de clientes
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

            elif choice == 1:
                if client:
                    print('\033[32mClientes cadastrados:\033[m')
                    for clientes in client:
                        print(clientes)
                else:
                    print('\033[31mNenhum cliente cadastrado.\033[m')
                sleep(2)

            elif choice == 2:
                add_client = input('Nome do cliente: ')
                functions.cadastrarCliente(add_client)
                print('\033[32mCliente cadastrado com sucesso!\033[m')
                print(f'Clientes atuais: {client}')
                sleep(2)

            elif choice == 3:   
                print(f'Clientes atuais: {client}')
                remove_client = input('Nome do cliente ou índice para remover: ')
                functions.removerCliente(remove_client)
                print(f'Clientes atualizados: {client}')
                sleep(2)

            else:
                print('\033[31mOpção inválida.\033[m')
                sleep(1)

    elif option == 3:  # Registro de pedidos
        if not client:
            print('\033[31mNão há clientes cadastrados!\033[m')
            sleep(2)
            continue

        if not product:
            print('\033[31mNão há produtos cadastrados!\033[m')
            sleep(2)
            continue

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

        pedido = Pedido(cliente_nome)

        while True:
            print("\nProdutos disponíveis:")
            for i, p in enumerate(product):
                print(f"{i} - {p}")

            try:
                prod_index = int(input("Escolha o produto pelo número (ou escreva -1 para finalizar): "))
                if prod_index == -1:
                    break
                produto_nome = product[prod_index]
                preco = float(input(f"Digite o preço de '{produto_nome}': R$ "))
            except (ValueError, IndexError):
                print('\033[31mEntrada inválida.\033[m')
                continue

            pedido.adicionar_item(produto_nome, preco)

        pedido.exibir_pedido()
        request.append(pedido)
        print("\033[32mPedido registrado com sucesso!\033[m")
        sleep(2)
    elif option == 4:
        if not request:
            print("\033[31mNenhum pedido registrado.\033[m")
        else:
            print("\n\033[36mPedidos registrados:\033[m")
            for i, pedido in enumerate(request, start=1):
                print(f"\n--- Pedido {i} ---")
                pedido.exibir_pedido()
        sleep(2)

    elif option == 5:
            if not request:
                print("\033[31mNenhum pedido registrado para remover.\033[m")
                sleep(2)
                continue

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



