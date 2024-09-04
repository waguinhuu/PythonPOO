#

class ContaBancaria:
    def __init__(self, banco: str,agencia: str,numeroDaConta: str,
                 tipoDaConta: str, saldoAtual: float, limiteDisponivel: float) -> None:

        self.banco = banco
        self.agencia = agencia
        self.numeroDaConta = numeroDaConta
        self.tipoDaConta = tipoDaConta
        self.saldoAtua = saldoAtual
        self.limiteDisponivel = limiteDisponivel

    def __str__(self) -> str:
        return (
            f"\nBanco: {self.banco}"
            f"\nAgencia: {self.agencia}"
            f"\nNúmero da conta: {self.numeroDaConta}"
            f"\nTipo da conta: {self.tipoDaConta}"
            f"\nSaldo atual: {self.saldoAtua}"
            f"\nLimite disponivel: {self.limiteDisponivel}"

        )

class Funcionario:
    def __init__(self,codigoDoFuncionario: str,nome: str,endereco: str,
                 telefone: str,email: str,contaBanco: ContaBancaria) -> None:

        self.codigoDoFuncionario = codigoDoFuncionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.contaBanco = contaBanco

    def __str__(self) -> str:
        return (
            f"\nCodigoDoFuncionario: {self.codigoDoFuncionario}"
            f"\nNome: {self.nome}"
            f"\nEndereço: {self.endereco}"
            f"\nTelefone: {self.telefone}"
            f"\n\nContaBanco: {self.contaBanco}"

        )

funcionario = Funcionario("123","Wagner","Rua A",
                          "719827763623","wagner@gmail.com",
                          ContaBancaria("Santander","1244445","00000","Corrente",7500,9000))


print(funcionario)