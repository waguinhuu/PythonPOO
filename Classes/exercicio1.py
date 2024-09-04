import os

os.system("cls || clear")

class Pet:
    def __init__(self, nome: str, idade: int,raca: str, porte: str,alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    def exibir_dados(self) -> None:
        return (f"Nome: {self.nome} \n Idade: {self.idade} \n Raça: {self.raca} Porte: {self.porte}"
                f"\n Alimentação: {self.alimentacao}")


pet = Pet("Thor",3,"Labrador","Leve","Ração")
pet2 = Pet("Amora",1,"Labrador","Leve","Ração")

print(pet.exibir_dados())
print(pet2.exibir_dados())