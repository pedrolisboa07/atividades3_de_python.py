import calculadora
import utilidades

def adicionar_item_seguro(lista_original, item):
    #adiciona um item a uma lista sem alterar a lista original 
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista

def executar_demonstracao():
    #executa chamadas demonstrativas das funções
    print("--- Testando Calculadora ---")
    print(f"Soma (5 + 3): {calculadora.somar(5, 3)}")
    print(f"Divisão por zero (5 / 0): {calculadora.dividir(5, 0)}")

    print("\n--- Testando Utilidades ---")
    f_temp = utilidades.converter_celsius_para_fahrenheit(25)
    print(f"25°C em Fahrenheit: {f_temp}°F")
    
    senha_valida = utilidades.validar_senha("12345")
    print(f"Senha '12345' é válida? {senha_valida}")
    
    total_caixa = utilidades.calcular_caixa(10.50, 20.00, 5.75)
    print(f"Total do caixa (*precos): R$ {total_caixa:.2f}")
    
    ficha = utilidades.gerar_ficha_aluno(nome="João", idade=20, curso="Python")
    print(ficha)

    print("--- Testando Lista Segura ---")
    lista_inicial = [1, 2, 3]
    nova_lista = adicionar_item_seguro(lista_inicial, 4)
    print(f"Lista Original (inalterada): {lista_inicial}")
    print(f"Nova Lista: {nova_lista}")

if __name__ == "__main__":
    executar_demonstracao()
