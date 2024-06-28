import time

def menu():
    print("\n===== Car Rent =====\n")
    print("1 - Alugar um carro")
    print("2 - Lista de carros")
    print("3 - Sair")

    opcao = int(input("\nDigite o número da opção desejada: "))
    return opcao
        
def alugar_carro(veiculos):
    if any(veiculo['disponivel'] for veiculo in veiculos):
        print("\n=== Cadastro ===\n")
        print("Antes de prosseguirmos, precisamos de algumas informações suas\n")
        nome = str(input("Digite seu nome completo: "))
        nascimento = input("Data de nascimento: ")
        cpf = input("Digite seu CPF (somente números): ")
        endereco = input("Digite seu endereço: ")
        cidade = input("Digite sua cidade: ")
        telefone = input("Digite seu número de telefone (somente números): ")

        print("\nTudo certo!\nQue tal escolher o carro?")
        time.sleep(1)
        print("\nImprimindo veículos disponíveis...")
        time.sleep(2)
        for veiculo in veiculos:
            if veiculo['disponivel']:
                print(f"\n\tMarca: {veiculo['marca']}\n\tAno: {veiculo['ano']}\n\tPlaca: {veiculo['placa']}\n\tDiária: {veiculo['diaria']}\n")
                time.sleep(1)

        marca = input("Digite a marca que deseja: ")
        for veiculo in veiculos:
            if veiculo['disponivel'] and marca.lower() == veiculo['marca'].lower():
                print("\nMarca escolhida:")
                print(f"\n\tMarca: {veiculo['marca']}\n\tAno: {veiculo['ano']}\n\tPlaca: {veiculo['placa']}\n\tDiária: {veiculo['diaria']}\n")
                
                time.sleep(2)
                tempo_uso = int(input("Quantos dias pretende usar o veículo: "))
                
                print("\nVerifique as informações antes de prosseguir\n")
                time.sleep(1)
                print("Informações pessoais:")
                print(f"\tNome: {nome}\n\tData de Nascimento: {nascimento}\n\tCPF: {cpf}\n\tEndereço: {endereco} - {cidade}\n\tTelefone: {telefone}")
                print("\nInformações sobre o carro:")
                print(f"\tMarca: {veiculo['marca']}\n\tAno: {veiculo['ano']}\n\tPlaca: {veiculo['placa']}\n\tDiária: {veiculo['diaria']}\n\tTempo de uso: {tempo_uso} dias\n")

                opcao = input("\nDeseja continuar? (Sim/Não): ")
                if opcao.lower() == 'sim':
                    veiculo['disponivel'] = False
                    print("\nSeu cadastro e a reserva do carro foram concluídos com sucesso!\nPasse em uma de nossas agências mais próximas para coleta biométrica e retirada do carro.\n")
                    print("Agradecemos a preferência! Volte sempre ;)")
                    time.sleep(2)
                return
        else:
            print("\nMarca não encontrada ou indisponível!\nVerifique se escreveu corretamente.\n")
    else:
        print("\nInfelizmente, não temos nenhum veículo disponível!\nVolte mais tarde.\n")
        time.sleep(2)

def lista_carros(veiculos):
    print("\n=== Lista de Carros ===\n")
    for veiculo in veiculos:
        disponibilidade = "Disponível" if veiculo['disponivel'] else "Indisponível"
        print(f"\tMarca: {veiculo['marca']}\n\tAno: {veiculo['ano']}\n\tPlaca: {veiculo['placa']}\n\tDiária: {veiculo['diaria']}\n\tDisponibilidade: {disponibilidade}\n")
        time.sleep(1)
def main():
    veiculos = [
        {'marca': 'Fox', 'ano': '2009','placa': 'JSA-1562','diaria':'R$100', 'disponivel': True},
        {'marca': 'Ford Ka', 'ano': '2014','placa': 'OZK-7563','diaria':'R$300', 'disponivel': True},
        {'marca': 'Supra', 'ano': '2022','placa': 'DFK-3197','diaria':'R$750', 'disponivel': True}
    ]

    while True:
        opcao = menu()

        if opcao == 1:
            alugar_carro(veiculos)

        elif opcao == 2:
            lista_carros(veiculos)

        elif opcao == 3:
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(1)

if __name__ == '__main__':
    main()