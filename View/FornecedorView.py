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
from Fornecedor import Fornecedor
from FornecedorDAO import FornecedorDAO

class FornecedorView:

    @staticmethod
    def listar(fornecedores: list = None):          
        if fornecedores == None:
            fornecedores = FornecedorDAO.selecionar()
        pausar = True
        print(" Fornecedores ".center(60, "#"))
        for f in fornecedores:                                 
            print("ID: {}. Nome: {}\n       CNPJ: {}".format(f.id, f.nome, f.CNPJ))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def adicionar():
        print(" Adicionar Fornecedor ".center(60, "%"))
        fornecedor = Fornecedor()
        fornecedor.nome = input("Nome: ")        
        fornecedor.CNPJ = input("CNPJ: ")        
        if not FornecedorDAO.existe(fornecedor.CNPJ):
            if FornecedorDAO.inserir(fornecedor):
                print("Fornecedor cadastrado com sucesso!")
                FornecedorView.listar()
            else:
                print("Falha ao cadastrar o fornecedor!")
        else:
            print("Fornecedor já cadastrado.")        
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Fornecedor ".center(60, "%"))
        fornecedores = FornecedorDAO.selecionar()
        FornecedorView.listar(fornecedores)
        fornecedor_id = int(input("Informe o id do fornecedor a ser atualizado: "))
        fornecedor = list(filter(lambda x: x.id == fornecedor_id, fornecedores))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            fornecedor.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar CNPJ [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:        
            CNPJ = input("Informe o novo CNPJ: ")
            if FornecedorDAO.existe(CNPJ):
                print("O CNPJ já está vinculado a outro fornecedor.")
            else:
                fornecedor.CNPJ = CNPJ    
        if FornecedorDAO.atualizar(fornecedor):
            print("Fornecedor atualizado com sucesso!")                   
            FornecedorView.listar()
        else:
            print("Falha ao atualizar o fornecedor. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Fornecedor ".center(60, "%"))
        FornecedorView.listar()
        fornecedor_id = int(input("Informe o ID do fornecedor a ser removido: "))    
        if FornecedorDAO.deletar(fornecedor_id):
            print("Fornecedor removido com sucesso!")                
            FornecedorView.listar()
        else:
            print("Falha ao remover o fornecedor. Contate o administrador do sistema!")    
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")