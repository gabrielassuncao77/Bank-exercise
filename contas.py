from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
       

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def deposito(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Depósito de: {valor}')
        return self.saldo

    def detalhes(self, msg='') -> None:
        f'Saldo é: {self.saldo:.2f}'
        print('----')
    

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_sacada = self.saldo - valor

        if valor_pos_sacada >= 0:
            self.saldo -= valor
            print(f'Saque: {valor}')
            print(f'Saldo: {self.saldo}')
            return self.saldo
        
        print(f'Valor negado {valor}')
        print(f'Não foi possivél realizar saque. Saldo insuficiente: {self.saldo}')
        return self.saldo






class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_sacada = self.saldo - valor
        limite = -self.limite

        if valor_pos_sacada >= limite:
            self.saldo -= valor
            limite -= valor
            print(f'SAQUE, {valor}')
            print(f'SALDO, {self.saldo}')
            return self.saldo        

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
    
    
if __name__ == '__main__':
    c1 = ContaPoupanca(222, 333, 100)
    c1.sacar(100)
    c1.deposito(20)
    c1.sacar(100)
    c2 = ContaCorrente(111, 222, 200, 200)
    c2.sacar(200)
    c2.sacar(200)

    
