class Pedido:
    contador_id = 1  # classe variável para gerar ID automático

    def __init__(self, cliente):
        self.id = Pedido.contador_id
        Pedido.contador_id += 1

        self.cliente = cliente
        self.itens = []         # Lista de dicionários: {"produto": nome, "preco": valor}
        self.total = 0.0

    def adicionar_item(self, produto, preco):
        self.itens.append({"produto": produto, "preco": preco})
        self.total += preco

    def exibir_pedido(self):
        print(f"\n\033[36mPedido #{self.id} - Cliente: {self.cliente}\033[m")
        print("\033[33mItens do pedido:\033[m")
        for item in self.itens:
            print(f" - {item['produto']} - R$ {item['preco']:.2f}")
        print(f"\033[32mTotal: R$ {self.total:.2f}\033[m")
