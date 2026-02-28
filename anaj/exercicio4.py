salario_atual = float(input("Digite o salário atual: "))
percentual_aumento = float(input("Digite a porcentagem de aumento: "))
aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + aumento
print(f"O novo salário após o aumento é: {novo_salario:.2f}")
