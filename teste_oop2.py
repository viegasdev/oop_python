# Este ficheiro é um teste de aprendizagem de Programação Orientada a Objetos com Python

class Dog:
    def __init__(self, nome, idade): # O método "__init__" inicializa a nossa Classe
        self.nome = nome # Definimos que o nome do próprio objeto vai ser o que está no parâmetro da função
        self.idade = idade

    def get_age(self): # Definimos um método que nos vai retornar a idade do objeto referido
        return self.idade

    def get_name(self):
        return self.nome

d = Dog("Tim", 12) # Definimos um objeto com as características pretendidas

print(d.get_name()) # Mostramos no ecrã o valor retornado pela função
print(d.get_age())