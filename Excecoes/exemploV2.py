import os

os.system("cls || clear")

# Criando minha própria exceção.
class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class ValorInvalidoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 900  # Atributo protegido.

    # Semelhante ao getSaldo()
    @property
    def saldo(self):
        return self._saldo

    def sacar(self) -> str:
        valor_saque = input("Digite o valor que deseja sacar: ")

        try:
            valor_saque = self.__verificar_valor_invalido(valor_saque)
            self.__verificar_sacar(valor_saque)
            self.__verificar_valor_negativo(valor_saque)
        except (SaldoInsuficienteError, ValorNegativoError, ValorInvalidoError) as erro:
            return f"Prezado cliente: {erro}"

        self._saldo -= valor_saque
        return f"Saque realizado com sucesso."

    def __verificar_sacar(self, valor) -> None:  # Método privado.
        if valor > self._saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente. Seu saldo atual é de R$ {self._saldo}.")

    def __verificar_valor_negativo(self, valor):
        if valor < 0:
            raise ValorNegativoError("Valor negativo.")

    def __verificar_valor_invalido(self, valor) -> float:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            raise ValorInvalidoError("Valor inválido. Por favor, insira um número válido.")

    def depositar(self):
        valor_deposito = input("Digite o valor que deseja depositar: ")
        try:
            valor_deposito = self.__verificar_valor_invalido(valor_deposito)
            self.__verificar_valor_negativo(valor_deposito)
        except (ValorInvalidoError, ValorNegativoError) as erro:
            return f"Prezado cliente: {erro}"

        self._saldo += valor_deposito
        return f"Depósito realizado com sucesso."


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass

# Instanciando classe.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

print(f"Número da conta: {conta_corrente.numero_conta}")
print(f"Saldo: {conta_corrente.saldo}")

# Sacar com saldo insuficiente.
# print("Conta corrente")
# print(conta_corrente.sacar())
# print(f"Saldo: {conta_corrente.saldo}")

print("Conta poupança")
print(conta_poupanca.sacar())
print(f"Saldo: {conta_poupanca.saldo}")

print("Depositar.")
print(conta_poupanca.depositar())
print(conta_poupanca.saldo)
