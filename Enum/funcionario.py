from enum import Enum
import os

os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, id: str, nome: str, setor: Setor, sexo: Sexo, idade: int) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.setor = setor

    def __str__(self) -> str:
        return (
            f"ID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo}"
            f"\nSetor: {self.setor}"

        )    
    

funcionario = Funcionario("123","Wagner Silva", Setor.VENDAS.value,Sexo.MASCULINO.value,19)

print(funcionario)