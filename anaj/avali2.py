class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def alterar_velocidade(self, valor):
        self.velocidade = max(0, self.velocidade + valor)

    def exibir_dados(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) - {self.velocidade} km/h")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"{self.portas} portas")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"{self.cilindradas} cc")

carro = Carro("Toyota", "Corolla", 2022, 4)
moto = Moto("Honda", "CB500", 2021, 500)

carro.alterar_velocidade(20)
moto.alterar_velocidade(40)
carro.alterar_velocidade(-10)
moto.alterar_velocidade(-20)

carro.exibir_dados()
moto.exibir_dados()
