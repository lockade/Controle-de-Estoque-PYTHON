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
from Categoria import Categoria
import pathlib
import json

"""
Classe de acesso aos dados das categorias para selecionar, inserir, atualizar e deletar Categorias.
"""
class CategoriaDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/categorias.json"

    @staticmethod
    def selecionar():        
        return CategoriaDAO.ler()        
    
    @staticmethod
    def selecionarPorID(categoria_id : int):
        for categoria in CategoriaDAO.selecionar():
            if categoria.id == categoria_id:
                return categoria
        return None
    
    @staticmethod
    def inserir(categoria : Categoria):        
        categorias = CategoriaDAO.selecionar()
        categoria.id = 1 if len(categorias) == 0 else max(c.id for c in categorias) + 1
        if categoria.validar():
            categorias.append(categoria)                
            categorias = CategoriaDAO.parseJSON(categorias)
            return CategoriaDAO.escrever(categorias)
        return False

    @staticmethod
    def atualizar(categoria : Categoria):
        if categoria.validar():
            categorias = CategoriaDAO.selecionar()
            for c in categorias:
                if categoria.id == c.id:
                    c.nome = categoria.nome                    
                    break
            categorias = CategoriaDAO.parseJSON(categorias)
            return CategoriaDAO.escrever(categorias)
        return False

    @staticmethod
    def deletar(categoria_id : int):
        categorias = CategoriaDAO.selecionar()
        if len(categorias) > 0:            
            for indice, categoria in enumerate(categorias):
                if categoria.id == categoria_id:
                    categorias.pop(indice)
                    break
            categorias = CategoriaDAO.parseJSON(categorias)
            return CategoriaDAO.escrever(categorias)
        return False

    @staticmethod
    def existe(nome : str):        
        for categoria in CategoriaDAO.selecionar():            
            if categoria.nome == nome:
                return True        
        return False

    @staticmethod
    def parseJSON(categorias: list):
        categorias_dct = []
        for categoria in categorias:
            dct = {}
            for k, v in categoria.__dict__.items():
                dct[k.replace("_Categoria__", "")] = v
            categorias_dct.append(dct)
        return json.dumps(categorias_dct)

    @staticmethod
    def escrever(categorias : list):
        try:
            arquivo = open(CategoriaDAO.DEFAULT_FILE, "w", CategoriaDAO.BUFFER_SIZE)
            arquivo.write(categorias)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(CategoriaDAO.DEFAULT_FILE, "r", CategoriaDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            categorias = []            
            for c in json.loads(conteudo):                
                categoria = Categoria()
                categoria.id = c["id"]
                categoria.nome = c["nome"]                
                categorias.append(categoria)
            return categorias
        except:
            pass
        return []