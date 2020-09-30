#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo - C"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
sys.path.insert(0, "Controller")
sys.path.insert(0, "View")
from Produto import Produto
from ProdutoDAO import ProdutoDAO
from CategoriaDAO import CategoriaDAO
from ProdutoView import ProdutoView
from CategoriaView import CategoriaView
from ClienteView import ClienteView
from FuncionarioView import FuncionarioView
from FornecedorView import FornecedorView
from CompraView import CompraView
from VendaView import VendaView
from CidadeView import CidadeView
from RelatorioView import RelatorioView
from CaixaView import CaixaView

if __name__ == "__main__":
    while(1):
        print("------ Menu ------")
        print("### Produto ###")
        print("1 - Inserir | 2 - Alterar | 3 - Excluir | 4 - Visualizar")
        
        print("### Categoria ###")
        print("5 - Inserir | 6 - Alterar | 7 - Excluir | 8 - Visualizar")
        
        print("### Cliente ###")
        print("9 - Inserir | 10 - Alterar | 11 - Excluir | 12 - Visualizar")
        
        print("### Funcionário ###")
        print("13 - Inserir | 14 - Alterar | 15 - Excluir | 16 - Visualizar")
        
        print("### Fornecedor ###")
        print("17 - Inserir | 18 - Alterar | 19 - Excluir | 20 - Visualizar")
        
        print("### Compra ###")
        print("21 - Comprar | 22 - Visualizar")
        
        print("### Venda ###")
        print("23 - Vender | 24 - Visualizar")
        
        print("### Relatorios ###")
        print("25 - Produtos mais vendidos | 26 - Clientes que mais Compram")
        
        print("### Caixa ###")
        print("27 - Saldo Diario")
        
        print("### Cidades ###")
        print("28 - Inserir | 29 - Aterar | 30 - Excluir | 31 - Visualizar")
        escolha = input("Opção: ")
        
        #Inicio Produto
        if(escolha == "1"):
            ProdutoView.inserirProduto()
        elif(escolha == "2"):
            ProdutoView.alterarProduto()
        elif(escolha == "3"):
            ProdutoView.excluirProduto()
        elif(escolha == "4"):
            ProdutoView.visualizarProduto()
        #Fim Produto
            
        #inicio Categoria
        elif(escolha == "5"):
            CategoriaView.inserirCategoria()
        elif(escolha == "6"):
            CategoriaView.alterarCategoria()
        elif(escolha == "7"):
            CategoriaView.excluirCategoria()
        elif(escolha == "8"):
            CategoriaView.visualizarCategoria()
        #Fim Categoria
        
        #Inicio Cliente
        elif(escolha == "9"):
            ClienteView.adicionar()
        elif(escolha == "10"):
            ClienteView.atualizar()
        elif(escolha == "11"):
            ClienteView.remover()
        elif(escolha == "12"):
            ClienteView.listar()
        #Fim Cliente 
        
        #Inicio Funcionario
        elif(escolha == "13"):
            FuncionarioView.adicionar()
        elif(escolha == "14"):
            FuncionarioView.atualizar()
        elif(escolha == "15"):
            FuncionarioView.remover()
        elif(escolha == "16"):
            FuncionarioView.listar()
        #Fim Funcionario
        
        #Inicio Fornecedor
        elif(escolha == "17"):
            FornecedorView.adicionar()
        elif(escolha == "18"):
            FornecedorView.atualizar()
        elif(escolha == "19"):
            FornecedorView.remover()
        elif(escolha == "20"):
            FornecedorView.listar()
        #Fim Fornecedor
        
        #Inicio Compra
        elif(escolha == "21"):
            CompraView.inserirCompra()
        elif(escolha == "22"):
            CompraView.visualizarCompras()
        #Fim Compra
        
        #Inicio Venda
        elif(escolha == "23"):
            VendaView.inserirVenda()
        elif(escolha == "24"):
            VendaView.visualizarVendas()
        #Fim Venda
        
        
        #relatorio
        elif(escolha == "25"):
            RelatorioView.listar_produtos_mais_vendidos()
        elif(escolha == "26"):
            RelatorioView.listar_clientes_mais_compraram()
            
        #caixa
        elif(escolha == "27"):
            CaixaView.saldo_diario()
        
        #cidade
        elif(escolha == "28"):
            CidadeView.adicionar()
        elif(escolha == "29"):
            CidadeView.atualizar()
        elif(escolha == "30"):
            CidadeView.remover()
        elif(escolha == "31"):
            CidadeView.listar()
            
            