def criar_usuario(usuarios):
    """
    Cria um novo usuário e o adiciona à lista, garantindo CPF único.
    """
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Erro: Já existe um usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    })

    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """
    Busca um usuário na lista pelo CPF. 
    Retorna o dicionário do usuário ou None se não encontrado.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma conta corrente vinculada a um usuário existente.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario
        }

    print("\n@@@ Erro: Usuário não encontrado! Fluxo de criação de conta encerrado. @@@")
    return None


def listar_contas(contas):
    """
    Exibe todas as contas cadastradas no sistema.
    """
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada ainda. @@@")
        return

    print("-" * 30)
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)
        print("-" * 30)