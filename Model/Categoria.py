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

"""
Classe Categoria: Modelo para objetos do tipo Categoria.
Cada categoria contém um id (int) e um nome (str).
"""
class Categoria:
    
    def __init__(self, categoria_id : int = None, nome : str = None):
        self.__id = categoria_id
        self.__nome = nome
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, categoria_id : int):
        if categoria_id > 0:
            self.__id = categoria_id
        
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

    def validar(self):
        return self.__id != None and self.__nome != None