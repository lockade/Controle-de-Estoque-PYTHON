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
from Pessoa import Pessoa

"""
Classe Funcionario: Modelo para objetos do tipo Funcionario.
Cada Funcionário contém um id (int), um nome (str), um registro (str) e um salário (float).
"""
class Funcionario(Pessoa):

    def __init__(self, funcionario_id : int = None, nome : str = None, registro : str = None, salario : float = None):           
        super().__init__(funcionario_id, nome)
        self.__registro = None
        self.__salario = None

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
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro : str):
        if 2 <= len(registro) <= 15:
            self.__registro = registro

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario : float):
        if salario >= 0.0:
            self.__salario = salario

    def validar(self):        
        return super().id != None and self.__nome != None and self.__registro != None and self.__salario != None