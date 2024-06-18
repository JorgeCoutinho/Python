import os

restaurantes = [
    {"nome": "Praça", "Categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza", "Categoria": "Italiana", "ativo": True},
    {"nome": "Cantina", "Categoria": "Polenesa", "ativo": False},
]


def exibir_nome_do_programa():
    print(
        """
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """
    )


def finalizar_app():
    exibir_subtitulo("Finalizar app..")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_opcoes():
    print("1. Cadastar restaurante")
    print("2. Listar restaurantes")
    print("3. ativar restaurante")
    print("4. Sair\n")


def cadastrar_novo_restaurante():
    """Cadastrar um novo restaurante no sistema
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    output:
    - Adiciona o restaurante na lista de restaurantes
    """
    exibir_subtitulo("Cadastros de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que desaja cadastra : ")
    categoria = input(
        f"Digite o nome da categoria do restaurante {nome_do_restaurante}: "
    )
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "Categoria": categoria,
        "ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"Restaurante {nome_do_restaurante} cadastrado com sucesso!\n")
    voltar_ao_menu_principal()


def listar_restaurantes():

    exibir_subtitulo("Listagem de restaurantes\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["Categoria"]
        ativo = restaurante["ativo"]
        print(f"- {nome_restaurante} | {categoria} | {ativo} \n")

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("ALterando estado do restaurante")
    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o estado: "
    )
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            )
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    voltar_ao_menu_principal()


def excolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        # opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    excolher_opcao()


if __name__ == "__main__":
    main()
