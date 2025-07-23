#importa product e client que esta em database.py
from database import product, client


#Produtos


#função para adicionar produto na lista product
def addProduct(value):
    product.append(value)

#função que remove produto da lista product
def removeProduct(value):
    # tratando para poder tirar o produto pelo indice
    if value.isdigit():
        index = int(value)
        if 0 <= index < len(product):
            removed = product.pop(index)
            print(f'\033[32mProduto "{removed}" removido com sucesso pelo indice.\033[m')
        else:
            print('\033[31mIndice inválido!\033[m')
    else:
        # tratando para poder remover pelo nome
        if value in product:
            product.remove(value)
            print(f'\033[32mProduto "{value}" removido com sucesso pelo nome.\033[m')
        else:
            print('\033[31mProduto não encontrado!\033[m')


#Crientes


#função que cadastra clientes joga na lista client
def cadastrarCliente(value):
    client.append(value)

def removerCliente(value):
    # tratando para poder tirar o produto pelo indice
    if value.isdigit():
        index = int(value)
        if 0 <= index < len(client):
            removed = client.pop(index)
            print(f'\033[32mCriente "{removed}" removido com sucesso pelo indice.\033[m')
        else:
            print('\033[31mIndice inválido!\033[m')
    else:
        # tratando para poder remover pelo nome
        if value in client:
            client.remove(value)
            print(f'\033[32mCriente "{value}" removido com sucesso pelo nome.\033[m')
        else:
            print('\033[31mProduto não encontrado!\033[m')

