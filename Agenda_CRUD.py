from time import sleep
from os import system
contatos = []

# Função para adicionar um novo contato à agenda
def adicionar_contato():
    system('cls;clear')
    nome = input("Digite o nome do contato: ").title()
    telefone = salvar_telefone()
    email = input("Digite o email do contato: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")
    sleep(1.5)


# Função para buscar um contato na agenda
def buscar_contato():
    if lista_vazia():
        return
    system('cls;clear')
    nome = input("Digite o nome do contato que deseja buscar: ").title()
    for contato in contatos:
        if contato["nome"] == nome:
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            system('pause')
            return
    print("Contato não encontrado.")
    sleep(1.5)

# Função para atualizar um contato na agenda
def atualizar_contato():
    if lista_vazia():
        return
    system('cls;clear')
    nome = input("Digite o nome do contato que deseja atualizar: ").title()
    for contato in contatos:
        if contato["nome"] == nome:
            novo_telefone = salvar_telefone()
            novo_email = input("Digite o novo email: ")
            contato["telefone"] = novo_telefone
            contato["email"] = novo_email
            print("Contato atualizado com sucesso!")
            return
    print("Contato não encontrado.")
    sleep(1.5)

# Função para remover um contato da agenda
def remover_contato():
    if lista_vazia():
        return
    system('cls;clear')
    nome = input("Digite o nome do contato que deseja remover: ").title()
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print("Contato removido com sucesso!")
            return
    print("Contato não encontrado.")
    sleep(1.5)

# Função para exibir todos os contatos da agenda
def exibir_contatos():
    if lista_vazia():
        return
    system('cls;clear')
    print('AGENDA'.center(30, '_'))
    for contato in contatos:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print("-------------------------")
    system('pause')

# Função para conferir se a lista de contatos está vazia
def lista_vazia():
    if not contatos:
        print('Lista vazia', end='')
        for _ in range(3):
            sleep(0.5)
            print('.', end='', flush=True)
        return True
    return False

# Salva número do telefone com um padrão
def salvar_telefone():
    while True:
        telefone = input("Digite o telefone do contato: ")
        if not telefone.isdigit():
            print('Digite apenas números!')
            continue
        if len(telefone) != 11 and len(telefone) != 9 and len(telefone) != 8:
            print('Número de telefone invalido')
            continue
        telefone_formatado = ''
        if len(telefone) == 11:
            for i, digito in enumerate(telefone):
                if i == 0:
                    telefone_formatado += '(' + digito
                elif i == 1:
                    telefone_formatado += digito + ') '
                elif i == 6:
                    telefone_formatado += digito + '-'
                else:
                    telefone_formatado += digito
        elif len(telefone) == 9:
            for i, digito in enumerate(telefone):
                if i == 4:
                    telefone_formatado += digito + '-'
                else:
                    telefone_formatado += digito
        elif len(telefone) == 8:
            for i, digito in enumerate(telefone):
                if i == 3:
                    telefone_formatado += digito + '-'
                else:
                    telefone_formatado += digito
        break
    return telefone_formatado



# Menu de opções da agenda
while True:
    system('cls;clear')

    print("Selecione uma opção:")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Atualizar contato")
    print("4 - Remover contato")
    print("5 - Exibir todos os contatos")
    print("6 - Sair")

    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        atualizar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        exibir_contatos()
    elif opcao == "6":
        break
    else:
        print("Opção inválida.")
