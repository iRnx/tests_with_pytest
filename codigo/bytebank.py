from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario


    @property
    def nome(self):
        return self._nome


    @property
    def salario(self):
        return self._salario


    def idade(self):
        data_atual = date.today()
        ano_atual = data_atual.year
        mes_atual = data_atual.month
        dia_atual = data_atual.day
        
        ano_nascimento, mes_nascimento, dia_nascimento = map(int, self._data_nascimento.split('-'))

        idade = ano_atual - ano_nascimento

        if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and not dia_nascimento >= dia_atual):
            idade -= 1

        return idade
    

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]
    

    def _eh_diretor(self):
        sobrenomes = ['Voldemort', 'Rnx', 'slytherin', 'dumbledore']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
        


    def decrescimo_salario(self):
        if self._eh_diretor():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo


    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor


    def __str__(self):
        return f'Funcionario {self._nome}, {self._data_nascimento}, {self._salario}'
