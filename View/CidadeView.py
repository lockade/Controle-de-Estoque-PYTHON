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
from Cidade import Cidade
from CidadeDAO import CidadeDAO

class CidadeView:

    @staticmethod
    def listar(cidades: list = None):          
        if cidades == None:
            cidades = CidadeDAO.selecionar()
            pausar = True
        print(" Cidades ".center(60, "#"))        
        for c in cidades:
            print("ID: {}. Nome: {}. UF: {}.".format(c.id, c.nome, c.UF))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def adicionar():
        print(" Adicionar Cidade ".center(60, "%"))
        cidade = Cidade()
        cidade.nome = input("Nome: ")
        cidade.UF = input("UF: ")    
        if not CidadeDAO.existe(cidade.nome, cidade.UF):
            if CidadeDAO.inserir(cidade):
                print("Cidade cadastrada com sucesso!")
                CidadeView.listar()
            else:
                print("Falha ao cadastrar a cidade.")
        else:
            print("Cidade já cadastrada.")        
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Cidade ".center(60, "%"))
        cidades = CidadeDAO.selecionar()
        CidadeView.listar(cidades)
        cidade_id = int(input("Informe o ID da cidade a ser atualizada: "))    
        cidade = list(filter(lambda x: x.id == cidade_id, cidades))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cidade.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar UF [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cidade.UF = input("Informe a nova UF: ")
        if CidadeDAO.atualizar(cidade):
            print("Cidade atualizada com sucesso!")    
            CidadeView.listar()
        else:
            print("Falha ao atualizar a cidade. Contate o administrador do sistema!")   
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Cidade ".center(60, "%"))
        CidadeView.listar()   
        cidade_id = int(input("Informe o ID da cidade a ser removida: "))    
        if CidadeDAO.deletar(cidade_id):
            print("Cidade removida com sucesso!")    
            CidadeView.listar()   
        else:
            print("Falha ao remover a cidade. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")