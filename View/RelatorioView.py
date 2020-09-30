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