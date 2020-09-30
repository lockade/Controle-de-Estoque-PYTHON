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
from Cidade import Cidade
import pathlib
import json

"""
Classe de acesso aos dados das cidades para selecionar, inserir, atualizar e deletar cidades.
"""
class CidadeDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/cidades.json"

    @staticmethod
    def selecionar():        
        return CidadeDAO.ler()        
    
    @staticmethod
    def selecionarPorID(cidade_id : int):
        for cidade in CidadeDAO.selecionar():
            if cidade.id == cidade_id:
                return cidade
        return None
    
    @staticmethod
    def inserir(cidade : Cidade):        
        cidades = CidadeDAO.selecionar()
        cidade.id = 1 if len(cidades) == 0 else max(c.id for c in cidades) + 1
        if cidade.validar():
            cidades.append(cidade)                
            cidades = CidadeDAO.parseJSON(cidades)
            return CidadeDAO.escrever(cidades)
        return False

    @staticmethod
    def atualizar(cidade : Cidade):
        if cidade.validar():
            cidades = CidadeDAO.selecionar()
            for c in cidades:
                if cidade.id == c.id:
                    c.nome = cidade.nome
                    c.UF = cidade.UF
                    break
            cidades = CidadeDAO.parseJSON(cidades)
            return CidadeDAO.escrever(cidades)
        return False

    @staticmethod
    def deletar(id_cidade : int):
        cidades = CidadeDAO.selecionar()
        if len(cidades) > 0:            
            for indice, cidade in enumerate(cidades):
                if cidade.id == id_cidade:
                    cidades.pop(indice)
                    break
            cidades = CidadeDAO.parseJSON(cidades)
            return CidadeDAO.escrever(cidades)
        return False

    @staticmethod
    def existe(nome : str, UF : str):        
        for cidade in CidadeDAO.selecionar():            
            if cidade.nome == nome and cidade.UF == UF:
                return True        
        return False

    @staticmethod
    def parseJSON(cidades: list):
        cidades_dct = []
        for cidade in cidades:
            dct = {}
            for k, v in cidade.__dict__.items():
                dct[k.replace("_Cidade__", "")] = v
            cidades_dct.append(dct)
        return json.dumps(cidades_dct)

    @staticmethod
    def escrever(cidades : list):
        try:
            arquivo = open(CidadeDAO.DEFAULT_FILE, "w", CidadeDAO.BUFFER_SIZE)
            arquivo.write(cidades)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(CidadeDAO.DEFAULT_FILE, "r", CidadeDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            cidades = []            
            for c in json.loads(conteudo):                
                cidade = Cidade()
                cidade.id = c["id"]
                cidade.nome = c["nome"]
                cidade.UF = c["UF"]
                cidades.append(cidade)
            return cidades
        except:
            pass
        return []