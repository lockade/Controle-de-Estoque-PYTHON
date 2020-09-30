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
from Compra import Compra
from CompraDAO import CompraDAO
from Item import Item
from FornecedorDAO import FornecedorDAO
from ProdutoDAO import ProdutoDAO
from datetime import datetime

class CompraView:

    @staticmethod
    def visualizarCompras(compras : list = None):          
        if compras == None:
            compras = CompraDAO.selecionar()
        print("-" * 7 + " Compras " + "-" * 7)#
        for compra in compras:
            
            valor_total = 0.0
            
            if(compra.fornecedor == None):
                fornecedor = "Não informado"
            else:
                fornecedor = compra.fornecedor.nome
                
            print("\n" + "-" * 4 + f" Fornecedor: {fornecedor} " + "-" * 4)#
             
            print(f"ID: {compra.id} | Data: {compra.data} | Fornecedor : {fornecedor}")
            
            for item in compra.itens:
                if(item.produto == None):
                    produto = "Não Informado"
                else:
                    produto = item.produto.nome
                
                print(f"Produto: {produto} | Quantidade: {item.quantidade} | Valor: {item.valor}")
                valor_total += item.quantidade * item.valor
            print(f"Valor total: R$ {valor_total:.2f}")


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
    def listar_fornecedores(fornecedores : list = None):
        if fornecedores == None:
            fornecedores = FornecedorDAO.selecionar()
        
        print("-" * 7 + " Fornecedores " + "-" * 7)#                
        for f in fornecedores:
            print(f"ID: {f.id} | Nome: {f.nome} | CNPJ: {f.CNPJ}")

    @staticmethod
    def inserirCompra():
        print("-" * 7 + " Efetuar Compra " + "-" * 7)#  
        compra = Compra()
        compra.itens = []
        item_id = 1
        produtos = ProdutoDAO.selecionar()
        fornecedores = FornecedorDAO.selecionar()
        while(1):
            print(f"Adicionando Item ID: {item_id}")
            CompraView.listar_produtos(produtos)
            produto_id = int(input("Informe o ID do produto a ser comprado: "))            
            produto = ProdutoDAO.selecionarPorID(produto_id)
            
            if(produto == None):
                print("ID não existe")
                continue
            
            
            
            item = Item()
            item.valor = float(input("Valor Unitário: "))
            item.id = item_id
            item.produto = produto        
            item.quantidade = int(input("Informe a quantidade a ser comprada: ")) 
            
            compra.itens.append(item)
            item_id += 1
            
            if(CompraView.opcaoSimNao("Adicionar mais Itens ? Sim ou Não: ") == False):
                break
        
        CompraView.listar_fornecedores(fornecedores)#exibindo lista de fornecedores 
        fornecedor_id = int(input("Informe o ID do fornecedor: "))      
        compra.fornecedor = FornecedorDAO.selecionarPorID(fornecedor_id)
        compra.data = datetime.now()#pega data atual para registrar venda
        if CompraDAO.inserir(compra):
            for item in compra.itens:
                ProdutoDAO.atualizar_estoque(item.produto.id, item.quantidade, ProdutoDAO.ATUALIZA_COMPRA)
            print("Compra efetuada com sucesso!")
        else:
            print("Falha ao efetuar a compra.")
        input("Pressione <Enter> para continuar.")# vamos deixar isso ?
        
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