#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

from Pessoa import Pessoa

"""
Classe Fornecedor: Modelo para objetos do tipo Fornecedor.
Cada fornecedor contém um id (int), um nome (str) e um CNPJ (str).
"""
class Fornecedor(Pessoa):

    def __init__(self, fornecedor_id : int = None, nome : str = None, CNPJ : str = None):
        super().__init__(fornecedor_id, nome)        
        self.__CNPJ = CNPJ

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome : str):
        if 4 <= len(nome) <= 60:
            self.__nome = nome
        
    @property
    def CNPJ(self):
        return self.__CNPJ

    @CNPJ.setter
    def CNPJ(self, CNPJ : str):
        if len(CNPJ) == 14:
            self.__CNPJ = CNPJ

    def validar(self):
        return super().id != None and self.__nome != None and self.__CNPJ != None