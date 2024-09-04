import os

os.system("cls || clear")


# criando a classe aluno
class Aluno:
    # Criando um construtor
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def exibi_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"

    # Instanciar classe.
aluno = Aluno("wagne",22)

print(aluno.exibi_dados())
# print(aluno.nome)
# print(aluno.idade)
