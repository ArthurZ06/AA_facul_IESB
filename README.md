# ☕ Coffee Shops Tia Rosa - Sistema de Gerenciamento

**Atividade do professor Francisco Lima (IESB)**  
Sistema simples em Python para reforçar conceitos práticos de programação.

---

## 📋 Descrição do Sistema

O sistema **Coffee Shops Tia Rosa** é uma aplicação de linha de comando que auxilia no controle da cafeteria fictícia. Ele facilita o cadastro de produtos e clientes, o registro e gerenciamento de pedidos, proporcionando um controle digital básico para o negócio.

---

## ⚙️ Funcionalidades

### 1. Cadastro de Produtos
- Listar produtos cadastrados  
- Adicionar novos produtos  
- Remover produtos por nome ou índice  

### 2. Cadastro de Clientes
- Listar clientes cadastrados  
- Adicionar novos clientes  
- Remover clientes por nome ou índice  

### 3. Registro e Gerenciamento de Pedidos
- Selecionar cliente para o pedido  
- Adicionar múltiplos produtos com preços ao pedido  
- Visualizar resumo detalhado do pedido, incluindo total

### 4. Mostrar Pedidos
- Exibir todos os pedidos realizados com detalhes (cliente, itens, total)

### 5. Remover Pedido
- Remover pedido pelo índice na lista de pedidos

### 6. Encerrar o Programa
- Opção para sair do sistema com mensagem de agradecimento

---

## 📂 Organização dos Arquivos

- `main.py`  
  Arquivo principal que apresenta o menu e gerencia o fluxo da aplicação.

- `functions.py`  
  Contém funções auxiliares para manipulação de produtos e clientes (adicionar e remover).

- `database.py`  
  Simula o banco de dados com listas globais:  
  - `product[]`: produtos cadastrados  
  - `client[]`: clientes cadastrados  
  - `request[]`: pedidos realizados

- `classes.py`  
  Define a classe `Pedido` que representa os pedidos realizados, com funcionalidades para adicionar itens, calcular o total e exibir detalhes formatados.

---

## 💡 Como Utilizar

1. Execute o programa: `python main.py`  
2. No menu principal, escolha entre:  
   - **1** - Cadastro de produtos  
   - **2** - Cadastro de clientes  
   - **3** - Registrar pedido  
   - **4** - Mostrar pedidos  
   - **5** - Remover pedido  
   - **999** - Encerra o programa  
3. Siga as instruções para adicionar, listar ou remover itens conforme necessário.  
4. No registro de pedidos, selecione o cliente e depois adicione produtos com seus preços, finalizando com `-1`.

---

## 📌 Considerações Finais

- O sistema funciona inteiramente na linha de comando, ideal para aprendizado e reforço dos conceitos básicos de Python.  
- As listas em `database.py` funcionam como banco de dados em memória, não persistindo dados entre execuções.  
- A aplicação utiliza tratamento de exceções para evitar entradas inválidas e manter a experiência amigável.
