"""
crie um programa que:

-cadastre quantas pessoas eu quiser.
-liste o nome das pessoas cadastradas.
-pesquisar pelo nome de uma pessoa.
-ordenar a lista por ordem alfabética.
-atualizar nome.
-deletar nome da lista.
-sair do programa.

"""
#importa a biblioteca para limpar o código
import os

#cria uma lista vazia
pessoas = []

while True: #enquanto for verdadeiro
    11
    print(f"\n{'❰'*20} MENU CRUD {'❱'*20}\n ")
    print(f"{' '*8}1-Cadastrar novo nome:{' '*8}\n")
    print(f"{' '*8}2-Lista de nomes cadastrados:{' '*8}\n")
    print(f"{' '*8}3-Pesquisar nome:{' '*8}\n")
    print(f"{' '*8}4-Ordenar nomes em órdem alfabética:{' '*8}\n")
    print(f"{' '*8}5-Atualizar nome:{' '*8}\n")
    print(f"{' '*8}6-Deletar nome:{' '*8}\n")
    print(f"{' '*8}7-Sair:{' '*8}\n\n")

    opcao = input("Informe a opção desejada:\n")

    os.system('cls') #limpa

    #cadastro de nome
    if opcao == "1":
        id_nome = input("Informe o nome da pessoa:\n")
        pessoas.append(id_nome)
        print("Nome cadastrado!\n")


    #listar nomes
    elif opcao == "2":
        for id_nome in pessoas:
            print(id_nome)


    #pesquisar nomes
    elif opcao == "3":
        id_nome = input("Informe o nome que você procura:\n")
        if id_nome in pessoas:
            print(f"Nome encontrado {id_nome}.\n")
        else:
            print("Nome não encontrado.")


    #ordenar a lista em odem alfabética
    elif opcao == "4":
        pessoas.sort()
        for id_nome in pessoas:
            print(id_nome)


    #atualizar nomes da lista
    elif opcao == "5":
        atualiza_nome = input("Informe o nome que deseja alterar:\n")
        if atualiza_nome in pessoas:
            nome_atualizado = input("Informe o novo nome:\n")
            index = pessoas.index(atualiza_nome)
            pessoas[index] = nome_atualizado
            print("Nome atualizado.\n")
        else:
            print("Nome não encontrado.\n")


    #deletar nomes
    elif opcao == "6":
        id_nome = input("informe o nome a ser excluído:\n")
        if id_nome in pessoas:
            pessoas.remove(id_nome)
            print("Nome excluído.")
        else:
            print("Nome não encontrado.\n")


    #sair
    elif opcao == "7":
        print("Você saiu do programa.\n")
        break


    #caso o usuário insira um caracter inválido
    else:
        print("Opção inválida.\n")
    
