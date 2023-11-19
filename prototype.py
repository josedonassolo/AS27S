from copy import deepcopy

# Interface Protótipo
class BancoDeDadosPrototype:
    def clone(self):
        pass

# Classe Protótipo Concreta
class BancoDeDados(BancoDeDadosPrototype):
    def __init__(self, host, port, dbname, user, pwd):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.pwd = pwd

    def clone(self):
        return deepcopy(self)

# Cliente
class CatalogoDeBancos:
    def __init__(self):
        self.bancos = {}

    def adicionar_banco(self, nome, banco_prototype):
        self.bancos[nome] = banco_prototype

    def obter_copia_banco(self, nome, host, port, dbname, user, pwd):
        banco_prototype = self.bancos.get(nome)
        if banco_prototype:
            novo_banco = banco_prototype.clone()
            novo_banco.host = host
            novo_banco.port = port
            novo_banco.dbname = dbname
            novo_banco.user = user
            novo_banco.pwd = pwd
            return novo_banco
        else:
            raise ValueError("Banco de dados não encontrado no catálogo.")

# Exemplo de Uso
catalogo = CatalogoDeBancos()

banco_prototype = BancoDeDados("localhost", 5432, "mydb", "user", "password")

catalogo.adicionar_banco("BancoPadrao", banco_prototype)

banco_personalizado = catalogo.obter_copia_banco("BancoPadrao", "customhost", 8080, "customdb", "customuser", "custompwd")

print(f"Host: {banco_personalizado.host}")
print(f"Port: {banco_personalizado.port}")
print(f"DB Name: {banco_personalizado.dbname}")
print(f"User: {banco_personalizado.user}")
print(f"Password: {banco_personalizado.pwd}")