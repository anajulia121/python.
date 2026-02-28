class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
    
    def frear(self, valor):
        self.velocidade = max(0, self.velocidade - valor)
    
    def exibir_dados(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Portas: {self.portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas} cc")

def main():
    carro = Carro("Toyota", "Corolla", 2022, 4)
    moto = Moto("Honda", "CBR 500R", 2021, 500)
    
    print("Antes de acelerar")
    carro.exibir_dados()
    moto.exibir_dados()
    
    carro.acelerar(50)
    moto.acelerar(80)
    
    print("Apos acelerar")
    carro.exibir_dados()
    moto.exibir_dados()
    
    carro.frear(30)
    moto.frear(50)
    
    print("Apos frear")
    carro.exibir_dados()
    moto.exibir_dados()

if __name__ == '__main__':
    main()