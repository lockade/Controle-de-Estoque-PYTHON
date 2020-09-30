__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
sys.path.insert(0, "Controller")
from Cliente import Cliente
from ClienteDAO import ClienteDAO
from CidadeDAO import CidadeDAO

class ClienteView:

    @staticmethod
    def listar(clientes : list = None):          
        if clientes == None:
            clientes = ClienteDAO.selecionar()       
            pausar = True
        print(" Clientes ".center(60, "#"))        
        for c in clientes:
            cidade = "Não informada" if c.cidade == None else c.cidade.nome + " - "  + c.cidade.UF
            print("ID: {}. Nome: {}. CPF: {}. Logradouro: {}. Número: {}. CEP: {}. Cidade: {}.".format(c.id, c.nome, c.CPF, c.logradouro, c.numero, c.CEP, cidade))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def listar_cidades(cidades : list = None):
        if cidades == None:
            cidades = CidadeDAO.selecionar()       
        pausar = True
        print(" Cidades ".center(60, "#"))        
        for c in cidades:
            print("ID: {}. Nome: {}. UF: {}.".format(c.id, c.nome, c.UF))
        print("#" * 60)         
        if pausar: 
            pass #esse input atrapalhava na hora de inserir um cliente, estava falando que iria voltar ao menu
            #input("Pressione <Enter> para voltar ao menu.")        

    @staticmethod
    def adicionar():
        print(" Adicionar Cliente ".center(60, "%"))
        cliente = Cliente()
        cliente.nome = input("Nome: ")
        cliente.CPF = input("CPF: ")        
        cliente.logradouro = input("Logradouro: ")
        cliente.numero = int(input("Número: "))
        cliente.CEP = input("CEP: ")
        cidades = CidadeDAO.selecionar()
        ClienteView.listar_cidades(cidades)
        cidade_id = int(input("Informe o ID da cidade: "))    
        cliente.cidade = list(filter(lambda x : x.id == cidade_id, cidades))[0]
        if not ClienteDAO.existe(cliente.CPF):
            if ClienteDAO.inserir(cliente):
                print("Cliente cadastrado com sucesso!")
                ClienteView.listar()
            else:
                print("Falha ao cadastrar o cliente.")
        else:
            print("Cliente já cadastrado.")        
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Cliente ".center(60, "%"))
        clientes = ClienteDAO.listar()
        ClienteView.listar(clientes)
        cliente_id = int(input("Informe o ID do cliente a ser atualizado: "))    
        cliente = list(filter(lambda x: x.id == cliente_id, clientes))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar CPF [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.CPF = input("Informe o novo CPF: ")
        entrada = input("Atualizar logradouro [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.logradouro = input("Informe o novo logradouro: ")
        entrada = input("Atualizar número [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.numero = int(input("Informe o novo número: "))
        entrada = input("Atualizar CEP [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.CEP = input("Informe o novo CEP: ")
        entrada = input("Atualizar cidade [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cidades = CidadeDAO.selecionar()
            ClienteView.listar_cidades(cidades)
            cidade_id = int(input("Informe o ID da nova cidade: "))        
            cliente.cidade = list(filter(lambda x : x.id == cidade_id, cidades))[0]
        if ClienteDAO.atualizar(cliente):
            print("Cliente atualizado com sucesso!")                    
            ClienteView.listar()
        else:
            print("Falha ao atualizar o cliente. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Cliente ".center(60, "%"))        
        ClienteView.listar()
        Cliente_id = int(input("Informe o ID do cliente a ser removido: "))    
        if ClienteDAO.deletar(Cliente_id):
            print("Cliente removido com sucesso!")    
            ClienteView.listar()
        else:
            print("Falha ao remover o cliente. Contate o administrador do sistema!")    
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")
