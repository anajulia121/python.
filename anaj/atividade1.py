def recomendacao_conteudo():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    if idade.isdigit():
        idade = int(idade)  
        if idade <= 12:
            print(f"Olá {nome}, recomendamos conteúdos infantis, malvado favorito!")
        if 12<= idade <= 17:
            print(f"Olá {nome}, recomendamos jogos e filmes juvenis!, como treinar seu dragao")
        elif idade >=18:
            print(f"Olá {nome}, recomendamos filmes e livros adultos! clube da luta")
    else:
        print("Erro: idade invalida")

recomendacao_conteudo()
