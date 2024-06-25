"""
Módulo feito por Luiz em 20/06
Objetivo: gerenciar os demais módulos

RODE ESSE MÓDULO PARA INICIAR A RASPAGEM
"""

import insights
import output
import mine

#Inserção da chave OpenAI
CHAVE = input("Insira chave da OpenAI: ")

def main():
    print("deu certo")
    #Criar arquivo CSV com PANDAS, verificar existencia com OS:
    output.create()

    #Para cada livro cadastrado no site:
    for i in range(1,113784):
        #Coletar dados acerca do livro
        livro = mine.coletar_informacoes(i)
        if livro == False: continue
        avaliacoes = mine.coletar_avaliacoes(i)

        #Usar a OpenAI para gerar novos dados:
        livro["avaliacao"], livro["sentimento"] = insights.interpretar(avaliacoes, CHAVE)
        livro["genero"] = insights.avaliarCategoria(livro["titulo"], CHAVE)
        #Adicionar nova linha ao CSV com PANDAS
        output.add(livro)

        #Print para notificar em qual livro está
        print(f'Livro {i} - "{livro["titulo"]}" adicionado ao CSV')

main()
