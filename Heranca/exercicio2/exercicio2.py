from abc import ABC,abstractmethod

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
            f"\nComplemento {self.complemento}"
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
                f"\nSalario final: {self.salario_final()}"
                f"\nEndereço: {self.endereco}"
                )

class Engenheiro(Funcionario):
    BONIFICACAO = 1.1

    def __init__(self, nome: str, telefone: str, email: str,salario: float, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email,salario, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCrea: {self.crea}\n"
        )



class Medico(Funcionario):
    BONIFICACAO = 1.3

    def __init__(self,nome: str, telefone: str, email: str,salario: float, endereco: Endereco, crm: str) -> None:
        super().__init__(nome,telefone,email,salario,endereco)
        self.crm = crm

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"\nCRM: {self.crm}"
        )



engenheiro = Engenheiro("Wagner","7983445733","wg@gmail.com",1000,
                        Endereco("Rua A","88","sla","43900-000","SFC"),"2321")

medico = Medico("Paulo","719383392","pl@gmail.com",1000,
                Endereco("Rua B","00","nnsei","28900-000","STA"),"92981")

print(engenheiro)
print(medico)