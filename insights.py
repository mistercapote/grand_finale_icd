"""
Módulo feito por Ximena Breatriz Gomez Flores em 22/06
Objetivo: solicitar ao ChatGPT que gere mais dados para serem trabalhados
"""

from openai import OpenAI

#Funcao para solicitar palavra a ChatGPT
def chat(prompt, chave, model = "gpt-3.5-turbo-0125", max_tokens = 800, temperature = 0.5):
    #Iniciar chat com o GPT
    client = OpenAI(api_key=chave)
    resposta = client.chat.completions.create(
        messages = prompt,
        model = model,
        max_tokens = max_tokens,
        temperature = temperature
    )
    return resposta.choices[0].message.content

def interpretar(avaliacoes, chave):
    #Gerar resumo das avaliações e dar o veredito
    texto = f"Condidere a seguinte lista de avaliações acerca de um livro: {avaliacoes}."
    
    prompt = [{"role":"user", "content":f"{texto} Resuma todas as avaliações em um texto de um paragrafo."}]
    avaliacaoMedia = chat(prompt, chave)

    prompt = [{"role":"user", "content":f"{texto} Dê o veredito sobre o livro. Retorne APENAS 'Bom', 'Mediano' ou 'Ruim'."}]
    sentimento = chat(prompt, chave, max_tokens=500)
    return avaliacaoMedia, sentimento

def avaliarCategoria(titulo, chave):
    #Gerar gênero literário do livro
    generos = "Arte, Biografia, Negócios, Infantil, Clássico, Quadrinho, Receita, Fantasia, Romance, Acadêmico, Ficção Histórica, História, Terror, Memórias, Música, Mistério, Poesia, Conto, Romance, Ciência, Ficção Científica, Autoajuda, Esportes"
    prompt = [{"role":"user", "content":f"A qual destes generos {generos}, o livro {titulo} pertence. Dê como resposta apenas a palavra da categoria"}]
    categoria = chat(prompt, chave, max_tokens=150)
    return categoria
