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
from Cidade import Cidade
from Pessoa import Pessoa

"""
Classe Cliente: Modelo para objetos do tipo Cliente.
Cada cliente contém um id (int), um nome (str), um CPF (str) e um endereço (logradouro (str), número (int), CEP (str) e cidade(Cidade)).
"""
class Cliente(Pessoa):

    def __init__(self, client_id : int = None, nome : str = None, CPF : str = None, logradouro : str = None, numero : int = None, CEP : str = None, cidade : Cidade = None):          
        super().__init__(client_id, nome)        
        self.__CPF = CPF
        self.__logradouro = logradouro
        self.__numero = numero
        self.__CEP = CEP
        self.__cidade = cidade

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
    def CPF(self):
        return self.__CPF

    @CPF.setter
    def CPF(self, CPF : str):
        if len(CPF) == 11:
            self.__CPF = CPF

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro : str):
        if 2 <= len(logradouro) <= 60:
            self.__logradouro = logradouro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if 0 <= numero <= 999999:
            self.__numero = numero

    @property
    def CEP(self):
        return self.__CEP

    @CEP.setter
    def CEP(self, CEP: str):
        if len(CEP) == 8:
            self.__CEP = CEP
    
    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade : Cidade):
        if cidade != None:
            self.__cidade = cidade

    def validar(self):        
        return super().id != None and self.__nome != None and self.__CPF != None and self.__logradouro != None and self.__numero != None and self.__CEP != None and self.__cidade != None