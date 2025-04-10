# Função para calcular a comissão
def calcular_comissao(valor_venda):
    if valor_venda <= 5000:
        return valor_venda * 0.05  # Comissão de 5% para vendas até R$5000
    elif valor_venda > 5000:
        return valor_venda * 0.08  # Comissão de 8% para vendas acima de R$5000

# Lista para armazenar os dicionários de vendas
vendedores = []

# Função para registrar uma venda
def registrar_venda():
    nome = input("Digite o nome do vendedor: ")
    valor_venda = float(input("Digite o valor da venda: R$"))

    comissao = calcular_comissao(valor_venda)
    
    # Cria um dicionário para cada vendedor e adiciona na lista
    vendedor = {
        'nome': nome,
        'venda': valor_venda,
        'comissao': comissao
    }
    vendedores.append(vendedor)
    
    # Exibindo o resultado
    print(f"\nComissão do vendedor {nome}: R${comissao:.2f} (Venda: R${valor_venda:.2f})")

# Função para exibir todas as vendas e comissões registradas
def exibir_comissoes():
    if not vendedores:
        print("\nNenhum vendedor registrado ainda.")
        return
    
    print("\nVendas e Comissões Registradas:")
    for vendedor in vendedores:
        nome = vendedor['nome']
        venda = vendedor['venda']
        comissao = vendedor['comissao']
        print(f"Vendedor: {nome} | Venda: R${venda:.2f} | Comissão: R${comissao:.2f}")

# Função principal que controla o fluxo do programa
def main():
    while True:
        print("\n1. Registrar venda de um vendedor")
        print("2. Exibir comissões registradas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            registrar_venda()
        

# Executando o programa
if __name__ == "__main__":
    main()
