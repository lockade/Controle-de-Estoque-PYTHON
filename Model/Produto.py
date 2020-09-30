#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import re
from Categoria import Categoria

"""
Classe Produto: Modelo para objetos do tipo Produto.
Cada produto contém um id (int), um nome (str), uma categoria (Categoria) a qual pertence, um valor (float) de venda e a quantidade (int) de unidades que possui em estoque.
"""
class Produto:

    def __init__(self, id_produto : int = None, nome : str = None, categoria : Categoria = None, valor : float = None, quantidade_estoque : int = None):
        self.__id = id_produto
        self.__nome = nome
        self.__quantidade_estoque = quantidade_estoque
        self.__categoria = categoria
        self.__valor = valor
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_produto : int):
        if id_produto > 0:
            self.__id = id_produto
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome : str):
        self.__nome = None
        try:
            nome = str(nome).strip()
            if (re.search(r"^[\w]{2,}(\s[\d\w\-,;\+]+)*$", nome, re.UNICODE) and len(nome) <= 60):
                self.__nome = nome
        except:
            pass
  
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria : Categoria):
        if categoria != None:
            self.__categoria = categoria

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor : float):
        if valor >= 0:
            self.__valor = valor   
    
    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque
    
    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque : int):
        if quantidade_estoque >= 0:
            self.__quantidade_estoque = quantidade_estoque   

    def validar(self):
        return self.__id != None and self.__nome != None and self.__categoria != None and self.__valor != None

    """"
    @param quantidade: quantidade de produto a ser atualizada, o valor deve ser positivo
    @param tipo_atualizacao: uma constante que refere se o estoque será atualizado para compra (incremento) ou venda (decremento)
    @return retorna o estado das operações, se o estoque for alterado True, do contrário, False
    """
    def atualizar_estoque(self, quantidade : int, tipo_atualizacao : int):
        if tipo_atualizacao == Produto.ATUALIZACAO_COMPRA:
            self.__quantidade_estoque += quantidade
            return True        
        if tipo_atualizacao == Produto.ATUALIZACAO_VENDA:
            if quantidade <= self.__quantidade_estoque:
                self.__quantidade_estoque -= quantidade
                return True            
        return False

  