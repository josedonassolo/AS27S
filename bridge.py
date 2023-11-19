from abc import ABC, abstractmethod


class SGBD(ABC):
    @abstractmethod
    def obter_nome(self) -> str:
        pass


class SGBDMySQL(SGBD):
    def obter_nome(self) -> str:
        return "MySQL"

class SGBDPostgreSQL(SGBD):
    def obter_nome(self) -> str:
        return "PostgreSQL"


class BancoDeDados(ABC):
    def __init__(self, sgbd: SGBD):
        self.sgbd = sgbd

    @abstractmethod
    def obter_informacoes(self) -> str:
        pass


class BancoA(BancoDeDados):
    def obter_informacoes(self) -> str:
        return f"Banco A ({self.sgbd.obter_nome()})"

class BancoB(BancoDeDados):
    def obter_informacoes(self) -> str:
        return f"Banco B ({self.sgbd.obter_nome()})"


banco_mysql = BancoA(SGBDMySQL())
banco_postgresql = BancoB(SGBDPostgreSQL())

print(banco_mysql.obter_informacoes())
print(banco_postgresql.obter_informacoes())