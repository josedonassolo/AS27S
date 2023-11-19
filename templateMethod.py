from abc import ABC, abstractmethod

class ExecucaoDeCodigo(ABC):
    def executar(self, comando):
        self.pre_execucao()
        resultado = self.executar_codigo(comando)
        self.pos_execucao()
        return resultado

    @abstractmethod
    def executar_codigo(self, comando):
        pass

    def pre_execucao(self):
        print("Realizando ações antes da execução.")

    def pos_execucao(self):
        print("Realizando ações após a execução.")

class ExecucaoDDL(ExecucaoDeCodigo):
    def executar_codigo(self, comando):
        print(f"Executando DDL: {comando}")

class ExecucaoDML(ExecucaoDeCodigo):
    def executar_codigo(self, comando):
        print(f"Executando DML: {comando}")

ddl_executor = ExecucaoDDL()
dml_executor = ExecucaoDML()

comando_ddl = "CREATE TABLE exemplo (id INT, nome VARCHAR(255));"
comando_dml = "INSERT INTO exemplo (id, nome) VALUES (1, 'Exemplo');"

ddl_executor.executar(comando_ddl)
print("-" * 30)
dml_executor.executar(comando_dml)