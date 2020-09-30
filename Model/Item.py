#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

from Produto import Produto

"""
Classe Item: Modelo para objetos do tipo Item, os quais servem tanto para a compra quanto para a venda de produtos.
Cada item contém um id (int), um produto (Produto), a sua quantidade (int), e o valor (float) de compra ou venda.
"""
class Item:
    def __init__(self, id_item : int = None, produto : Produto = None, quantidade : int = None, valor : float = None):
        self.__id = id_item
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = valor
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_item : int):
        if id_item > 0:
            self.__id = id_item
    
    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto : Produto):
        if produto != None:
            self.__produto = produto
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade : int):
        if quantidade > 0:
            self.__quantidade = quantidade        
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor : float):
        if valor > 0:
            self.__valor = valor
    
    def validar(self):
        return self.__id != None and self.__produto != None and self.__quantidade != None and self.__valor != None