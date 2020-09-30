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
from Funcionario import Funcionario
import pathlib
import json

"""
Classe de acesso aos dados dos funcionários para selecionar, inserir, atualizar e deletar funcionários.
"""
class FuncionarioDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/funcionarios.json"

    @staticmethod
    def selecionar():        
        return FuncionarioDAO.ler()        

    @staticmethod
    def selecionarPorID(funcionario_id : int):
        for funcionario in FuncionarioDAO.selecionar():
            if funcionario.id == funcionario_id:
                return funcionario
        return None  

    @staticmethod
    def inserir(funcionario : Funcionario):        
        funcionarios = FuncionarioDAO.selecionar()
        funcionario.id = 1 if len(funcionarios) == 0 else max(c.id for c in funcionarios) + 1
        if funcionario.validar():
            funcionarios.append(funcionario)                
            funcionarios = FuncionarioDAO.parseJSON(funcionarios)
            return FuncionarioDAO.escrever(funcionarios)
        return False

    @staticmethod
    def atualizar(funcionario : Funcionario):
        if funcionario.validar():
            funcionarios = FuncionarioDAO.selecionar()
            for f in funcionarios:
                if funcionario.id == f.id:
                    f.nome = funcionario.nome
                    f.registro = funcionario.registro
                    f.salario = funcionario.salario                    
                    break
            funcionarios = FuncionarioDAO.parseJSON(funcionarios)
            return FuncionarioDAO.escrever(funcionarios)
        return False

    @staticmethod
    def deletar(funcionario_id : int):
        funcionarios = FuncionarioDAO.selecionar()
        if len(funcionarios) > 0:            
            for indice, funcionario in enumerate(funcionarios):
                if funcionario.id == funcionario_id:
                    funcionarios.pop(indice)
                    break
            funcionarios = FuncionarioDAO.parseJSON(funcionarios)
            return FuncionarioDAO.escrever(funcionarios)
        return False

    @staticmethod
    def existe(registro : str):    
        for funcionario in FuncionarioDAO.selecionar():            
            if funcionario.registro == registro:
                return True        
        return False

    @staticmethod
    def parseJSON(funcionarios: list):
        funcionarios_dct = []
        for funcionario in funcionarios:
            dct = {}
            for k, v in funcionario.__dict__.items():
                chave = k.replace("_Funcionario__", "").replace("_Pessoa__", "")
                dct[chave] = v
            funcionarios_dct.append(dct)
        return json.dumps(funcionarios_dct)

    @staticmethod
    def escrever(funcionarios : list):
        try:
            arquivo = open(FuncionarioDAO.DEFAULT_FILE, "w", FuncionarioDAO.BUFFER_SIZE)
            arquivo.write(funcionarios)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(FuncionarioDAO.DEFAULT_FILE, "r", FuncionarioDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            funcionarios = []                        
            for c in json.loads(conteudo):                
                funcionario = Funcionario()
                funcionario.id = c["id"]
                funcionario.nome = c["nome"]
                funcionario.registro = c["registro"]
                funcionario.salario = c["salario"]                
                funcionarios.append(funcionario)            
            return funcionarios
        except Exception as ex:
            print(ex)
        return []