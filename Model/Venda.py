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
sys.path.insert(0, "controller")
from Cliente import Cliente
from Funcionario import Funcionario
from datetime import datetime

"""
Classe Venda: Modelo para objetos do tipo Venda.
Cada venda contém um id (int), uma data em que a venda foi realizada (datetime), um funcionário (Funcionario) que realizou a venda, um cliente (Cliente) que fez a compra e uma lista de itens de venda (cada uma contendo um produto (Produto) e a sua quantidade (int)).
"""
class Venda:    
    def __init__(self, id_venda : int = None, data : datetime = None, funcionario : Funcionario = None, cliente : Cliente = None, itens : list = None):
        self.__id = id_venda        
        self.__data = data  
        self.__funcionario = funcionario
        self.__cliente = cliente              
        self.__itens = itens if itens != None and len(itens) > 0 else []
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_venda : int):
        if id_venda > 0:
            self.__id = id_venda

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data : datetime):
        self.__data = data       
        
    @property
    def funcionario(self):
        return self.__funcionario
    
    @funcionario.setter
    def funcionario(self, funcionario : Funcionario):
        if funcionario != None:
            self.__funcionario = funcionario
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente : Cliente):
        if cliente != None:
            self.__cliente = cliente
    
    @property
    def itens(self):
        return self.__itens
    
    @itens.setter
    def itens(self, itens : list):
        if len(itens) > 0:
            self.__itens = itens
        
    def validar(self):
        return self.__id != None and self.__data != None and self.__funcionario != None and self.__cliente != None and self.__itens != None