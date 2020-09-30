#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jefferson Dias"
__copyright__ = "Copyright 2020, Jefferson Dias"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
sys.path.insert(0, "Controller")
from Categoria import Categoria
from CategoriaDAO import CategoriaDAO

"""
"""
class CategoriaView:
    @staticmethod
    def menu():
        while(1):
            print("--Menu Categoria--")
            print("1 - Inserir Categoria")
            print("2 - Alterar Categoria")
            print("3 - Visualizar Categorias")
            print("0 - Voltar")            
            escolha = input("Opção: ")            
            if(escolha == "1"):
                if(CategoriaView.inserirCategoria()):
                    print("Categoria Inserida")
                    continue
                print("Categoria NÃO Inserida")
            elif(escolha == "2"):
                CategoriaView.alterarCategoria()
            elif(escolha == "3"):
                CategoriaView.visualizarCategoria()
            elif(escolha == "0"):
                return
            
    @staticmethod
    def excluirCategoria():
        CategoriaView.visualizarCategoria()
        try:
            id_categoria = int(input("ID da Categoria para Exclusão: "))
            #pesquisa por ID, retorna o objeto produto completo
            categoria = CategoriaDAO.selecionarPorID(id_categoria)
            if(categoria != None):
                if(CategoriaView.opcaoSimNao(f"Deseja Excluir a Categoria {categoria.nome}? Sim para Exclução e Não para Cancelar \nResposta: ")):
                    CategoriaDAO.deletar(id_categoria)
                    print(f"Categoria {categoria.nome} foi Deletado!")
                else:
                    print("Nada foi Excluido")
                                
        except:
            print("Nada Salvo, Erro na Exclusão")
            return False
        
        
    @staticmethod
    def inserirCategoria():
        nome = input("Nome da Categoria: ")        
        categoria = Categoria(None, nome)
        #inserir nos arquivos        

        #se foi inserido deve retornar true
        if(CategoriaDAO.inserir(categoria)): 
            return True
        return False
    
    @staticmethod
    def visualizarCategoria():        
        #deve receber uma lista de categorias vinda da pesquisa dos arquivos
        lista_categorias = CategoriaDAO.selecionar()
        print("--Categorias--")
        for item in lista_categorias:
            print(f"{item.id} - {item.nome}")
        print("--------------")
        

    @staticmethod
    def alterarCategoria():
        CategoriaView.visualizarCategoria()
        try:
            id_categoria = int(input("ID da Categoria para Edição: "))            
            categoria = CategoriaDAO.selecionarPorID(id_categoria)#pesquisa por  ID ? e ele me retorna um objeto Categoria Completo
            if(categoria != None):
                while(1):#while de edição
                    print(f"\n\nCategoria: {categoria.nome}")
                    print("1 - Editar Nome")
                    print("2 - Finalizar")                    
                    escolha = input("Opção: ")
                    if(escolha == "1"):
                        novo_nome = input("Novo nome: ")
                        categoria.nome = novo_nome
                    elif(escolha == "2"):
                        CategoriaDAO.atualizar(categoria)#mando a categoria já editada
                        return True            
        except:
            return False    
    
    @staticmethod
    def opcaoSimNao(texto : str):
        while(1):
            try:
                resposta = input(texto).lower()
                if(resposta == "sim"):
                    return True
                elif(resposta == "nao" or resposta == "não"):
                    return False
            except:
                return False