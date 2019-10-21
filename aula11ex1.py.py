from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente (Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.salario * 2


class Assistente (Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.salario


class Vendedor (Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario + self.comissao


gerente = Gerente("Ademir", "00123456", 8000.00)
assistente = Assistente("Camila", "4568912", 4000.00)
vendedor = Vendedor("Jubscleysu", "0125895", 1500.00, 2000.00)
funcionarios = [gerente, assistente, vendedor]
for i in funcionarios:
    print(i.calcular_salario())
