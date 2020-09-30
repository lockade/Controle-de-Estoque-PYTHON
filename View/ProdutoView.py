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
from CategoriaView import CategoriaView
from CategoriaDAO import CategoriaDAO
from Produto import Produto
from ProdutoDAO import ProdutoDAO

"""
"""
class ProdutoView:
    
    def menu():
        while(1):
            print("--Menu Produto--")
            print("1 - Inserir Produto")
            print("2 - Alterar Produto")
            print("3 - Excluir Produto")
            print("4 - Visualizar Produto")
            print("0 - Voltar")   
        
            escolha = input("Opção: ")            
            if(escolha == "1"):
                if(ProdutoView.inserirProduto()):
                    print("Produto Inserido")
                    continue
                print("Produto NÃO Inserido")
            elif(escolha == "2"):
                ProdutoView.alterarProduto()
            elif(escolha == "3"):
                ProdutoView.excluirProduto()
            elif(escolha == "4"):
                ProdutoView.visualizarProduto()
            elif(escolha == "0"):
                return
    

    @staticmethod 
    def excluirProduto():
        ProdutoView.visualizarProduto()
        try:
            id_produto = int(input("ID do produto para Exclusão: "))
            #pesquisa por ID, retorna o objeto produto completo
            produto = ProdutoDAO.selecionarPorID(id_produto)
            if(produto != None):
                if(ProdutoView.opcaoSimNao(f"Deseja Excluir o Produto {produto.nome}? Sim para Exclução e Não para Cancelar \nResposta: ")):
                    ProdutoDAO.deletar(produto.id)
                    print(f"Produto {produto.nome} foi Deletado!")
                else:
                    print("Nada foi Excluido")
                                
        except:
            print("Nada Salvo, Erro na Exclusão")
            return False


    @staticmethod
    def visualizarProduto():
        lista_produto = ProdutoDAO.selecionar() #me retorna uma lista com todos produtos : Produto
        
        print("--Produtos--")
        for item in lista_produto:
            if(item.categoria is None):
                print(f"ID: {item.id} | Nome: {item.nome} | Quantidade em Estoque: {item.quantidade_estoque} | Preço : {item.valor} | Categoria: Sem Categoria")
            else:
                print(f"ID: {item.id} | Nome: {item.nome} | Quantidade em Estoque: {item.quantidade_estoque} | Preço : {item.valor} | Categoria: {item.categoria.nome}")
        print("------------")

    @staticmethod
    def alterarProduto():
        ProdutoView.visualizarProduto()
        try:
            id_produto = int(input("ID do produto para Edição: "))
            #pesquisa por ID, retorna o objeto produto completo
            produto = ProdutoDAO.selecionarPorID(id_produto)
            if(produto != None):
                while(1):
                    print(f"Produto: {produto.nome} | Quantidade: {produto.quantidade_estoque} | Valor: {produto.valor} | Categoria: {produto.categoria.nome}")
                    print("1 - Editar Nome")
                    print("2 - Editar Quantidade")
                    print("3 - Editar Valor")
                    print("4 - Editar Categoria")
                    print("5 - Finalizar")                    
                    escolha = input("Opção: ")                    
                    if(escolha == "1"):
                        novo_nome = input("Novo nome: ")
                        produto.nome = novo_nome
                    elif(escolha == "2"):
                        nova_quantidade = int(input("Nova quantidade: "))
                        produto.quantidade_estoque = nova_quantidade
                    elif(escolha == "3"):
                        novo_valor = float(input("Novo valor: "))
                        produto.valor = novo_valor
                    elif(escolha == "4"):
                        CategoriaView.visualizarCategoria()
                        id_categoria = int(input("ID da Categoria: "))
                        #pesquisa por id e retornar o objeto
                        categoria = CategoriaDAO.selecionarPorID(id_categoria)
                        produto.categoria = categoria
                    elif(escolha == "5"):
                        ProdutoDAO.atualizar(produto)
                        return True            
        except:
            print("Nada Salvo, Erro na alteração")
            return False

    @staticmethod
    def inserirProduto():
        try:
            nome = input("Nome do Produto: ")
            valor = float(input("Valor do Produto: "))
            quantidade_estoque = int(input("Quantidade em Estoque: "))
            
            #Seleção da Categoria
            while(1):#evitar seleção de categoria inválida, e efetuar um loop para que selecione uma categoria verdadeira
              print("Selecione a Categoria")
              CategoriaView.visualizarCategoria()
              escolha = int(input("ID da Categoria: "))
              categoria = CategoriaDAO.selecionarPorID(escolha)
              if(categoria != None):
                break


            

            #criando objeto para inserção         
            produto = Produto(None, nome, categoria, valor, quantidade_estoque)
            #inserção nos arquivos
            if(ProdutoDAO.inserir(produto)):
                return True
            return False
        except Exception as e:
            print("Erro na Inserção do Produto")
            print(str(e))
            return False

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