#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
from Venda import Venda
from Item import Item
from Funcionario import Funcionario
from FuncionarioDAO import FuncionarioDAO
from ClienteDAO import ClienteDAO
from ProdutoDAO import ProdutoDAO
from datetime import datetime
import pathlib
import json

"""
Classe de acesso aos dados das vendas para selecionar, inserir, atualizar e deletar vendas.
"""
class VendaDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/vendas.json"

    @staticmethod
    def selecionar():        
        return VendaDAO.ler()        

    @staticmethod
    def inserir(venda : Venda):   
        
        vendas = VendaDAO.selecionar()
        venda.id = 1 if len(vendas) == 0 else max(c.id for c in vendas) + 1                
        if venda.validar():
            vendas.append(venda)
            
            vendas = VendaDAO.parseJSON(vendas)
            return VendaDAO.escrever(vendas)
        return False    

    @staticmethod
    def parseJSON(vendas: list):
        vendas_dct = []  
        for venda in vendas:            
            itens = []   
            for item in venda.itens:
                item_dct = {
                    "id" : item.id,
                    "produto_id" : item.produto.id,
                    "quantidade" : item.quantidade,
                    "valor" : item.valor
                }
                itens.append(item_dct)
                
                venda_dct = {
                    "id" : venda.id,
                    "data" : venda.data.strftime('%Y-%m-%d %H:%M:%S'),
                    "funcionario_id" : venda.funcionario.id,
                    "cliente_id" : venda.cliente.id,
                    "itens" : itens
                }
            vendas_dct.append(venda_dct)
        return json.dumps(vendas_dct)

    @staticmethod
    def escrever(vendas : list):
        try:
            arquivo = open(VendaDAO.DEFAULT_FILE, "w", VendaDAO.BUFFER_SIZE)
            arquivo.write(vendas)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(VendaDAO.DEFAULT_FILE, "r", VendaDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            vendas = []                        
            for c in json.loads(conteudo):                
                venda = Venda()
                venda.id = c["id"]                
                venda.data = datetime.strptime(c["data"], '%Y-%m-%d %H:%M:%S')                
                funcionario_id = c["funcionario_id"]                
                venda.funcionario = FuncionarioDAO.selecionarPorID(funcionario_id)                
                cliente_id = c["cliente_id"]                
                venda.cliente = ClienteDAO.selecionarPorID(cliente_id)                
                itens = c["itens"]
                for i in itens:                
                    item = Item()
                    item.id = i["id"]
                    produto_id = i["produto_id"]
                    item.produto = ProdutoDAO.selecionarPorID(produto_id)
                    item.quantidade = i["quantidade"]
                    item.valor = i["valor"] 
                    venda.itens.append(item)
                vendas.append(venda)
            return vendas
        except:
            pass
        return []