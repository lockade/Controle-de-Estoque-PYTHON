#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

from Fornecedor import Fornecedor
from datetime import datetime

"""
Classe Compra: Modelo para objetos do tipo Compra.
Cada compra contém um id (int), uma data (datetime), um fornecedor (Fornecedor) da mercadoria e uma lista de Itens (cada um com o seu id (int), seu produto (Produto) e sua respectiva quantidade (int) e seu valor (float) de compra).
"""
class Compra:

    def __init__(self, id_compra : int = None, data : datetime = None, fornecedor : Fornecedor = None, itens : list = None):
        self.__id = id_compra        
        self.__data = data  
        self.__fornecedor = fornecedor
        self.__itens = itens if itens != None and len(itens) > 0 else []
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_compra : int):
        if id_compra > 0:
            self.__id = id_compra
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data : datetime):
        self.__data = data

    @property
    def fornecedor(self):
        return self.__fornecedor
    
    @fornecedor.setter
    def fornecedor(self, fornecedor : Fornecedor):
        if fornecedor != None:
            self.__fornecedor = fornecedor
    
    @property
    def itens(self):
        return self.__itens
    
    @itens.setter
    def itens(self, itens : list):
        if len(itens) > 0:
            self.__itens = itens
        
    def validar(self):
        return self.__id != None and self.__data != None and self.__fornecedor != None and self.__itens != None
