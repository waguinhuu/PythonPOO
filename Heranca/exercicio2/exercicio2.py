from abc import ABC,abstractmethod
from cgitb import reset


class Endereco:
    def __init__(self, logradouro: str, numero: str,
                 complemento: str, cep: str, cidade: str) -> None:

        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\ncomplemento {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
        )


class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str,salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco


    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
                f"Nome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSalario: {self.salario}"
                f"\nEndereço: {self.endereco}"
                f"\nSalario: {self.salario_final()}"
                )

class Engenheiro(Funcionario):
    BONIFICACAO = 1.1

    def __init__(self, nome: str, telefone: str, email: str,salario: float, endereco: Endereco, crea: str) -> None:
        super.__init__(nome, telefone, email,salario, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCrea: {self.crea}"
        )



class Medico(Funcionario):
    def __init__(self,nome: str, telefone: str, email: str,salario: float, endereco: Endereco, crm: str) -> None:
        self.crm = crm