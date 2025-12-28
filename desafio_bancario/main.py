from core.operacoes import depositar, sacar, exibir_extrato
from core.usuarios import criar_usuario, criar_conta, listar_contas
from database import mock_db

def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(menu_text)

def main():
    db = mock_db.estado_bancario

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            db["saldo"], db["extrato"] = depositar(db["saldo"], valor, db["extrato"])

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            db["saldo"], db["extrato"] = sacar(
                saldo=db["saldo"],
                valor=valor,
                extrato=db["extrato"],
                limite=db["limite"],
                numero_saques=db["numero_saques"],
                limite_saques=db["limite_saques"],
            )
            db["numero_saques"] += 1 

        elif opcao == "e":
            exibir_extrato(db["saldo"], extrato=db["extrato"])

        elif opcao == "nu":
            criar_usuario(mock_db.usuarios)

        elif opcao == "nc":
            numero_conta = len(mock_db.contas) + 1
            conta = criar_conta(db["agencia"], numero_conta, mock_db.usuarios)
            if conta:
                mock_db.contas.append(conta)

        elif opcao == "lc":
            listar_contas(mock_db.contas)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema bancário!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente. @@@")

if __name__ == "__main__":
    main()