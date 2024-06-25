"""
Módulo feito em conjunto por Luiz e Ximena em 20/06
Objetivo: minerar dados do site escolhido
"""

import requests
from bs4 import BeautifulSoup
import clean



#Link para o site
LINK = "https://www.skoob.com.br"

def coletar_informacoes(id_livro):
    #Coletar informações contidas na páginas do livro
    url = LINK+"/livro/"+str(id_livro)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    barra_superior = soup.find('div', id="livro-perfil-status")

    #Caso o id passado não corresponda a um livro, ignorá-lo
    try:  estrelas = float(barra_superior.find('span').text.strip())
    except: return False

    barra_superior = barra_superior.find_all('div', class_="bar")
    resenhas = clean.cleanInt(barra_superior[0].find('b').find('a').text)
    
    #Caso o livro não seja muito conhecido, ignorá-lo
    if resenhas <=1000: return False

    abandonos = clean.cleanInt(barra_superior[1].find('b').find('a').text)
    relendo = clean.cleanInt(barra_superior[2].find('b').find('a').text)
    querendo = clean.cleanInt(barra_superior[3].find('b').find('a').text)
    lendo = clean.cleanInt(barra_superior[4].find('b').find('a').text)
    leram = clean.cleanInt(barra_superior[5].find('b').find('a').text)
    
    barra_lateral = soup.find('div', id="pg-livro-menu-principal-container")
    imagem = barra_lateral.find('img', class_="cpimg").get('src')
    titulo = barra_lateral.find('strong', class_="sidebar-titulo").text.strip()
    autor = barra_lateral.find_all('a')[1].text.strip()
    ano, paginas, editora = clean.cleanText(barra_lateral.find('div', class_="sidebar-desc").text)
    
    qtdMulheres = soup.find('span', class_="pg-livro-icone-female-label").text.strip()
    qtdHomens =soup.find('span', class_="pg-livro-icone-male-label").text.strip()

    livro = {
        "id": id_livro,
        "imagem": imagem,
        "titulo": titulo,
        "autor": autor, 
        "ano": ano, 
        "paginas": paginas, 
        "editora": editora, 
        "estrelas": estrelas, 
        "resenhas": resenhas, 
        "abandonos": abandonos, 
        "relendo": relendo, 
        "querendo": querendo, 
        "lendo": lendo, 
        "leram": leram,
        "qtdHomens": qtdHomens,
        "qtdMulheres": qtdMulheres
    }
    return livro

def coletar_avaliacoes(id_livro):
    #Coletar avaliações dos livros
    avaliacoes = []
    for i in range(2):
        url = LINK+"/livro/resenhas/"+str(id_livro)+"/mpage:"+str(i+1)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        divs = soup.find_all('div', id=lambda x: x and x.startswith('resenhac'))
        for div in divs:
            avaliacoes.append(clean.cleanAvaliacao(div.find('span').text.strip(), div.text.strip()))   
    return avaliacoes

