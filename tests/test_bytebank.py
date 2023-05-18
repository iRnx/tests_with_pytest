import pytest
from codigo.bytebank import Funcionario
from pytest import mark

class Test_Class:

    def test_quando_idade_recebe_1998_05_16_deve_retornar_24(self):
        """Give-When-Then"""

        entrada = '1998-05-16' # Given-Contexto
        esperado = 24

        funcionario_teste = Funcionario('Renan', entrada, 1000)
        resultado = funcionario_teste.idade() # when-ação

        assert resultado == esperado # Then-desfecho


    def test_quando_idade_recebe_1998_05_25_deve_retornar_25(self):
        """Give-When-Then"""

        entrada = '1998-05-25' # Given-Contexto
        esperado = 25

        funcionario_teste = Funcionario('Renan', entrada, 1000)
        resultado = funcionario_teste.idade() # when-ação
        
        assert resultado == esperado # Then-desfecho


    def test_quando_sobrenome_recebe_Renan_Gustavo_deve_retornar_Gustavo(self):
        entrada = ' Renan Gustavo ' #Given
        esperado = 'Gustavo'

        renan = Funcionario(nome=entrada, data_nascimento='1998-07-01', salario=1000)
        resultado = renan.sobrenome() # when

        assert resultado == esperado
        

    # TDD- Test Drive Development
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_900000(self):
        entrada_salario = 100000 # given
        entrada_nome = 'Voldemort'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, data_nascimento='1998-07-01', salario=entrada_salario)
        funcionario_teste.decrescimo_salario() # when 
        resultado = funcionario_teste.salario
        

        assert resultado == esperado # then


    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # given
        esperado = 100

        rnx = Funcionario('Rnx', data_nascimento='1998-07-01', salario=entrada) 
        resultado = rnx.calcular_bonus() # when
        

        assert resultado == esperado # then


    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 # given

            rnx = Funcionario('Rnx', data_nascimento='1998-07-01', salario=entrada) 
            resultado = rnx.calcular_bonus() # when
            

            assert resultado # then 


    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = 'Slytherin', '1998-07-01', 5000 # given

    #     esperado = f'Funcionario Slytherin, 1998-07-01, 5000'

    #     slytherin = Funcionario(nome, data_nascimento, salario) 
    #     resultado = slytherin.__str__() # when
        

    #     assert resultado == esperado # then







