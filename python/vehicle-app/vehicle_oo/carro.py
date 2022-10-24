class Carro:
    def __init__(self, marca, modelo, ano, correndo=False,):
        self.marca    = marca
        self.modelo   = modelo
        self.ano      = ano
        self.correndo = correndo
    
    def correr(self):
        if self.correndo:
            print(f'A {self.marca} {self.modelo} {self.ano} está correndo.')
            return
        print (f'{self.marca} {self.modelo} {self.ano} está parada')
        self.correndo = True
    