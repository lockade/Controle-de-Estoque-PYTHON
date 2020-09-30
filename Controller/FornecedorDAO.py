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
from Fornecedor import Fornecedor
import pathlib
import json

"""
Classe de acesso aos dados dos fornecedores para selecionar, inserir, atualizar e deletar fornecedores.
"""
class FornecedorDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/fornecedores.json"

    @staticmethod
    def selecionar():        
        return FornecedorDAO.ler()        

    @staticmethod
    def selecionarPorID(fornecedor_id : int):
        for fornecedor in FornecedorDAO.selecionar():
            if fornecedor.id == fornecedor_id:
                return fornecedor
        return None    

    @staticmethod
    def inserir(fornecedor : Fornecedor):        
        fornecedores = FornecedorDAO.selecionar()
        fornecedor.id = 1 if len(fornecedores) == 0 else max(c.id for c in fornecedores) + 1        
        if fornecedor.validar():
            fornecedores.append(fornecedor)                
            fornecedores = FornecedorDAO.parseJSON(fornecedores)
            return FornecedorDAO.escrever(fornecedores)
        return False

    @staticmethod
    def atualizar(fornecedor : Fornecedor):
        if fornecedor.validar():
            fornecedores = FornecedorDAO.selecionar()
            for f in fornecedores:
                if fornecedor.id == f.id:
                    f.nome = fornecedor.nome
                    f.CNPJ = fornecedor.CNPJ                    
                    break
            fornecedores = FornecedorDAO.parseJSON(fornecedores)
            return FornecedorDAO.escrever(fornecedores)
        return False

    @staticmethod
    def deletar(fornecedor_id : int):
        fornecedores = FornecedorDAO.selecionar()
        if len(fornecedores) > 0:            
            for indice, fornecedor in enumerate(fornecedores):
                if fornecedor.id == fornecedor_id:
                    fornecedores.pop(indice)
                    break
            fornecedores = FornecedorDAO.parseJSON(fornecedores)
            return FornecedorDAO.escrever(fornecedores)
        return False

    @staticmethod
    def existe(CNPJ : str):    
        for fornecedor in FornecedorDAO.selecionar():            
            if fornecedor.CNPJ == CNPJ:
                return True        
        return False

    @staticmethod
    def parseJSON(fornecedores: list):
        fornecedores_dct = []
        for fornecedor in fornecedores:
            dct = {}
            for k, v in fornecedor.__dict__.items():
                chave = k.replace("_Fornecedor__", "").replace("_Pessoa__", "")
                dct[chave] = v
            fornecedores_dct.append(dct)
        return json.dumps(fornecedores_dct)

    @staticmethod
    def escrever(fornecedores : list):
        try:
            arquivo = open(FornecedorDAO.DEFAULT_FILE, "w", FornecedorDAO.BUFFER_SIZE)
            arquivo.write(fornecedores)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(FornecedorDAO.DEFAULT_FILE, "r", FornecedorDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            fornecedores = []                        
            for c in json.loads(conteudo):                
                fornecedor = Fornecedor()
                fornecedor.id = c["id"]
                fornecedor.nome = c["nome"]
                fornecedor.CNPJ = c["CNPJ"]                
                fornecedores.append(fornecedor)            
            return fornecedores
        except Exception as ex:
            print(ex)
        return []