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


    product = ['maça', 'banana', 'pera']
    client = None
    request = {}

    def addProduct(produto):
        product.append(produto)

    def removeProduct(produto):
        product.remove(produto)

    addProduct('mantega')
    removeProduct('maça')

    option = int(input('escolha uma opção:'))

    if option == 1:
        print()
        print('\033[36mCadastro de produtos\033[m')
        print()
        choice = int(input('''
1-mostrar produtos
2-adicionar produtos
3-deletar produtos
digite aqui: '''))
        if choice == 1:
            print()
            if product != []:
                for produto in product:
                    print(produto)
            print()
        if choice == 2:
            add_product = input('nome do produto: ')
            addProduct(add_product)
            print(product)
            print()

        if choice == 3:
            print(product)
            remove_product = input('nome do produto: ')
            removeProduct(remove_product)
            print(product)
            print()

    if option == 999:
        print()
        print('\033[33mObrigado por utilizar o programa\033[m')
        break

