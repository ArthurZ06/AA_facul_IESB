# ☕ Coffee Shops Tia Rosa - Sistema de Gerenciamento

**Atividade ativa do professor Francisco Lima (IESB)**  
Sistema simples em Python para reforçar os conhecimentos práticos da disciplina.

---

## 📋 Descrição do Sistema

O sistema tem como objetivo melhorar a gestão da cafeteria fictícia **Coffee Shops Tia Rosa**, que sofre com falta de controle digital. Ele permite o cadastro de produtos e clientes, além do registro de pedidos com preços e exibição do total.

---

## ⚙️ Funcionalidades

### 1. Cadastro de Produtos
- Listar produtos
- Adicionar novos produtos
- Remover produtos por nome ou índice

### 2. Cadastro de Clientes
- Listar clientes
- Adicionar novos clientes
- Remover clientes por nome ou índice

### 3. Registro de Pedidos
- Selecionar cliente
- Escolher produtos com preço
- Exibir resumo e valor total do pedido
- Salvar o pedido na memória

---

## 🧠 Explicação do Código (Passo a Passo)

### `main.py`
- Apresenta o menu principal em loop.
- Direciona para cadastro de produtos, clientes ou pedidos.
- Utiliza validações simples para entrada do usuário.

### `functions.py`
- Define funções auxiliares para:
  - Adicionar e remover **produtos**
  - Adicionar e remover **clientes**
- Permite remover tanto por **nome** quanto por **índice** da lista.

### `database.py`
- Simula um banco de dados com 3 listas globais:
  - `product[]`: lista de produtos
  - `client[]`: lista de clientes
  - `request[]`: lista de pedidos feitos

### `classes.py`
- Define a classe `Pedido`:
  - Atribui automaticamente um `ID`
  - Armazena o nome do cliente
  - Adiciona itens ao pedido com nome e preço
  - Calcula o total automaticamente
  - Exibe todos os dados formatados

---

## 🖼️ Prints Simulados

```bash
COFFEE SHOPS TIA ROSA

1 - Cadastro de produtos
2 - Cadastro de clientes
3 - Registro de pedidos
999 - Encerra o programa
