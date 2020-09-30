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