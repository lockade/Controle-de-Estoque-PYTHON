#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

"""
Classe Cidade: Modelo para objetos do tipo Cidade.
Cada cidade contém um id (int), um nome (str) e uma UF (str).
"""
class Cidade:

    def __init__(self, cidade_id : int = None, nome : str = None, UF : str = None):
        self.__id = cidade_id
        self.__nome = nome
        self.__UF = UF

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, cidade_id):
        if cidade_id > 0:
            self.__id = cidade_id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome : str):
       if 2 <= len(nome) <= 60:
           self.__nome = nome       
    
    @property
    def UF(self):
        return self.__UF

    @UF.setter
    def UF(self, UF : str):
        if len(UF) == 2:
            self.__UF = UF

    def validar(self):
        return self.__id != None and self.__nome != None and self.__UF != None 