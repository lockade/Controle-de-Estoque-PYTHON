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
from datetime import datetime
from Venda import Venda
from Funcionario import Funcionario
from VendaDAO import VendaDAO
from Item import Item
from ClienteDAO import ClienteDAO
from FuncionarioDAO import FuncionarioDAO
from ProdutoDAO import ProdutoDAO

class VendaView:

    @staticmethod
    def visualizarVendas(vendas : list = None):          
        if vendas == None:
            vendas = VendaDAO.selecionar()
        print("-" * 7 + " Vendas " + "-" * 7)#        
        vendas = VendaDAO.selecionar()   
        for venda in vendas:
            valor_total = 0.0
            
            if(venda.funcionario == None):
                funcionario = "Não informado"
            else:
                funcionario = venda.funcionario.nome
                
            if(venda.cliente == None):
                cliente = "Não informado"
            else:
                cliente = venda.cliente.nome
                
                
            print(f"ID: {venda.id} | Data: {venda.data} | Funcionário: {funcionario} | Cliente: {cliente}")
            for item in venda.itens:
                print(f"Item ID: {item.id} ")
                
                if(item.produto == None):
                    produto = "Não informado"
                else:
                    produto = item.produto.nome
                    
                print(f"\tProduto: {produto}\n\tQuantidade: {item.quantidade}.\n\tValor: {item.valor:.2f}")
                valor_total += item.quantidade * item.valor
            print(f"Valor total: R$ {valor_total:.2f}")
            print("-----------------------------------------")

        
        input("Pressione <Enter> para continuar.")

    @staticmethod
    def listar_produtos(produtos : list = None):
        if produtos == None:
            produtos = ProdutoDAO.selecionar()
        print("-" * 7 + " Produtos " + "-" * 7)#        
        for p in produtos:  
            if(p.categoria == None):
                categoria = "Não Informada"
            else:
                categoria = p.categoria.nome
        
            print(f"ID: {p.id} | Nome: {p.nome} | Valor: {p.valor:.2f} | Quantidade em Estoque: {p.quantidade_estoque} | Categoria: {categoria}")

    @staticmethod
    def listar_funcionarios(funcionarios : list = None):
        if funcionarios == None:
            funcionarios = FuncionarioDAO.selecionar()
        print("-" * 7 + " Funcionários " + "-" * 7)              
        for f in funcionarios:
            print(f"ID: {f.id} | Nome: {f.nome} | Registro: {f.registro}")

    @staticmethod
    def listar_clientes(clientes : list = None):
        if clientes == None:
            clientes = ClienteDAO.selecionar()
            
        print("-" * 7 + " Clientes " + "-" * 7)
        for c in clientes:
            if c.cidade == None:
                cidade = "Não informada"
            else:
                cidade = c.cidade.nome + " - "  + c.cidade.UF
            
            print(f"ID: {c.id} | Nome: {c.nome} | CPF: {c.CPF} | Logradouro: {c.logradouro} | Número: {c.numero} | CEP: {c.CEP} | Cidade: {cidade}".format(c.id, c.nome, c.CPF, c.logradouro, c.numero, c.CEP, cidade))
              
        

    @staticmethod
    def inserirVenda():
        print(" Efetuar Venda ".center(60, "%"))
        venda = Venda()
        venda.itens = []    
        resposta = "s"
        item_id = 1
        produtos = ProdutoDAO.selecionar()
        clientes = ClienteDAO.selecionar()
        funcionarios = FuncionarioDAO.selecionar()    
        while(1):
            print("-- Item: {item_id} --") 
            VendaView.listar_produtos(produtos)
            produto_id = int(input("Informe o ID do produto a ser vendido: "))            
            produto = list(filter(lambda x: x.id == produto_id, produtos))[0]
            item = Item()
            item.id = item_id
            item.produto = produto        
            item.quantidade = int(input("Informe a quantidade a ser vendida: "))        
            item.valor = produto.valor
            venda.itens.append(item)
            item_id += 1
            
            if(VendaView.opcaoSimNao("Adicionar mais Itens ? Sim ou Não: ") == False):
                break
            
        
        VendaView.listar_clientes(clientes)
        
        while(1):
            cliente_id = int(input("Informe o ID do cliente: ")) 
            venda.cliente = ClienteDAO.selecionarPorID(cliente_id)
            
            if(venda.cliente != None):
                break
            print("ID Inválido")
        
        VendaView.listar_funcionarios(funcionarios)
        
        while(1):
            funcionario_id = int(input("Informe o ID do funcionário: "))            
            venda.funcionario = FuncionarioDAO.selecionarPorID(funcionario_id)
        
            if(venda.funcionario != None):
                break
            print("ID Inválido")
        
        venda.data = datetime.now()
        
        if VendaDAO.inserir(venda):
            for item in venda.itens:
                ProdutoDAO.atualizar_estoque(item.produto.id, item.quantidade, ProdutoDAO.ATUALIZA_VENDA)
            print("Venda efetuada com sucesso!") 
            VendaView.visualizarVendas()
        else:
            print("Falha ao efetuar a venda.")
        input("Pressione <Enter> para Continuar")
        
    @staticmethod
    def opcaoSimNao(texto : str):
        while(1):
            try:
                resposta = input(texto).lower()
                if(resposta == "sim"):
                    return True
                elif(resposta == "nao" or resposta == "não"):
                    return False
            except:
                return False

