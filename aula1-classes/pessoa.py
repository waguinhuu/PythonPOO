from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} ja esta falando')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao esta falando')
            return
        print(f'{self.nome} esta parou de falar')
        self.falando = False


    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return

        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return

        print(f'{self.nome} está comendo {alimento}. ')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    #Clone do objeto
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)

    @staticmethod
    def geraId():
        rand = randint(1, 100)
        return rand

