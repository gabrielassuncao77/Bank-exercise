import contas
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome 

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
    
    def __repr__(self):
        #class_name = self.__class__.__name__ (mesma coisa da linha abaixo)
        class_name = type(self).__name__
        return f'{class_name}: {self.nome!r}\nIdade: {self.idade!r}'

    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta


if __name__ == '__main__':
    c1 = Cliente('Gabigol', 19)
    c1.conta = contas.ContaCorrente(1, 222, 30, 100)
    print(c1)
    c2 = Cliente('Lucas', 40)
    c2.conta = contas.ContaPoupanca(3, 34, 200)
    print(c2)