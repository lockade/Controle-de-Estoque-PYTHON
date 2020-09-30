__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "View")
sys.path.insert(0, "Controller")
from Funcionario import Funcionario
from FuncionarioDAO import FuncionarioDAO

class FuncionarioView:

    @staticmethod
    def listar(funcionarios: list = None):          
        if funcionarios == None:
            funcionarios = FuncionarioDAO.selecionar()       
        pausar = True
        print(" Funcionários ".center(60, "#"))        
        for f in funcionarios:                                 
            print("ID: {}. Nome: {}. Registro: {}. salario: {:.2f}.".format(f.id, f.nome, f.registro, f.salario))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def adicionar():
        print(" Adicionar Funcionário ".center(60, "%"))
        funcionario = Funcionario()
        funcionario.nome = input("Nome: ")    
        funcionario.registro = input("Registro: ")    
        funcionario.salario = float(input("Salário: "))
        if not FuncionarioDAO.existe(funcionario.registro):
            if FuncionarioDAO.inserir(funcionario):
                print("Funcionário cadastrado com sucesso!")
                FuncionarioView.listar()
            else:
                print("Falha ao cadastrar o funcionário.")
        else:
            print("Funcionário já cadastrado.")               
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Funcionário ".center(60, "%"))
        funcionarios = FuncionarioDAO.selecionar()
        FuncionarioView.listar(funcionarios)
        funcionario_id = int(input("Informe o ID do funcionário a ser atualizado: "))
        funcionario = list(filter(lambda x: x.id == funcionario_id, funcionarios))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            funcionario.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar registro [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:        
            registro = input("Informe o novo registro: ")
            if FuncionarioDAO.existe(registro):
                print("O registro já está vinculado a outro funcionário.")
            else:
                funcionario.registro = registro
        entrada = input("Atualizar salário [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            funcionario.salario = float(input("Informe o novo salário: "))
        if FuncionarioDAO.atualizar(funcionario):
            print("Funcionário atualizado com sucesso!")       
            FuncionarioView.listar()
        else:
            print("Falha ao atualizar o funcionário. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Funcionário ".center(60, "%"))
        FuncionarioView.listar()
        funcionario_id = int(input("Informe o ID do funcionário a ser removido: "))    
        if FuncionarioDAO.deletar(funcionario_id):
            print("Funcionário removido com sucesso!")    
            FuncionarioView.listar()
        else:
            print("Falha ao remover o funcionário. Contate o administrador do sistema!")    
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")