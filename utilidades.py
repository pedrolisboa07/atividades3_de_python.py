def converter_celsius_para_fahrenheit(celsius):
    #converte a temperatura de celsius pafa fahrenheit 
    return (celsius * 9/5) + 32

def validar_senha(senha):
    #valida se uma senha possui 8 caracteres 
    return len(senha) >= 8

def calcular_caixa(*precos):
    #calcula o valor total a partir de uma quantidade produtos
    return sum(precos)

def gerar_ficha_aluno(**dados):
   #gera uma string formatada
    ficha = "Ficha do Aluno:\n"
    for chave, valor in dados.items():
        ficha += f"- {chave.title()}: {valor}\n"
    return ficha
  
