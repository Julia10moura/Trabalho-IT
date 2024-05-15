produtos = {}

def adicionar_produto():
    produtos[input("Nome do produto: ")] = float(input("Preço: "))
    print("Produto adicionado com sucesso!")

def listar_produtos():
    print("\nLista de produtos:")
    [print(f"{nome}: R${preco}") for nome, preco in produtos.items()] or print("Nenhum produto cadastrado.")

def remover_produto():
    produto = input("Digite o nome do produto que deseja remover: ")
    print(f"Produto '{produto}' removido com sucesso!" if produtos.pop(produto, None) else "Produto não encontrado.")

def main():
    while True:
        print("\n### Menu ###")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Remover Produto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": adicionar_produto()
        elif opcao == "2": listar_produtos()
        elif opcao == "3": remover_produto()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

