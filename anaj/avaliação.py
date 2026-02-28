def classificar_atleta():
    nome = input("Nome do atleta: ")
    idade = int(input("Idade do atleta: "))
    sexo = input("Sexo do atleta (M/F): ")
    experiencia = float(input("Anos de treino: "))
    
    if idade < 8:  
           print("Muito jovem para competir")
    elif 8 <= idade <= 12:
           print("Categoria Infantil")
    elif 13 <= idade <= 17:
           print("Categoria Juvenil")
    elif 18 <= idade <= 30:
           print("Categoria Adulto")
    else:
        print("Categoria Sênior")
    
    if experiencia < 1:
           print("Iniciante")
    elif 1 <= experiencia < 3:
           print("Intermediário")
    else:
        print("Avançado")
    
    print(f"Atleta: {nome} Idade: {idade} anos Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}")
    print(f"Categoria Final: {idade} - {experiencia}")
    

classificar_atleta()

        
