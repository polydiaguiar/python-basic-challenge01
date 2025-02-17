"""1. Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.



def soma_dados(a,b,c):
#funcao para somar os argumentos a, b, c e retorna esse valor
    soma = a+b+c
    return soma

resultado = soma_dados(1,2,4)
#atribui o valor da soma de 1,2,4 a variável resultado

print (f'O resultado da soma é {resultado}.')
#imrpime resultado 

"""

#------------------------------------------------------------------------------------------------------------
"""
2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.

def entra_numero():
#função que recebe número que será invertido, realiza validação e só sai do loop com o input de número válido
    
    while True:
        try:   
            num = int(input("Digite um número inteiro: "))
            if num>0:
                return num
            
            else:
                print("Número inválido.")
        
        except ValueError:
            print("Valor inválido. Certifique-se que é um número.")    
        
        
        
def inverte_numero(num):
#função converte número em string e em seguida inverte a ordem desta string aplicando slicing
    numero = str(num)
    
    numero_invertido=(numero[::-1])
    print(f'Número {num} invertido {numero_invertido}')



num = entra_numero() #desempacotamento da função
inverte_numero(num) #chamada da função
"""



#------------------------------------------------------------------------------------------------------------

"""3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta.


def menu():
#função que recebe a temperatura que o usuário deseja converter, apresenta as opções de conversão, guarda a opção desejada na variável opecao
#valida os valores entrados para certificar que são número e string
#chama as funções de conversão adequadas e imprime o valor da conversão na unidade de saída especificada pelo usuário
"""
"""
    while True:
        try:
            temperatura = float(input("Insira a temperatura que deseja converter? "))
            opcao = input(f"""
"""
        == Menu de Conversão ==                     == Unidade de saída ==
    1 - De Fahrenheit (F°) para Celcius (°C)     -->         (C°)
    2 - De Celclius (°C) para Fahrenheit (F°)    -->         (F°)
    Digite opção desejada: """""").strip()"""

"""           
            if opcao == "1":
                temperatura_convertida = converte_para_celsius(temperatura)
                print(f'\nO valor {temperatura} é equivalente a {temperatura_convertida:.1f}°C.')
                break
           
            elif opcao == "2":
                temperatura_convertida = converte_para_fahrenheit(temperatura)
                print(f'\nO valor {temperatura} é equivalente a {temperatura_convertida:.1f}°F.')
                break
            
            else:
                print("\nOpção inválida. Digite 1 ou 2.")            
                
        except ValueError:
            print("\nCertifique-se que o valor é um número. ")
    
        
        
def converte_para_fahrenheit(temperatura):
#função que converte temperatura de celsius para fahrenheit e retorna seu valor 
    temp_fahrenheit = 1.8*temperatura +32
    return temp_fahrenheit
    
    
def converte_para_celsius(temperatura):
#função que converte temperatura de fahrenheit para celsius e retorna seu valor 
    temp_celsius = (temperatura - 32)/1.8
    return temp_celsius
    
menu() 
#chamda de função"""



#------------------------------------------------------------------------------------------------------------
"""4. Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21


def ler_dinheiro():
#função para receber vaor do dinheiro na carteira, valida e guarda este valor na variável saldo

    while True: 
        try:
            saldo = float(input('Digite quando dinheiro você tem na sua carteira: '))
            if saldo>=0:
                return saldo
            else:
                print("Certifique-se que o valor é maior que zero.")
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def converte_moeda (saldo):
#converte o valor saldo para várias outras moedas retornando a conversão para o usuário
    
    dolar_americano = saldo/4.91
    peso_argentino = saldo/0.02
    dolar_australiano = saldo/3.18
    dolar_canadense = saldo/3.64
    franco_suico = saldo/0.42
    euro = saldo/5.36
    libra_esterlina = saldo/6.21
    
"""

"""
print(f"""
"""
Seu saldo em carteira de {saldo} equivale a:

Dólar Americano: $ {dolar_americano:.2f}
Peso Argentino: $ {peso_argentino:.2f}
Dólar Australiano: A$ {dolar_australiano:.2f}
Dólar Canadense: C$ {dolar_canadense:.2f}
Franco Suiço: SFr {franco_suico:.2f}
Euro: Є {euro:.2f}
Libra esterlina: £ {libra_esterlina:.2f}


)
    
saldo = ler_dinheiro() #desempacotamento de função
converte_moeda(saldo) #chamada de função

"""

#------------------------------------------------------------------------------------------------------------
"""5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.


def solicita_frase():
#recebe palavra ou frase para contagem de vogais, retorna o input convertido para maiúsculo e sem espaço em branco

    frase = input("Digite uma palavra ou frase e eu te direi quantas vogais ela tem: ").upper().strip()
    return frase

def contar_vogais(frase):
#implementa contador com laço for que itera sobre cada letra da variável frase, checa se é uma vogal comparando com a lista vogais e retorna a contagem
    
    vogais=["A","E","I","O","U"]
    contador=0
    

    for vogal in frase: 
        if vogal in vogais:
            contador += 1
        
    return contador

#desempacota função
frase = solicita_frase() 
quant_vogais = contar_vogais(frase)

#imprime a quantidade de vogais
print(f'A quantidade de vogais é {quant_vogais}')

"""


#------------------------------------------------------------------------------------------------------------

"""6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício"""
import random

lista = [["A","M", "O","R"],["C", "A","S","A"],["T","E","R","R","A"],["B","O","L","A"],["F","O","L","H","A"]]

print(lista[0,0])