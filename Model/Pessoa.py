#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = "vinciusmadureira@outlook.com"
__status__ = "Testing"

"""
Classe Pessoa: Modelo para objetos do tipo Pessoa.
Cada pessoa contém um id (int) e um nome (str).
"""
class Pessoa:
    
    def __init__(self, pessoa_id : int = None, nome : str = None):
        self.__id = pessoa_id
        self.__nome = nome
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_pessoa : int):
        if id_pessoa >= 0:
            self.__id = id_pessoa

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome : str):
        if 2 <= len(nome) <= 60:
            self.__nome = nome