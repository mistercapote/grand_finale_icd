"""
Módulo feito por Ximena Breatriz Gomez Flores em 22/06
Objetivo: limpar os dados minerados do site
"""


def cleanText(texto):
    #Função que corrige textos da barra lateral
    ano = ""
    paginas = "" 
    editora = ""
    
    for i in range(len(texto)):
        if(texto[i:i+4]=='Ano:'):
            i = i + 5
            while(texto[i] != ' '):
                ano = ano + texto[i]
                i = i + 1 

        if(texto[i:i+8]=='Páginas:'):
            i = i + 9
            while(texto[i] != ' '):
                paginas = paginas + texto[i]
                i = i + 1 

        if(texto[i:i+8] == 'Editora:'):
            i = i + 9
            while(i != len(texto)):
                editora = editora + texto[i]
                i = i + 1 
    
    return int(ano), int(paginas), editora.strip()

def cleanInt(n):
  #Função que corrige numeros minerados
  numero=""
  for i in n:
    if(i != '.'):
      numero = numero + i
  return int(numero)


def cleanAvaliacao(data, texto):
  #Função quer corrige o texto da avaliação
  ss=""
  ind=0
  for i in range(len(texto)):
    if data == texto[i:i+10]  and texto[i+2]=='/':
      ind = i+10
  
  ss = texto[ind: ind + len(texto)]
  return ss