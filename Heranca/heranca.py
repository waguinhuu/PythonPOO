from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nSalario: {self.salario}"
            f"\nSalario final: {self.salario_final()}"
        )


class Motoboy(Funcionario):
    # Acréscimo de 10%
    BONIFICACAO = 1.1

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado


class Engenheiro(Funcionario):
    # Acréscimo de 20%
    BONIFICACAO = 1.2

    def __init__(self, nome: str, salario: float,crea: str) -> None:
        super().__init__(nome,salario)
        self.crea = crea

    def salario_final(self) -> float:
            resultado = self.salario * self.BONIFICACAO
            return resultado
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}")

motoboy = Motoboy("Wagner",1000)
print(motoboy)

engenheiro = Engenheiro("Marta",1000,"453453")
print(engenheiro)