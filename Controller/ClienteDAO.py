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
from Cliente import Cliente
from CidadeDAO import CidadeDAO
import pathlib
import json

"""
Classe de acesso aos dados dos clientes para selecionar, inserir, atualizar e deletar clientes.
"""
class ClienteDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/clientes.json"

    @staticmethod
    def selecionar():        
        return ClienteDAO.ler()        

    @staticmethod
    def selecionarPorID(cliente_id : int):
        for cliente in ClienteDAO.selecionar():
            if cliente.id == cliente_id:
                return cliente
        return None  

    @staticmethod
    def inserir(cliente : Cliente):        
        clientes = ClienteDAO.selecionar()
        cliente.id = 1 if len(clientes) == 0 else max(c.id for c in clientes) + 1
        if cliente.validar():
            clientes.append(cliente)                
            clientes = ClienteDAO.parseJSON(clientes)
            return ClienteDAO.escrever(clientes)
        return False

    @staticmethod
    def atualizar(cliente : Cliente):
        if cliente.validar():
            clientes = ClienteDAO.selecionar()
            for c in clientes:
                if cliente.id == c.id:
                    c.nome = cliente.nome
                    c.CPF = cliente.CPF
                    c.logradouro = cliente.logradouro
                    c.numero = cliente.numero
                    c.CEP = cliente.CEP
                    c.cidade = cliente.cidade
                    break
            clientes = ClienteDAO.parseJSON(clientes)
            return ClienteDAO.escrever(clientes)
        return False

    @staticmethod
    def deletar(cliente_id : int):
        clientes = ClienteDAO.selecionar()
        if len(clientes) > 0:            
            for indice, cliente in enumerate(clientes):
                if cliente.id == cliente_id:
                    clientes.pop(indice)
                    break
            clientes = ClienteDAO.parseJSON(clientes)
            return ClienteDAO.escrever(clientes)
        return False

    @staticmethod
    def existe(CPF : str):    
        for cliente in ClienteDAO.selecionar():            
            if cliente.CPF == CPF:
                return True        
        return False

    @staticmethod
    def parseJSON(clientes: list):
        clientes_dct = []
        for cliente in clientes:
            dct = {}
            for k, v in cliente.__dict__.items():
                chave = k.replace("_Cliente__", "").replace("_Pessoa__", "")
                valor = v if chave != "cidade" else v.id
                dct[chave] = valor
            clientes_dct.append(dct)
        return json.dumps(clientes_dct)

    @staticmethod
    def escrever(clientes : list):
        try:
            arquivo = open(ClienteDAO.DEFAULT_FILE, "w", ClienteDAO.BUFFER_SIZE)
            arquivo.write(clientes)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(ClienteDAO.DEFAULT_FILE, "r", ClienteDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            clientes = []                        
            for c in json.loads(conteudo):                
                cliente = Cliente()
                cliente.id = c["id"]
                cliente.nome = c["nome"]
                cliente.CPF = c["CPF"]
                cliente.logradouro = c["logradouro"]
                cliente.numero = c["numero"]
                cliente.CEP = c["CEP"]
                id_cidade = c["cidade"]
                cliente.cidade = CidadeDAO.selecionarPorID(id_cidade)
                clientes.append(cliente)            
            return clientes
        except Exception as ex:
            print(ex)
        return []