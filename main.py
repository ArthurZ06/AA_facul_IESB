# imports funções que eu criei database e sleep
import functions
from database import product, client, request
from time import sleep

# criando um laço infinito
while True:
    print('\033[35mCOFFEE SHOPS TIA ROSA\033[m')
    print(
        """
\033[36m1-Cadastro de produtos
2-Cadastro de clientes
3-Registro de pedidos\033[m
\033[31m999-Encerra o programa\033[m
"""
    )
    # usando try para se a pessoa digitar errado não estragar o programa inteiro
    try:
        option = int(input('Escolha uma opção: '))
    except ValueError:
        print('\033[31mOpção inválida! Digite um número.\033[m')
        sleep(2)
        print()
        continue
    # se a pessoa digitar 999 sai do programa
    if option == 999:
        print('\n\033[33mObrigado por utilizar o programa\033[m')
        break

    # primeira opção da pessoa
    # criei outro laço infinito para poder a pessoa ficar lá
    # e só sair para o menu principal quando apertar 0
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

            # voltar ao menu principal
            if choice == 0:
                print()
                break

            # primeira escolha
            # mostra os produtos para a pessoa
            elif choice == 1:
                print()
                if product:
                    print('\033[32mProdutos cadastrados:\033[m')
                    for produto in product:
                        print(produto)
                else:
                    print('\033[31mNenhum produto cadastrado.\033[m')
                print()
                sleep(2)

            # segunda escolha cadastra o produto
            # utilizo a função chamada addProduct para cadastrar a pessoa
            elif choice == 2:
                add_product = input('Nome do produto: ')
                functions.addProduct(add_product)
                print('\033[32mProduto cadastrado com sucesso!\033[m')
                print('Produtos atuais:', product)
                print()
                sleep(2)

            # terceira escolha
            # utilizo a função remove_product para tirar da lista
            elif choice == 3:
                print('Produtos atuais:', product)
                remove_product = input('Nome do produto para remover ou o indice: ')
                functions.removeProduct(remove_product)
                print('Produtos atualizados:', product)
                print()
                sleep(2)

            else:
                print('\033[31mOpção inválida dentro do cadastro de produtos.\033[m')
                sleep(1)

    # cadastrando clientes
    elif option == 2:
        while True:
            print()
            print('\033[36mCadastro de clientes\033[m')
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

            # voltar ao menu principal
            if choice == 0:
                print()
                break


            # primeira escolha
            # mostra todos os clientes
            elif choice == 1:
                print()
                if client:
                    print('\033[32mCliente cadastrados:\033[m')
                    for clientes in client:
                        print(clientes)
                else:
                    print('\033[31mNenhum cliente cadastrado.\033[m')
                print()
                sleep(2)


            # segunda escolha cadastrar clientes
            # utilizo a função chamada addProduct para cadastrar a pessoa
            elif choice == 2:
                add_client = input('Nome do cliente: ')
                functions.cadastrarCliente(add_client)
                print('\033[32mCliente cadastrado com sucesso!\033[m')
                print(f'clientes atuais:{client}')
                print()
                sleep(2)

            # terceira escolha
            # utilizo a função remove_product para tirar da lista
            elif choice == 3:
                print(f'Clientes atuais:{client}')
                remove_client = input('Nome do cliente ou index para remover: ')
                functions.removerCliente(remove_client)
                print(f'clientes atualizados:{client}')
                print()
                sleep(2)

            else:
                print('\033[31mOpção inválida dentro do cadastro de clientes.\033[m')
                sleep(1)


    elif option == 3:

        print()

    elif option == 999:
        print('\n\033[33mObrigado por utilizar o programa\033[m')
        break

