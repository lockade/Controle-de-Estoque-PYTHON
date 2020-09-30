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
from Produto import Produto
from CategoriaDAO import CategoriaDAO
import pathlib
import json

"""
Classe de acesso aos dados dos produtos para selecionar, inserir, atualizar e deletar produtos.
"""
class ProdutoDAO:
    
    ATUALIZA_VENDA = 0
    ATUALIZA_COMPRA = 1

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/produtos.json"

    @staticmethod
    def selecionar():        
        return ProdutoDAO.ler() 

    @staticmethod
    def selecionarPorID(produto_id : int):
        for produto in ProdutoDAO.selecionar():
            if produto.id == produto_id:
                return produto
        return None       

    @staticmethod
    def inserir(produto : Produto):        
        produtos = ProdutoDAO.selecionar()
        produto.id = 1 if len(produtos) == 0 else max(c.id for c in produtos) + 1
        if produto.validar():
            produtos.append(produto)                
            produtos = ProdutoDAO.parseJSON(produtos)
            return ProdutoDAO.escrever(produtos)
        return False

    @staticmethod
    def atualizar(produto : Produto):
        if produto.validar():
            produtos = ProdutoDAO.selecionar()
            for p in produtos:
                if produto.id == p.id:
                    p.nome = produto.nome                    
                    p.valor = produto.valor
                    p.quantidade_estoque = produto.quantidade_estoque
                    p.categoria = produto.categoria
                    break
            produtos = ProdutoDAO.parseJSON(produtos)
            return ProdutoDAO.escrever(produtos)
        return False

    @staticmethod
    def atualizar_estoque(produto_id : int, quantidade : int, tipo_atualizacao : int):        
        produtos = ProdutoDAO.selecionar()
        for p in produtos:
            if produto_id == p.id:     
                if tipo_atualizacao == ProdutoDAO.ATUALIZA_COMPRA:           
                    p.quantidade_estoque += quantidade
                else:
                    p.quantidade_estoque -= quantidade
                break
        produtos = ProdutoDAO.parseJSON(produtos)        
        return ProdutoDAO.escrever(produtos)        

    @staticmethod
    def deletar(produto_id : int):
        produtos = ProdutoDAO.selecionar()
        if len(produtos) > 0:            
            for indice, produto in enumerate(produtos):
                if produto.id == produto_id:
                    produtos.pop(indice)
                    break
            produtos = ProdutoDAO.parseJSON(produtos)
            return ProdutoDAO.escrever(produtos)
        return False

    @staticmethod
    def existe(nome : str):    
        for produto in ProdutoDAO.selecionar():            
            if produto.nome == nome:
                return True        
        return False

    @staticmethod
    def parseJSON(produtos: list):
        produtos_dct = []
        for produto in produtos:
            dct = {}
            for k, v in produto.__dict__.items():
                chave = k.replace("_Produto__", "")
                valor = v if chave != "categoria" else v.id
                dct[chave] = valor
            produtos_dct.append(dct)
        return json.dumps(produtos_dct)

    @staticmethod
    def escrever(produtos : list):
        try:
            arquivo = open(ProdutoDAO.DEFAULT_FILE, "w", ProdutoDAO.BUFFER_SIZE)
            arquivo.write(produtos)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(ProdutoDAO.DEFAULT_FILE, "r", ProdutoDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            produtos = []                        
            for c in json.loads(conteudo):                
                produto = Produto()
                produto.id = c["id"]
                produto.nome = c["nome"]
                produto.valor = c["valor"]
                produto.quantidade_estoque = c["quantidade_estoque"]                
                id_categoria = c["categoria"]
                produto.categoria = CategoriaDAO.selecionarPorID(id_categoria)
                produtos.append(produto)            
            return produtos
        except Exception as ex:
            print(ex)
        return []