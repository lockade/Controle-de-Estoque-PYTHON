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
from Compra import Compra
from Item import Item
from FornecedorDAO import FornecedorDAO
from ProdutoDAO import ProdutoDAO
from datetime import datetime
import pathlib
import json

"""
Classe de acesso aos dados dos compras para selecionar, inserir, atualizar e deletar compras.
"""
class CompraDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/compras.json"

    @staticmethod
    def selecionar():        
        return CompraDAO.ler()        

    @staticmethod
    def inserir(compra : Compra):        
        compras = CompraDAO.selecionar()
        compra.id = 1 if len(compras) == 0 else max(c.id for c in compras) + 1                
        if compra.validar():            
            compras.append(compra)                
            compras = CompraDAO.parseJSON(compras)
            return CompraDAO.escrever(compras)
        return False    

    @staticmethod
    def parseJSON(compras: list):
        compras_dct = []        
        for compra in compras:            
            itens = []                        
            for item in compra.itens:
                item_dct = {
                    "id" : item.id,
                    "produto_id" : item.produto.id,
                    "quantidade" : item.quantidade,
                    "valor" : item.valor
                }
                itens.append(item_dct)
                compra_dct = {
                    "id" : compra.id,
                    "data" : compra.data.strftime('%Y-%m-%d %H:%M:%S'),
                    "fornecedor_id" : compra.fornecedor.id,
                    "itens" : itens
                }                                                
            compras_dct.append(compra_dct)
        return json.dumps(compras_dct)

    @staticmethod
    def escrever(compras : list):
        try:
            arquivo = open(CompraDAO.DEFAULT_FILE, "w", CompraDAO.BUFFER_SIZE)
            arquivo.write(compras)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(CompraDAO.DEFAULT_FILE, "r", CompraDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            compras = []                        
            for c in json.loads(conteudo):                
                compra = Compra()
                compra.id = c["id"]                
                compra.data = datetime.strptime(c["data"], '%Y-%m-%d %H:%M:%S')                
                fornecedor_id = c["fornecedor_id"]                
                compra.fornecedor = FornecedorDAO.selecionarPorID(fornecedor_id)                
                itens = c["itens"]
                for i in itens:                
                    item = Item()
                    item.id = i["id"]
                    produto_id = i["produto_id"]
                    item.produto = ProdutoDAO.selecionarPorID(produto_id)
                    item.quantidade = i["quantidade"]
                    item.valor = i["valor"] 
                    compra.itens.append(item)
                compras.append(compra)
            return compras
        except:
            pass
        return []