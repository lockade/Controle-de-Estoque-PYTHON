# -*- coding: utf-8 -*-
""" ARQUIVO main.py
Created on Wed Sep 30 16:07:02 2020

@author: Jefferson
"""

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
			
			
#Arquivo: Controller/CategoriaDAO.py
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
sys.path.insert(0, "Model")
from Categoria import Categoria
import pathlib
import json

"""
Classe de acesso aos dados das categorias para selecionar, inserir, atualizar e deletar Categorias.
"""
class CategoriaDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/categorias.json"

    @staticmethod
    def selecionar():        
        return CategoriaDAO.ler()        
    
    @staticmethod
    def selecionarPorID(categoria_id : int):
        for categoria in CategoriaDAO.selecionar():
            if categoria.id == categoria_id:
                return categoria
        return None
    
    @staticmethod
    def inserir(categoria : Categoria):        
        categorias = CategoriaDAO.selecionar()
        categoria.id = 1 if len(categorias) == 0 else max(c.id for c in categorias) + 1
        if categoria.validar():
            categorias.append(categoria)                
            categorias = CategoriaDAO.parseJSON(categorias)
            return CategoriaDAO.escrever(categorias)
        return False

    @staticmethod
    def atualizar(categoria : Categoria):
        if categoria.validar():
            categorias = CategoriaDAO.selecionar()
            for c in categorias:
                if categoria.id == c.id:
                    c.nome = categoria.nome                    
                    break
            categorias = CategoriaDAO.parseJSON(categorias)
            return CategoriaDAO.escrever(categorias)
        return False

    @staticmethod
    def deletar(categoria_id : int):
        categorias = CategoriaDAO.selecionar()
        if len(categorias) > 0:            
            for indice, categoria in enumerate(categorias):
                if categoria.id == categoria_id:
                    categorias.pop(indice)
                    break
            categorias = CategoriaDAO.parseJSON(categorias)
            return CategoriaDAO.escrever(categorias)
        return False

    @staticmethod
    def existe(nome : str):        
        for categoria in CategoriaDAO.selecionar():            
            if categoria.nome == nome:
                return True        
        return False

    @staticmethod
    def parseJSON(categorias: list):
        categorias_dct = []
        for categoria in categorias:
            dct = {}
            for k, v in categoria.__dict__.items():
                dct[k.replace("_Categoria__", "")] = v
            categorias_dct.append(dct)
        return json.dumps(categorias_dct)

    @staticmethod
    def escrever(categorias : list):
        try:
            arquivo = open(CategoriaDAO.DEFAULT_FILE, "w", CategoriaDAO.BUFFER_SIZE)
            arquivo.write(categorias)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(CategoriaDAO.DEFAULT_FILE, "r", CategoriaDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            categorias = []            
            for c in json.loads(conteudo):                
                categoria = Categoria()
                categoria.id = c["id"]
                categoria.nome = c["nome"]                
                categorias.append(categoria)
            return categorias
        except:
            pass
        return []
		
#Arquivo: Controller/CidadeDAO.py
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
sys.path.insert(0, "Model")
from Cidade import Cidade
import pathlib
import json

"""
Classe de acesso aos dados das cidades para selecionar, inserir, atualizar e deletar cidades.
"""
class CidadeDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/cidades.json"

    @staticmethod
    def selecionar():        
        return CidadeDAO.ler()        
    
    @staticmethod
    def selecionarPorID(cidade_id : int):
        for cidade in CidadeDAO.selecionar():
            if cidade.id == cidade_id:
                return cidade
        return None
    
    @staticmethod
    def inserir(cidade : Cidade):        
        cidades = CidadeDAO.selecionar()
        cidade.id = 1 if len(cidades) == 0 else max(c.id for c in cidades) + 1
        if cidade.validar():
            cidades.append(cidade)                
            cidades = CidadeDAO.parseJSON(cidades)
            return CidadeDAO.escrever(cidades)
        return False

    @staticmethod
    def atualizar(cidade : Cidade):
        if cidade.validar():
            cidades = CidadeDAO.selecionar()
            for c in cidades:
                if cidade.id == c.id:
                    c.nome = cidade.nome
                    c.UF = cidade.UF
                    break
            cidades = CidadeDAO.parseJSON(cidades)
            return CidadeDAO.escrever(cidades)
        return False

    @staticmethod
    def deletar(id_cidade : int):
        cidades = CidadeDAO.selecionar()
        if len(cidades) > 0:            
            for indice, cidade in enumerate(cidades):
                if cidade.id == id_cidade:
                    cidades.pop(indice)
                    break
            cidades = CidadeDAO.parseJSON(cidades)
            return CidadeDAO.escrever(cidades)
        return False

    @staticmethod
    def existe(nome : str, UF : str):        
        for cidade in CidadeDAO.selecionar():            
            if cidade.nome == nome and cidade.UF == UF:
                return True        
        return False

    @staticmethod
    def parseJSON(cidades: list):
        cidades_dct = []
        for cidade in cidades:
            dct = {}
            for k, v in cidade.__dict__.items():
                dct[k.replace("_Cidade__", "")] = v
            cidades_dct.append(dct)
        return json.dumps(cidades_dct)

    @staticmethod
    def escrever(cidades : list):
        try:
            arquivo = open(CidadeDAO.DEFAULT_FILE, "w", CidadeDAO.BUFFER_SIZE)
            arquivo.write(cidades)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(CidadeDAO.DEFAULT_FILE, "r", CidadeDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            cidades = []            
            for c in json.loads(conteudo):                
                cidade = Cidade()
                cidade.id = c["id"]
                cidade.nome = c["nome"]
                cidade.UF = c["UF"]
                cidades.append(cidade)
            return cidades
        except:
            pass
        return []
		
#Arquivo: Controller/ClienteDAO.py
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
sys.path.insert(0, "Model")
from Cliente import Cliente
from CidadeDAO import CidadeDAO
import pathlib
import json

"""
Classe de acesso aos dados dos clientes para selecionar, inserir, atualizar e deletar clientes.
"""
class ClienteDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/clientes.json"

    @staticmethod
    def selecionar():        
        return ClienteDAO.ler()        

    @staticmethod
    def selecionarPorID(cliente_id : int):
        for cliente in ClienteDAO.selecionar():
            if cliente.id == cliente_id:
                return cliente
        return None  

    @staticmethod
    def inserir(cliente : Cliente):        
        clientes = ClienteDAO.selecionar()
        cliente.id = 1 if len(clientes) == 0 else max(c.id for c in clientes) + 1
        if cliente.validar():
            clientes.append(cliente)                
            clientes = ClienteDAO.parseJSON(clientes)
            return ClienteDAO.escrever(clientes)
        return False

    @staticmethod
    def atualizar(cliente : Cliente):
        if cliente.validar():
            clientes = ClienteDAO.selecionar()
            for c in clientes:
                if cliente.id == c.id:
                    c.nome = cliente.nome
                    c.CPF = cliente.CPF
                    c.logradouro = cliente.logradouro
                    c.numero = cliente.numero
                    c.CEP = cliente.CEP
                    c.cidade = cliente.cidade
                    break
            clientes = ClienteDAO.parseJSON(clientes)
            return ClienteDAO.escrever(clientes)
        return False

    @staticmethod
    def deletar(cliente_id : int):
        clientes = ClienteDAO.selecionar()
        if len(clientes) > 0:            
            for indice, cliente in enumerate(clientes):
                if cliente.id == cliente_id:
                    clientes.pop(indice)
                    break
            clientes = ClienteDAO.parseJSON(clientes)
            return ClienteDAO.escrever(clientes)
        return False

    @staticmethod
    def existe(CPF : str):    
        for cliente in ClienteDAO.selecionar():            
            if cliente.CPF == CPF:
                return True        
        return False

    @staticmethod
    def parseJSON(clientes: list):
        clientes_dct = []
        for cliente in clientes:
            dct = {}
            for k, v in cliente.__dict__.items():
                chave = k.replace("_Cliente__", "").replace("_Pessoa__", "")
                valor = v if chave != "cidade" else v.id
                dct[chave] = valor
            clientes_dct.append(dct)
        return json.dumps(clientes_dct)

    @staticmethod
    def escrever(clientes : list):
        try:
            arquivo = open(ClienteDAO.DEFAULT_FILE, "w", ClienteDAO.BUFFER_SIZE)
            arquivo.write(clientes)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(ClienteDAO.DEFAULT_FILE, "r", ClienteDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            clientes = []                        
            for c in json.loads(conteudo):                
                cliente = Cliente()
                cliente.id = c["id"]
                cliente.nome = c["nome"]
                cliente.CPF = c["CPF"]
                cliente.logradouro = c["logradouro"]
                cliente.numero = c["numero"]
                cliente.CEP = c["CEP"]
                id_cidade = c["cidade"]
                cliente.cidade = CidadeDAO.selecionarPorID(id_cidade)
                clientes.append(cliente)            
            return clientes
        except Exception as ex:
            print(ex)
        return []
		
#Arquivo: Controller/CompraDAO.py
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
sys.path.insert(0, "Model")
from Compra import Compra
from Item import Item
from FornecedorDAO import FornecedorDAO
from ProdutoDAO import ProdutoDAO
from datetime import datetime
import pathlib
import json

"""
Classe de acesso aos dados dos compras para selecionar, inserir, atualizar e deletar compras.
"""
class CompraDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/compras.json"

    @staticmethod
    def selecionar():        
        return CompraDAO.ler()        

    @staticmethod
    def inserir(compra : Compra):        
        compras = CompraDAO.selecionar()
        compra.id = 1 if len(compras) == 0 else max(c.id for c in compras) + 1                
        if compra.validar():            
            compras.append(compra)                
            compras = CompraDAO.parseJSON(compras)
            return CompraDAO.escrever(compras)
        return False    

    @staticmethod
    def parseJSON(compras: list):
        compras_dct = []        
        for compra in compras:            
            itens = []                        
            for item in compra.itens:
                item_dct = {
                    "id" : item.id,
                    "produto_id" : item.produto.id,
                    "quantidade" : item.quantidade,
                    "valor" : item.valor
                }
                itens.append(item_dct)
                compra_dct = {
                    "id" : compra.id,
                    "data" : compra.data.strftime('%Y-%m-%d %H:%M:%S'),
                    "fornecedor_id" : compra.fornecedor.id,
                    "itens" : itens
                }                                                
            compras_dct.append(compra_dct)
        return json.dumps(compras_dct)

    @staticmethod
    def escrever(compras : list):
        try:
            arquivo = open(CompraDAO.DEFAULT_FILE, "w", CompraDAO.BUFFER_SIZE)
            arquivo.write(compras)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(CompraDAO.DEFAULT_FILE, "r", CompraDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            compras = []                        
            for c in json.loads(conteudo):                
                compra = Compra()
                compra.id = c["id"]                
                compra.data = datetime.strptime(c["data"], '%Y-%m-%d %H:%M:%S')                
                fornecedor_id = c["fornecedor_id"]                
                compra.fornecedor = FornecedorDAO.selecionarPorID(fornecedor_id)                
                itens = c["itens"]
                for i in itens:                
                    item = Item()
                    item.id = i["id"]
                    produto_id = i["produto_id"]
                    item.produto = ProdutoDAO.selecionarPorID(produto_id)
                    item.quantidade = i["quantidade"]
                    item.valor = i["valor"] 
                    compra.itens.append(item)
                compras.append(compra)
            return compras
        except:
            pass
        return []
		
#Arquivo: Controller/FornecedorDAO.py
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
sys.path.insert(0, "Model")
from Fornecedor import Fornecedor
import pathlib
import json

"""
Classe de acesso aos dados dos fornecedores para selecionar, inserir, atualizar e deletar fornecedores.
"""
class FornecedorDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/fornecedores.json"

    @staticmethod
    def selecionar():        
        return FornecedorDAO.ler()        

    @staticmethod
    def selecionarPorID(fornecedor_id : int):
        for fornecedor in FornecedorDAO.selecionar():
            if fornecedor.id == fornecedor_id:
                return fornecedor
        return None    

    @staticmethod
    def inserir(fornecedor : Fornecedor):        
        fornecedores = FornecedorDAO.selecionar()
        fornecedor.id = 1 if len(fornecedores) == 0 else max(c.id for c in fornecedores) + 1        
        if fornecedor.validar():
            fornecedores.append(fornecedor)                
            fornecedores = FornecedorDAO.parseJSON(fornecedores)
            return FornecedorDAO.escrever(fornecedores)
        return False

    @staticmethod
    def atualizar(fornecedor : Fornecedor):
        if fornecedor.validar():
            fornecedores = FornecedorDAO.selecionar()
            for f in fornecedores:
                if fornecedor.id == f.id:
                    f.nome = fornecedor.nome
                    f.CNPJ = fornecedor.CNPJ                    
                    break
            fornecedores = FornecedorDAO.parseJSON(fornecedores)
            return FornecedorDAO.escrever(fornecedores)
        return False

    @staticmethod
    def deletar(fornecedor_id : int):
        fornecedores = FornecedorDAO.selecionar()
        if len(fornecedores) > 0:            
            for indice, fornecedor in enumerate(fornecedores):
                if fornecedor.id == fornecedor_id:
                    fornecedores.pop(indice)
                    break
            fornecedores = FornecedorDAO.parseJSON(fornecedores)
            return FornecedorDAO.escrever(fornecedores)
        return False

    @staticmethod
    def existe(CNPJ : str):    
        for fornecedor in FornecedorDAO.selecionar():            
            if fornecedor.CNPJ == CNPJ:
                return True        
        return False

    @staticmethod
    def parseJSON(fornecedores: list):
        fornecedores_dct = []
        for fornecedor in fornecedores:
            dct = {}
            for k, v in fornecedor.__dict__.items():
                chave = k.replace("_Fornecedor__", "").replace("_Pessoa__", "")
                dct[chave] = v
            fornecedores_dct.append(dct)
        return json.dumps(fornecedores_dct)

    @staticmethod
    def escrever(fornecedores : list):
        try:
            arquivo = open(FornecedorDAO.DEFAULT_FILE, "w", FornecedorDAO.BUFFER_SIZE)
            arquivo.write(fornecedores)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(FornecedorDAO.DEFAULT_FILE, "r", FornecedorDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            fornecedores = []                        
            for c in json.loads(conteudo):                
                fornecedor = Fornecedor()
                fornecedor.id = c["id"]
                fornecedor.nome = c["nome"]
                fornecedor.CNPJ = c["CNPJ"]                
                fornecedores.append(fornecedor)            
            return fornecedores
        except Exception as ex:
            print(ex)
        return []
		
#Arquivo: Controller/FuncionarioDAO.py
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
sys.path.insert(0, "Model")
from Funcionario import Funcionario
import pathlib
import json

"""
Classe de acesso aos dados dos funcionários para selecionar, inserir, atualizar e deletar funcionários.
"""
class FuncionarioDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/funcionarios.json"

    @staticmethod
    def selecionar():        
        return FuncionarioDAO.ler()        

    @staticmethod
    def selecionarPorID(funcionario_id : int):
        for funcionario in FuncionarioDAO.selecionar():
            if funcionario.id == funcionario_id:
                return funcionario
        return None  

    @staticmethod
    def inserir(funcionario : Funcionario):        
        funcionarios = FuncionarioDAO.selecionar()
        funcionario.id = 1 if len(funcionarios) == 0 else max(c.id for c in funcionarios) + 1
        if funcionario.validar():
            funcionarios.append(funcionario)                
            funcionarios = FuncionarioDAO.parseJSON(funcionarios)
            return FuncionarioDAO.escrever(funcionarios)
        return False

    @staticmethod
    def atualizar(funcionario : Funcionario):
        if funcionario.validar():
            funcionarios = FuncionarioDAO.selecionar()
            for f in funcionarios:
                if funcionario.id == f.id:
                    f.nome = funcionario.nome
                    f.registro = funcionario.registro
                    f.salario = funcionario.salario                    
                    break
            funcionarios = FuncionarioDAO.parseJSON(funcionarios)
            return FuncionarioDAO.escrever(funcionarios)
        return False

    @staticmethod
    def deletar(funcionario_id : int):
        funcionarios = FuncionarioDAO.selecionar()
        if len(funcionarios) > 0:            
            for indice, funcionario in enumerate(funcionarios):
                if funcionario.id == funcionario_id:
                    funcionarios.pop(indice)
                    break
            funcionarios = FuncionarioDAO.parseJSON(funcionarios)
            return FuncionarioDAO.escrever(funcionarios)
        return False

    @staticmethod
    def existe(registro : str):    
        for funcionario in FuncionarioDAO.selecionar():            
            if funcionario.registro == registro:
                return True        
        return False

    @staticmethod
    def parseJSON(funcionarios: list):
        funcionarios_dct = []
        for funcionario in funcionarios:
            dct = {}
            for k, v in funcionario.__dict__.items():
                chave = k.replace("_Funcionario__", "").replace("_Pessoa__", "")
                dct[chave] = v
            funcionarios_dct.append(dct)
        return json.dumps(funcionarios_dct)

    @staticmethod
    def escrever(funcionarios : list):
        try:
            arquivo = open(FuncionarioDAO.DEFAULT_FILE, "w", FuncionarioDAO.BUFFER_SIZE)
            arquivo.write(funcionarios)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(FuncionarioDAO.DEFAULT_FILE, "r", FuncionarioDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            funcionarios = []                        
            for c in json.loads(conteudo):                
                funcionario = Funcionario()
                funcionario.id = c["id"]
                funcionario.nome = c["nome"]
                funcionario.registro = c["registro"]
                funcionario.salario = c["salario"]                
                funcionarios.append(funcionario)            
            return funcionarios
        except Exception as ex:
            print(ex)
        return []
		
#Arquivo: Controller/ProdutoDAO.py
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
sys.path.insert(0, "Model")
from Produto import Produto
from CategoriaDAO import CategoriaDAO
import pathlib
import json

"""
Classe de acesso aos dados dos produtos para selecionar, inserir, atualizar e deletar produtos.
"""
class ProdutoDAO:
    
    ATUALIZA_VENDA = 0
    ATUALIZA_COMPRA = 1

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/produtos.json"

    @staticmethod
    def selecionar():        
        return ProdutoDAO.ler() 

    @staticmethod
    def selecionarPorID(produto_id : int):
        for produto in ProdutoDAO.selecionar():
            if produto.id == produto_id:
                return produto
        return None       

    @staticmethod
    def inserir(produto : Produto):        
        produtos = ProdutoDAO.selecionar()
        produto.id = 1 if len(produtos) == 0 else max(c.id for c in produtos) + 1
        if produto.validar():
            produtos.append(produto)                
            produtos = ProdutoDAO.parseJSON(produtos)
            return ProdutoDAO.escrever(produtos)
        return False

    @staticmethod
    def atualizar(produto : Produto):
        if produto.validar():
            produtos = ProdutoDAO.selecionar()
            for p in produtos:
                if produto.id == p.id:
                    p.nome = produto.nome                    
                    p.valor = produto.valor
                    p.quantidade_estoque = produto.quantidade_estoque
                    p.categoria = produto.categoria
                    break
            produtos = ProdutoDAO.parseJSON(produtos)
            return ProdutoDAO.escrever(produtos)
        return False

    @staticmethod
    def atualizar_estoque(produto_id : int, quantidade : int, tipo_atualizacao : int):        
        produtos = ProdutoDAO.selecionar()
        for p in produtos:
            if produto_id == p.id:     
                if tipo_atualizacao == ProdutoDAO.ATUALIZA_COMPRA:           
                    p.quantidade_estoque += quantidade
                else:
                    p.quantidade_estoque -= quantidade
                break
        produtos = ProdutoDAO.parseJSON(produtos)        
        return ProdutoDAO.escrever(produtos)        

    @staticmethod
    def deletar(produto_id : int):
        produtos = ProdutoDAO.selecionar()
        if len(produtos) > 0:            
            for indice, produto in enumerate(produtos):
                if produto.id == produto_id:
                    produtos.pop(indice)
                    break
            produtos = ProdutoDAO.parseJSON(produtos)
            return ProdutoDAO.escrever(produtos)
        return False

    @staticmethod
    def existe(nome : str):    
        for produto in ProdutoDAO.selecionar():            
            if produto.nome == nome:
                return True        
        return False

    @staticmethod
    def parseJSON(produtos: list):
        produtos_dct = []
        for produto in produtos:
            dct = {}
            for k, v in produto.__dict__.items():
                chave = k.replace("_Produto__", "")
                valor = v if chave != "categoria" else v.id
                dct[chave] = valor
            produtos_dct.append(dct)
        return json.dumps(produtos_dct)

    @staticmethod
    def escrever(produtos : list):
        try:
            arquivo = open(ProdutoDAO.DEFAULT_FILE, "w", ProdutoDAO.BUFFER_SIZE)
            arquivo.write(produtos)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(ProdutoDAO.DEFAULT_FILE, "r", ProdutoDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            produtos = []                        
            for c in json.loads(conteudo):                
                produto = Produto()
                produto.id = c["id"]
                produto.nome = c["nome"]
                produto.valor = c["valor"]
                produto.quantidade_estoque = c["quantidade_estoque"]                
                id_categoria = c["categoria"]
                produto.categoria = CategoriaDAO.selecionarPorID(id_categoria)
                produtos.append(produto)            
            return produtos
        except Exception as ex:
            print(ex)
        return []
		
#Arquivo: Controller/VendaDAO.py

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
sys.path.insert(0, "Model")
from Venda import Venda
from Item import Item
from Funcionario import Funcionario
from FuncionarioDAO import FuncionarioDAO
from ClienteDAO import ClienteDAO
from ProdutoDAO import ProdutoDAO
from datetime import datetime
import pathlib
import json

"""
Classe de acesso aos dados das vendas para selecionar, inserir, atualizar e deletar vendas.
"""
class VendaDAO:

    BUFFER_SIZE = 8192
    DEFAULT_FILE = str(pathlib.Path().parent.absolute()) + "/Dados/vendas.json"

    @staticmethod
    def selecionar():        
        return VendaDAO.ler()        

    @staticmethod
    def inserir(venda : Venda):   
        
        vendas = VendaDAO.selecionar()
        venda.id = 1 if len(vendas) == 0 else max(c.id for c in vendas) + 1                
        if venda.validar():
            vendas.append(venda)
            
            vendas = VendaDAO.parseJSON(vendas)
            return VendaDAO.escrever(vendas)
        return False    

    @staticmethod
    def parseJSON(vendas: list):
        vendas_dct = []  
        for venda in vendas:            
            itens = []   
            for item in venda.itens:
                item_dct = {
                    "id" : item.id,
                    "produto_id" : item.produto.id,
                    "quantidade" : item.quantidade,
                    "valor" : item.valor
                }
                itens.append(item_dct)
                
                venda_dct = {
                    "id" : venda.id,
                    "data" : venda.data.strftime('%Y-%m-%d %H:%M:%S'),
                    "funcionario_id" : venda.funcionario.id,
                    "cliente_id" : venda.cliente.id,
                    "itens" : itens
                }
            vendas_dct.append(venda_dct)
        return json.dumps(vendas_dct)

    @staticmethod
    def escrever(vendas : list):
        try:
            arquivo = open(VendaDAO.DEFAULT_FILE, "w", VendaDAO.BUFFER_SIZE)
            arquivo.write(vendas)
            arquivo.close()
            return True
        except Exception as ex:
            print(ex)
        return False

    @staticmethod
    def ler():
        try:
            arquivo = open(VendaDAO.DEFAULT_FILE, "r", VendaDAO.BUFFER_SIZE)
            conteudo = arquivo.read()
            arquivo.close()
            vendas = []                        
            for c in json.loads(conteudo):                
                venda = Venda()
                venda.id = c["id"]                
                venda.data = datetime.strptime(c["data"], '%Y-%m-%d %H:%M:%S')                
                funcionario_id = c["funcionario_id"]                
                venda.funcionario = FuncionarioDAO.selecionarPorID(funcionario_id)                
                cliente_id = c["cliente_id"]                
                venda.cliente = ClienteDAO.selecionarPorID(cliente_id)                
                itens = c["itens"]
                for i in itens:                
                    item = Item()
                    item.id = i["id"]
                    produto_id = i["produto_id"]
                    item.produto = ProdutoDAO.selecionarPorID(produto_id)
                    item.quantidade = i["quantidade"]
                    item.valor = i["valor"] 
                    venda.itens.append(item)
                vendas.append(venda)
            return vendas
        except:
            pass
        return []
		
#Arquivo: Model/Categoria.py
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
		
#Arquivo: Model/Cidade.py
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

#Arquivo: Model/Cliente.py
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

#Arquivo: Model/Compra.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

from Fornecedor import Fornecedor
from datetime import datetime

"""
Classe Compra: Modelo para objetos do tipo Compra.
Cada compra contém um id (int), uma data (datetime), um fornecedor (Fornecedor) da mercadoria e uma lista de Itens (cada um com o seu id (int), seu produto (Produto) e sua respectiva quantidade (int) e seu valor (float) de compra).
"""
class Compra:

    def __init__(self, id_compra : int = None, data : datetime = None, fornecedor : Fornecedor = None, itens : list = None):
        self.__id = id_compra        
        self.__data = data  
        self.__fornecedor = fornecedor
        self.__itens = itens if itens != None and len(itens) > 0 else []
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_compra : int):
        if id_compra > 0:
            self.__id = id_compra
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data : datetime):
        self.__data = data

    @property
    def fornecedor(self):
        return self.__fornecedor
    
    @fornecedor.setter
    def fornecedor(self, fornecedor : Fornecedor):
        if fornecedor != None:
            self.__fornecedor = fornecedor
    
    @property
    def itens(self):
        return self.__itens
    
    @itens.setter
    def itens(self, itens : list):
        if len(itens) > 0:
            self.__itens = itens
        
    def validar(self):
        return self.__id != None and self.__data != None and self.__fornecedor != None and self.__itens != None

#Arquivo: Model/Fornecedor.py
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
		
#Arquivo: Model/Funcionario.py
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
		
#Arquivo: Model/Item.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

from Produto import Produto

"""
Classe Item: Modelo para objetos do tipo Item, os quais servem tanto para a compra quanto para a venda de produtos.
Cada item contém um id (int), um produto (Produto), a sua quantidade (int), e o valor (float) de compra ou venda.
"""
class Item:
    def __init__(self, id_item : int = None, produto : Produto = None, quantidade : int = None, valor : float = None):
        self.__id = id_item
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = valor
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_item : int):
        if id_item > 0:
            self.__id = id_item
    
    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto : Produto):
        if produto != None:
            self.__produto = produto
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade : int):
        if quantidade > 0:
            self.__quantidade = quantidade        
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor : float):
        if valor > 0:
            self.__valor = valor
    
    def validar(self):
        return self.__id != None and self.__produto != None and self.__quantidade != None and self.__valor != None
		
#Arquivo: Model/Pessoa.py
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
			
#Arquivo: Model/Produto.py
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
from Categoria import Categoria

"""
Classe Produto: Modelo para objetos do tipo Produto.
Cada produto contém um id (int), um nome (str), uma categoria (Categoria) a qual pertence, um valor (float) de venda e a quantidade (int) de unidades que possui em estoque.
"""
class Produto:

    def __init__(self, id_produto : int = None, nome : str = None, categoria : Categoria = None, valor : float = None, quantidade_estoque : int = None):
        self.__id = id_produto
        self.__nome = nome
        self.__quantidade_estoque = quantidade_estoque
        self.__categoria = categoria
        self.__valor = valor
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id_produto : int):
        if id_produto > 0:
            self.__id = id_produto
        
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
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria : Categoria):
        if categoria != None:
            self.__categoria = categoria

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor : float):
        if valor >= 0:
            self.__valor = valor   
    
    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque
    
    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque : int):
        if quantidade_estoque >= 0:
            self.__quantidade_estoque = quantidade_estoque   

    def validar(self):
        return self.__id != None and self.__nome != None and self.__categoria != None and self.__valor != None

    """"
    @param quantidade: quantidade de produto a ser atualizada, o valor deve ser positivo
    @param tipo_atualizacao: uma constante que refere se o estoque será atualizado para compra (incremento) ou venda (decremento)
    @return retorna o estado das operações, se o estoque for alterado True, do contrário, False
    """
    def atualizar_estoque(self, quantidade : int, tipo_atualizacao : int):
        if tipo_atualizacao == Produto.ATUALIZACAO_COMPRA:
            self.__quantidade_estoque += quantidade
            return True        
        if tipo_atualizacao == Produto.ATUALIZACAO_VENDA:
            if quantidade <= self.__quantidade_estoque:
                self.__quantidade_estoque -= quantidade
                return True            
        return False

  
#Arquivo: Model/Venda.py
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
		
#Arquivo: View/CaixaView.py	
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Controller")
from VendaDAO import VendaDAO
from datetime import datetime

class CaixaView:
    
    @staticmethod
    def saldo_diario():
        try:
            print("digitar no padrão dd/mm/aa para visualizar faturamento diario")
            hoje = input("Data: ")
            hoje = datetime.strptime(hoje, '%d/%m/%Y')
            data_inicial = hoje.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
            data_final = hoje.replace(hour = 23, minute = 59, second = 59, microsecond = 999999)
            print(" Controle Diário de Caixa: ".center(60, "#"))
            print("Data: de {} até {}.\n".format(data_inicial.strftime("%d/%m/%Y %H:%M:%S"), data_final.strftime("%d/%m/%Y %H:%M:%S")))   
            total = 0.0
            valores_dict = {}
            quantidades_dict = {}
            nomes_dict = {}
            vendas = VendaDAO.selecionar()        
            if vendas != None and len(vendas) > 0:                        
                for venda in vendas:
                    data_venda = datetime.strptime(str(venda.data), "%Y-%m-%d %H:%M:%S")
                    if(data_venda >= data_inicial and data_venda <= data_final):                               
                        for item in venda.itens:
                            sub_total = item.quantidade * item.valor
                            nomes_dict[item.produto.id] = item.produto.nome
                            if item.produto.id not in valores_dict:
                                valores_dict[item.produto.id] = sub_total                        
                                quantidades_dict[item.produto.id] = item.quantidade                        
                            else:
                                valores_dict[item.produto.id] += sub_total
                                quantidades_dict[item.produto.id] += item.quantidade
                            total += sub_total
                for k in valores_dict.keys():
                    print("Produto: {}\nQuantidade vendida: {}\tTotal vendido: ${:.2f}\n".format(nomes_dict[k], quantidades_dict[k], valores_dict[k]))
                print("Valor total: ${:.2f}".format(total))
            print("#" * 60)
            input("Pressione <Enter> para voltar ao menu.")
        except Exception as e:
            print("Data Inválida/Erro")
			
#Arquivo: View/CategoriaView.py
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
				
#Arquivo: View/CidadeView.py
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "View")
sys.path.insert(0, "Controller")
from Cidade import Cidade
from CidadeDAO import CidadeDAO

class CidadeView:

    @staticmethod
    def listar(cidades: list = None):          
        if cidades == None:
            cidades = CidadeDAO.selecionar()
            pausar = True
        print(" Cidades ".center(60, "#"))        
        for c in cidades:
            print("ID: {}. Nome: {}. UF: {}.".format(c.id, c.nome, c.UF))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def adicionar():
        print(" Adicionar Cidade ".center(60, "%"))
        cidade = Cidade()
        cidade.nome = input("Nome: ")
        cidade.UF = input("UF: ")    
        if not CidadeDAO.existe(cidade.nome, cidade.UF):
            if CidadeDAO.inserir(cidade):
                print("Cidade cadastrada com sucesso!")
                CidadeView.listar()
            else:
                print("Falha ao cadastrar a cidade.")
        else:
            print("Cidade já cadastrada.")        
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Cidade ".center(60, "%"))
        cidades = CidadeDAO.selecionar()
        CidadeView.listar(cidades)
        cidade_id = int(input("Informe o ID da cidade a ser atualizada: "))    
        cidade = list(filter(lambda x: x.id == cidade_id, cidades))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cidade.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar UF [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cidade.UF = input("Informe a nova UF: ")
        if CidadeDAO.atualizar(cidade):
            print("Cidade atualizada com sucesso!")    
            CidadeView.listar()
        else:
            print("Falha ao atualizar a cidade. Contate o administrador do sistema!")   
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Cidade ".center(60, "%"))
        CidadeView.listar()   
        cidade_id = int(input("Informe o ID da cidade a ser removida: "))    
        if CidadeDAO.deletar(cidade_id):
            print("Cidade removida com sucesso!")    
            CidadeView.listar()   
        else:
            print("Falha ao remover a cidade. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")
		
#Arquivo: View/ClienteView.py
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
sys.path.insert(0, "Controller")
from Cliente import Cliente
from ClienteDAO import ClienteDAO
from CidadeDAO import CidadeDAO

class ClienteView:

    @staticmethod
    def listar(clientes : list = None):          
        if clientes == None:
            clientes = ClienteDAO.selecionar()       
            pausar = True
        print(" Clientes ".center(60, "#"))        
        for c in clientes:
            cidade = "Não informada" if c.cidade == None else c.cidade.nome + " - "  + c.cidade.UF
            print("ID: {}. Nome: {}. CPF: {}. Logradouro: {}. Número: {}. CEP: {}. Cidade: {}.".format(c.id, c.nome, c.CPF, c.logradouro, c.numero, c.CEP, cidade))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def listar_cidades(cidades : list = None):
        if cidades == None:
            cidades = CidadeDAO.selecionar()       
        pausar = True
        print(" Cidades ".center(60, "#"))        
        for c in cidades:
            print("ID: {}. Nome: {}. UF: {}.".format(c.id, c.nome, c.UF))
        print("#" * 60)         
        if pausar: 
            pass #esse input atrapalhava na hora de inserir um cliente, estava falando que iria voltar ao menu
            #input("Pressione <Enter> para voltar ao menu.")        

    @staticmethod
    def adicionar():
        print(" Adicionar Cliente ".center(60, "%"))
        cliente = Cliente()
        cliente.nome = input("Nome: ")
        cliente.CPF = input("CPF: ")        
        cliente.logradouro = input("Logradouro: ")
        cliente.numero = int(input("Número: "))
        cliente.CEP = input("CEP: ")
        cidades = CidadeDAO.selecionar()
        ClienteView.listar_cidades(cidades)
        cidade_id = int(input("Informe o ID da cidade: "))    
        cliente.cidade = list(filter(lambda x : x.id == cidade_id, cidades))[0]
        if not ClienteDAO.existe(cliente.CPF):
            if ClienteDAO.inserir(cliente):
                print("Cliente cadastrado com sucesso!")
                ClienteView.listar()
            else:
                print("Falha ao cadastrar o cliente.")
        else:
            print("Cliente já cadastrado.")        
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Cliente ".center(60, "%"))
        clientes = ClienteDAO.listar()
        ClienteView.listar(clientes)
        cliente_id = int(input("Informe o ID do cliente a ser atualizado: "))    
        cliente = list(filter(lambda x: x.id == cliente_id, clientes))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar CPF [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.CPF = input("Informe o novo CPF: ")
        entrada = input("Atualizar logradouro [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.logradouro = input("Informe o novo logradouro: ")
        entrada = input("Atualizar número [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.numero = int(input("Informe o novo número: "))
        entrada = input("Atualizar CEP [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cliente.CEP = input("Informe o novo CEP: ")
        entrada = input("Atualizar cidade [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            cidades = CidadeDAO.selecionar()
            ClienteView.listar_cidades(cidades)
            cidade_id = int(input("Informe o ID da nova cidade: "))        
            cliente.cidade = list(filter(lambda x : x.id == cidade_id, cidades))[0]
        if ClienteDAO.atualizar(cliente):
            print("Cliente atualizado com sucesso!")                    
            ClienteView.listar()
        else:
            print("Falha ao atualizar o cliente. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Cliente ".center(60, "%"))        
        ClienteView.listar()
        Cliente_id = int(input("Informe o ID do cliente a ser removido: "))    
        if ClienteDAO.deletar(Cliente_id):
            print("Cliente removido com sucesso!")    
            ClienteView.listar()
        else:
            print("Falha ao remover o cliente. Contate o administrador do sistema!")    
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

#Arquivo: View/CompraView.py
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
sys.path.insert(0, "Controller")
from Compra import Compra
from CompraDAO import CompraDAO
from Item import Item
from FornecedorDAO import FornecedorDAO
from ProdutoDAO import ProdutoDAO
from datetime import datetime

class CompraView:

    @staticmethod
    def visualizarCompras(compras : list = None):          
        if compras == None:
            compras = CompraDAO.selecionar()
        print("-" * 7 + " Compras " + "-" * 7)#
        for compra in compras:
            
            valor_total = 0.0
            
            if(compra.fornecedor == None):
                fornecedor = "Não informado"
            else:
                fornecedor = compra.fornecedor.nome
                
            print("\n" + "-" * 4 + f" Fornecedor: {fornecedor} " + "-" * 4)#
             
            print(f"ID: {compra.id} | Data: {compra.data} | Fornecedor : {fornecedor}")
            
            for item in compra.itens:
                if(item.produto == None):
                    produto = "Não Informado"
                else:
                    produto = item.produto.nome
                
                print(f"Produto: {produto} | Quantidade: {item.quantidade} | Valor: {item.valor}")
                valor_total += item.quantidade * item.valor
            print(f"Valor total: R$ {valor_total:.2f}")


    @staticmethod
    def listar_produtos(produtos : list = None):
        if produtos == None:
            produtos = ProdutoDAO.selecionar()
        print("-" * 7 + " Produtos " + "-" * 7)#        
        for p in produtos:  
            if(p.categoria == None):
                categoria = "Não Informada"
            else:
                categoria = p.categoria.nome
        
            print(f"ID: {p.id} | Nome: {p.nome} | Valor: {p.valor:.2f} | Quantidade em Estoque: {p.quantidade_estoque} | Categoria: {categoria}")

    @staticmethod
    def listar_fornecedores(fornecedores : list = None):
        if fornecedores == None:
            fornecedores = FornecedorDAO.selecionar()
        
        print("-" * 7 + " Fornecedores " + "-" * 7)#                
        for f in fornecedores:
            print(f"ID: {f.id} | Nome: {f.nome} | CNPJ: {f.CNPJ}")

    @staticmethod
    def inserirCompra():
        print("-" * 7 + " Efetuar Compra " + "-" * 7)#  
        compra = Compra()
        compra.itens = []
        item_id = 1
        produtos = ProdutoDAO.selecionar()
        fornecedores = FornecedorDAO.selecionar()
        while(1):
            print(f"Adicionando Item ID: {item_id}")
            CompraView.listar_produtos(produtos)
            produto_id = int(input("Informe o ID do produto a ser comprado: "))            
            produto = ProdutoDAO.selecionarPorID(produto_id)
            
            if(produto == None):
                print("ID não existe")
                continue
            
            
            
            item = Item()
            item.valor = float(input("Valor Unitário: "))
            item.id = item_id
            item.produto = produto        
            item.quantidade = int(input("Informe a quantidade a ser comprada: ")) 
            
            compra.itens.append(item)
            item_id += 1
            
            if(CompraView.opcaoSimNao("Adicionar mais Itens ? Sim ou Não: ") == False):
                break
        
        CompraView.listar_fornecedores(fornecedores)#exibindo lista de fornecedores 
        fornecedor_id = int(input("Informe o ID do fornecedor: "))      
        compra.fornecedor = FornecedorDAO.selecionarPorID(fornecedor_id)
        compra.data = datetime.now()#pega data atual para registrar venda
        if CompraDAO.inserir(compra):
            for item in compra.itens:
                ProdutoDAO.atualizar_estoque(item.produto.id, item.quantidade, ProdutoDAO.ATUALIZA_COMPRA)
            print("Compra efetuada com sucesso!")
        else:
            print("Falha ao efetuar a compra.")
        input("Pressione <Enter> para continuar.")# vamos deixar isso ?
        
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
				
#Arquivo: View/FornecedorView.py
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "View")
sys.path.insert(0, "Controller")
from Fornecedor import Fornecedor
from FornecedorDAO import FornecedorDAO

class FornecedorView:

    @staticmethod
    def listar(fornecedores: list = None):          
        if fornecedores == None:
            fornecedores = FornecedorDAO.selecionar()
        pausar = True
        print(" Fornecedores ".center(60, "#"))
        for f in fornecedores:                                 
            print("ID: {}. Nome: {}\n       CNPJ: {}".format(f.id, f.nome, f.CNPJ))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def adicionar():
        print(" Adicionar Fornecedor ".center(60, "%"))
        fornecedor = Fornecedor()
        fornecedor.nome = input("Nome: ")        
        fornecedor.CNPJ = input("CNPJ: ")        
        if not FornecedorDAO.existe(fornecedor.CNPJ):
            if FornecedorDAO.inserir(fornecedor):
                print("Fornecedor cadastrado com sucesso!")
                FornecedorView.listar()
            else:
                print("Falha ao cadastrar o fornecedor!")
        else:
            print("Fornecedor já cadastrado.")        
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Fornecedor ".center(60, "%"))
        fornecedores = FornecedorDAO.selecionar()
        FornecedorView.listar(fornecedores)
        fornecedor_id = int(input("Informe o id do fornecedor a ser atualizado: "))
        fornecedor = list(filter(lambda x: x.id == fornecedor_id, fornecedores))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            fornecedor.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar CNPJ [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:        
            CNPJ = input("Informe o novo CNPJ: ")
            if FornecedorDAO.existe(CNPJ):
                print("O CNPJ já está vinculado a outro fornecedor.")
            else:
                fornecedor.CNPJ = CNPJ    
        if FornecedorDAO.atualizar(fornecedor):
            print("Fornecedor atualizado com sucesso!")                   
            FornecedorView.listar()
        else:
            print("Falha ao atualizar o fornecedor. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Fornecedor ".center(60, "%"))
        FornecedorView.listar()
        fornecedor_id = int(input("Informe o ID do fornecedor a ser removido: "))    
        if FornecedorDAO.deletar(fornecedor_id):
            print("Fornecedor removido com sucesso!")                
            FornecedorView.listar()
        else:
            print("Falha ao remover o fornecedor. Contate o administrador do sistema!")    
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")
		
#Arquivo: View/FuncionarioView.py
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "View")
sys.path.insert(0, "Controller")
from Funcionario import Funcionario
from FuncionarioDAO import FuncionarioDAO

class FuncionarioView:

    @staticmethod
    def listar(funcionarios: list = None):          
        if funcionarios == None:
            funcionarios = FuncionarioDAO.selecionar()       
        pausar = True
        print(" Funcionários ".center(60, "#"))        
        for f in funcionarios:                                 
            print("ID: {}. Nome: {}. Registro: {}. salario: {:.2f}.".format(f.id, f.nome, f.registro, f.salario))
        print("#" * 60)         
        if pausar:       
            input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def adicionar():
        print(" Adicionar Funcionário ".center(60, "%"))
        funcionario = Funcionario()
        funcionario.nome = input("Nome: ")    
        funcionario.registro = input("Registro: ")    
        funcionario.salario = float(input("Salário: "))
        if not FuncionarioDAO.existe(funcionario.registro):
            if FuncionarioDAO.inserir(funcionario):
                print("Funcionário cadastrado com sucesso!")
                FuncionarioView.listar()
            else:
                print("Falha ao cadastrar o funcionário.")
        else:
            print("Funcionário já cadastrado.")               
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def atualizar():
        print(" Atualizar Funcionário ".center(60, "%"))
        funcionarios = FuncionarioDAO.selecionar()
        FuncionarioView.listar(funcionarios)
        funcionario_id = int(input("Informe o ID do funcionário a ser atualizado: "))
        funcionario = list(filter(lambda x: x.id == funcionario_id, funcionarios))[0]    
        entrada = input("Atualizar nome [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            funcionario.nome = input("Informe o novo nome: ")
        entrada = input("Atualizar registro [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:        
            registro = input("Informe o novo registro: ")
            if FuncionarioDAO.existe(registro):
                print("O registro já está vinculado a outro funcionário.")
            else:
                funcionario.registro = registro
        entrada = input("Atualizar salário [<S> SIM ou <N> NÃO]? ")
        if entrada in ["s", "S"]:
            funcionario.salario = float(input("Informe o novo salário: "))
        if FuncionarioDAO.atualizar(funcionario):
            print("Funcionário atualizado com sucesso!")       
            FuncionarioView.listar()
        else:
            print("Falha ao atualizar o funcionário. Contate o administrador do sistema!")
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def remover():        
        print(" Remover Funcionário ".center(60, "%"))
        FuncionarioView.listar()
        funcionario_id = int(input("Informe o ID do funcionário a ser removido: "))    
        if FuncionarioDAO.deletar(funcionario_id):
            print("Funcionário removido com sucesso!")    
            FuncionarioView.listar()
        else:
            print("Falha ao remover o funcionário. Contate o administrador do sistema!")    
        print("%" *60)
        input("Pressione <Enter> para voltar ao menu.")
		
#Arquivo: View/ProdutoView.py

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
				
#Arquivo: View/RelatorioView.py
__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Controller")
from VendaDAO import VendaDAO

class RelatorioView:
    
    @staticmethod
    def listar_produtos_mais_vendidos():                 
        vendas = VendaDAO.selecionar()
        produtos_dct = {}
        if vendas != None and len(vendas) > 0:                        
            for venda in vendas:                                                
                for item in venda.itens:                                    
                    if item.produto.nome in produtos_dct:
                        produtos_dct[item.produto.nome] += item.quantidade
                    else:
                        produtos_dct[item.produto.nome] = item.quantidade                
            print(" 10 Produtos mais vendidos: ".center(60, "#"))
            index = 1
            for k, v in sorted(produtos_dct.items(), key = lambda item : item[1], reverse = True):
                print("{}° {}: {}.".format(index, k, v))
                index += 1
                if index == 11:
                    break
            print("#" * 60)                  
        else:
            input("Não há produtos vendidos.\nPressione <Enter> para voltar ao menu.")
        input("Pressione <Enter> para voltar ao menu.")

    @staticmethod
    def listar_clientes_mais_compraram():                 
        vendas = VendaDAO.selecionar()
        clientes_dct = {}
        clientes = {}
        if vendas != None and len(vendas) > 0:                        
            for venda in vendas:                          
                clientes[venda.cliente.CPF] = venda.cliente.nome                      
                for item in venda.itens:                                      
                    valor_total = item.quantidade * item.valor
                    if venda.cliente.CPF in clientes_dct:
                        clientes_dct[venda.cliente.CPF] += valor_total
                    else:
                        clientes_dct[venda.cliente.CPF] = valor_total
            print(" 10 Clientes que mais compraram: ".center(60, "#"))
            index = 1
            for k, v in sorted(clientes_dct.items(), key = lambda item : item[1], reverse = True):
                print("{}° {}: ${}.".format(index, clientes[k], v))
                index += 1
                if index == 11:
                    break
            print("#" * 60)                  
        else:
            input("Não há clientes que compraram.\nPressione <Enter> para voltar ao menu.")
        input("Pressione <Enter> para voltar ao menu.")
		
#Arquivo: View/VendaView.py
__author__ = "Grupo C"
__copyright__ = "Copyright 2020, Grupo C"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Natash Polpeta, Gustavo Teles, Jefferson Dias, Vinícius Madureira"
__email__ = ""
__status__ = "Testing"

import sys
sys.path.insert(0, "Model")
sys.path.insert(0, "Controller")
from datetime import datetime
from Venda import Venda
from Funcionario import Funcionario
from VendaDAO import VendaDAO
from Item import Item
from ClienteDAO import ClienteDAO
from FuncionarioDAO import FuncionarioDAO
from ProdutoDAO import ProdutoDAO

class VendaView:

    @staticmethod
    def visualizarVendas(vendas : list = None):          
        if vendas == None:
            vendas = VendaDAO.selecionar()
        print("-" * 7 + " Vendas " + "-" * 7)#        
        vendas = VendaDAO.selecionar()   
        for venda in vendas:
            valor_total = 0.0
            
            if(venda.funcionario == None):
                funcionario = "Não informado"
            else:
                funcionario = venda.funcionario.nome
                
            if(venda.cliente == None):
                cliente = "Não informado"
            else:
                cliente = venda.cliente.nome
                
                
            print(f"ID: {venda.id} | Data: {venda.data} | Funcionário: {funcionario} | Cliente: {cliente}")
            for item in venda.itens:
                print(f"Item ID: {item.id} ")
                
                if(item.produto == None):
                    produto = "Não informado"
                else:
                    produto = item.produto.nome
                    
                print(f"\tProduto: {produto}\n\tQuantidade: {item.quantidade}.\n\tValor: {item.valor:.2f}")
                valor_total += item.quantidade * item.valor
            print(f"Valor total: R$ {valor_total:.2f}")
            print("-----------------------------------------")

        
        input("Pressione <Enter> para continuar.")

    @staticmethod
    def listar_produtos(produtos : list = None):
        if produtos == None:
            produtos = ProdutoDAO.selecionar()
        print("-" * 7 + " Produtos " + "-" * 7)#        
        for p in produtos:  
            if(p.categoria == None):
                categoria = "Não Informada"
            else:
                categoria = p.categoria.nome
        
            print(f"ID: {p.id} | Nome: {p.nome} | Valor: {p.valor:.2f} | Quantidade em Estoque: {p.quantidade_estoque} | Categoria: {categoria}")

    @staticmethod
    def listar_funcionarios(funcionarios : list = None):
        if funcionarios == None:
            funcionarios = FuncionarioDAO.selecionar()
        print("-" * 7 + " Funcionários " + "-" * 7)              
        for f in funcionarios:
            print(f"ID: {f.id} | Nome: {f.nome} | Registro: {f.registro}")

    @staticmethod
    def listar_clientes(clientes : list = None):
        if clientes == None:
            clientes = ClienteDAO.selecionar()
            
        print("-" * 7 + " Clientes " + "-" * 7)
        for c in clientes:
            if c.cidade == None:
                cidade = "Não informada"
            else:
                cidade = c.cidade.nome + " - "  + c.cidade.UF
            
            print(f"ID: {c.id} | Nome: {c.nome} | CPF: {c.CPF} | Logradouro: {c.logradouro} | Número: {c.numero} | CEP: {c.CEP} | Cidade: {cidade}".format(c.id, c.nome, c.CPF, c.logradouro, c.numero, c.CEP, cidade))
              
        

    @staticmethod
    def inserirVenda():
        print(" Efetuar Venda ".center(60, "%"))
        venda = Venda()
        venda.itens = []    
        resposta = "s"
        item_id = 1
        produtos = ProdutoDAO.selecionar()
        clientes = ClienteDAO.selecionar()
        funcionarios = FuncionarioDAO.selecionar()    
        while(1):
            print("-- Item: {item_id} --") 
            VendaView.listar_produtos(produtos)
            produto_id = int(input("Informe o ID do produto a ser vendido: "))            
            produto = list(filter(lambda x: x.id == produto_id, produtos))[0]
            item = Item()
            item.id = item_id
            item.produto = produto        
            item.quantidade = int(input("Informe a quantidade a ser vendida: "))        
            item.valor = produto.valor
            venda.itens.append(item)
            item_id += 1
            
            if(VendaView.opcaoSimNao("Adicionar mais Itens ? Sim ou Não: ") == False):
                break
            
        
        VendaView.listar_clientes(clientes)
        
        while(1):
            cliente_id = int(input("Informe o ID do cliente: ")) 
            venda.cliente = ClienteDAO.selecionarPorID(cliente_id)
            
            if(venda.cliente != None):
                break
            print("ID Inválido")
        
        VendaView.listar_funcionarios(funcionarios)
        
        while(1):
            funcionario_id = int(input("Informe o ID do funcionário: "))            
            venda.funcionario = FuncionarioDAO.selecionarPorID(funcionario_id)
        
            if(venda.funcionario != None):
                break
            print("ID Inválido")
        
        venda.data = datetime.now()
        
        if VendaDAO.inserir(venda):
            for item in venda.itens:
                ProdutoDAO.atualizar_estoque(item.produto.id, item.quantidade, ProdutoDAO.ATUALIZA_VENDA)
            print("Venda efetuada com sucesso!") 
            VendaView.visualizarVendas()
        else:
            print("Falha ao efetuar a venda.")
        input("Pressione <Enter> para Continuar")
        
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


            
            