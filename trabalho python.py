
def adicionar_produto(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    print(f"{quantidade} unidades de {produto} adicionadas ao estoque.")




def remover_produto(estoque, produto, quantidade):
    if produto in estoque:
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print(f"{quantidade} unidades de {produto} removidas do estoque.")
        else:
            print(
                f"Não há {quantidade} unidades de {produto} disponíveis no estoque.")
    else:
        print(f"{produto} não está no estoque.")


def exibir_estoque(estoque):
    print("\nEstoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")



estoque = {}


while True:
    print("\n Sistema de Gerenciamento de Estoque")
    print("1. Adicionar produto ao estoque")
    print("2. Remover produto do estoque")
    print("3. Exibir estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade a adicionar: "))
        adicionar_produto(estoque, produto, quantidade)
    elif opcao == '2':
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade a remover: "))
        remover_produto(estoque, produto, quantidade)
    elif opcao == '3':
        exibir_estoque(estoque)
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
