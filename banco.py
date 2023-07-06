import contas
import Pessoas


class Banco:
    def __init__(self, branch=None, clients=None, accounts=None):
        self.branch = branch or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.branch:
            print('Agencia: ', self.branch)
            return True
        print('Agencia não encontrada.')
        return False

    def _checa_conta(self, conta):
        if conta in self.accounts:
            print('Conta encontrada!')
            return True
        print('Conta não registrada no sistema.')
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clients:
            print(cliente)
            return True
        print('Cliente não encontrado no sistema.')
        return False

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'

    def autenticar(self, cliente, conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)


if __name__ == '__main__':

    banco = Banco()
    c2 = Pessoas.Cliente('Lucas', 40)
    cp2 = accounts.ContaPoupanca(111, 200, 100)
    c2.conta = cp2
    banco.clients.append(c2)
    banco.accounts.append(cp2)
    banco.branch.append(111)

    if banco.autenticar(c2, cp2):
        cp2.deposito(1000)
        c2.conta.sacar(10)
        