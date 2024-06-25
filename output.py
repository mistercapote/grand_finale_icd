"""
Módulo feito por Luiz Eduardo Bravin em 22/06
Objetivo: gerenciar o arquivo CSV, saída do programa
"""

import pandas as pd
import os

PATH = 'god_pinho_final.csv'
def create():
    #Criação do arquivo CSV, caso ainda não criado
    if not os.path.exists(PATH):
        dataset = pd.DataFrame({
                    "ID": [],
                    "Título": [],
                    "Autor": [], 
                    "Ano da edição": [], 
                    "Páginas": [], 
                    "Editora": [], 
                    "Gênero": [],
                    "Estrelas": [], 
                    "Já leram": [],
                    "Lendo": [], 
                    "Querendo ler": [], 
                    "Relendo": [], 
                    "Abandonos": [], 
                    "Resenhas": [], 
                    "Homens": [],
                    "Mulheres": [],
                    "Avaliação": [],
                    "Sentimento": [],
                    "Imagem": []
        })
        dataset.to_csv(PATH, index=False)
    return 


def add(produto):
    #Inserção de cada livro ao CSV
    dataset = pd.DataFrame({
                    "ID": [produto["id"]],
                    "Título": [produto["titulo"]],
                    "Autor": [produto["autor"]], 
                    "Ano da edição": [produto["ano"]], 
                    "Páginas": [produto["paginas"]], 
                    "Editora": [produto["editora"]], 
                    "Gênero": [produto["genero"]],
                    "Estrelas": [produto["estrelas"]], 
                    "Já leram": [produto["leram"]],
                    "Lendo": [produto["lendo"]], 
                    "Querendo ler": [produto["querendo"]], 
                    "Relendo": [produto["relendo"]], 
                    "Abandonos": [produto["abandonos"]], 
                    "Resenhas": [produto["resenhas"]], 
                    "Homens": [produto["qtdHomens"]],
                    "Mulheres": [produto["qtdMulheres"]],
                    "Avaliação": [produto["avaliacao"]],
                    "Sentimento": [produto["sentimento"]],
                    "Imagem": [produto["imagem"]]
    })
    dataset.to_csv(PATH, mode='a', header=False, index=False)
    return
