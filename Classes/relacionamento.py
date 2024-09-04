import os

os.system("cls || clear")

#Criando classe endereço
class Endereco:
    #Criando um construtor
    def __init__(self, logradouro: str, numero: str) -> None:
        self.logradouro = logradouro
        self.numero = numero

    # def exibir_dados(self):
    #     return (
    #         f"Logradouro: {self.logradouro}"
    #         f"\nNúmero: {self.numero}"
    #     )

    #Semelhante ao toString
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
        )


# criando a classe aluno
class Aluno:
    # Criando um construtor
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    #Semelhante ao toString
    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"

    # Instanciar classe.

aluno = Aluno("wagner",22,Endereco("Rua A","99"))

print(aluno)
# print(aluno.nome)
# print(aluno.idade)
