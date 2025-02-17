"""1 - Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão



print("olá! Vamos calcular? Você digitará dois números!")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Agora, digite o segundo número: "))
#entrada, atribuição e conversão de dados para inteiro


soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2
#define operações matemáticas


print(f'Vocês escolheu os números {numero1} e {numero2}, cuja soma é {soma}, subtração é {subtracao}, multiplicação é {multiplicacao} e divisão é {divisao}.')
#imprime resultados de cada operação matemética

"""
#----------------------------------------------------------

""" 2- Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.


import datetime
#importa biblioteca 


ano_atual = datetime.datetime.now().year
#obtém o ano corrente através da biblioteca datetime e método .now e armazena informação na variável ano_atual

nascimento = int(input("Qual o ano do seu nascimento? "))
#recebe o ano de nascimento do usuario

idade = ano_atual - nascimento
#calcula a idade subtraindo o ano de nascimento de 2025


print(f'Você tem {idade} anos.')
#imprime a idade do usuário"""

#----------------------------------------------------------

""" 3 - Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.

distancia = float(input("Digite a distância em KM: "))
#entrada e conversão de dado para float, atribuição da variável distancia


metros = distancia*1000
centimetros = metros*100
milimetros = metros*1000
#conversão da variável distância para as unidades m, cm e mm



print(f'O valor da distãncia equivale a {metros}m, {centimetros}cm e {milimetros}mm.')
#imprime a distância em diferentes unidade"""
#----------------------------------------------------------

""" 5- Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h


distancia = float(input("Qual a distâcia será percorrida? "))
#entrada e conversão de dado para float, atribuição da variável distancia

aviao = distancia *(1/600)
carro = distancia * (1/100)
onibus = distancia * (1/80)
#conversão do tempo de viagem conforme o meio de transporte

print(f' Você percorreria {distancia}km em {aviao*60:.1f} min de avião, {carro*60:.2f} min de carro e {onibus*60:.2f} min de ônibus')
#imprime o tempo em minutos gasto para percorrer a mesma distância com diferentes meios de transporte

"""

#----------------------------------------------------------

"""6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).

peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))
#solicita dados ao usuários e as atribue as variáveis peso e altura, covertendo-as para float

def calculo_imc (peso, altura):
#calcula índice IMC e trata erros

    try:
        imc = peso/(altura*altura)
        print(f'Seu índice de Massa Corporal é {imc:.1f}.') 
    except TypeError:
        print("Valor informado inválido.")
        
calculo_imc(peso, altura)
#imrpime o IMC conforme dados inseridos pelo usuário

"""
        

#----------------------------------------------------------

"""7. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês.



def entra_dados (): 
#solicita dados ao usuário, realiza validação e atribuição as variáveis valor_hora e horas
    while True:
        try:
            valor_hora = float(input("Informe o valor de sua hora de trabalho: "))
            horas = float(input("Quantas horas você trabalhou no mês: "))
            return valor_hora, horas    
        except ValueError:
            print("Tipo de dado informado inválido.")
            

def salario_calculo(valor_hora, horas): 
#calcula salário e o imprime
    salario = valor_hora*horas
    print(f'Salário: R${salario:.2f}')


valor_hora, horas = entra_dados() #desempacotamento da função
salario_calculo(valor_hora, horas) #chama função com parâmetro

"""


#----------------------------------------------------------
"""8. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.


semanas_mes = 4
#definição da quantidade de semanas em 1 mês como constante
cal_min = 5
#definição da quantidade de calorias queimadas por minuto 

def horas():
#solicita horas por semana em atividade física, realiza validação e atribuição a variável 
    while True:
        try:
            horas_semana = float(input("Quantas horas de exercício você faz por semana? "))
            if horas_semana>0:
                return horas_semana
            else:
                print("Valor inválido. Informe valor maior que zero.")         
                
        except ValueError:
                print ("Valor inválido. Certifique-se que o valor é um número.")
        
    

def total_calorias(horas_semana):
#calcula gasto calórico mensal tomando como base as horas semanais informadas pelo usuário
    
    cal_mes= semanas_mes*horas_semana*cal_min*60
    print(f'Você gasta em média {cal_mes:.1f}cal por mês.')



horas_semana = horas() #desempacotamento da função
total_calorias(horas_semana) #chama função 

"""

#----------------------------------------------------------
"""9 - Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
Lembrando que para o retorno vamos usar print com as variáveis
criadas e este texto é somente um exemplo, utilizem a criatividade

print("Olá, vou te fazer algumas perguntas sobre sua saúde, ok? Vamos lá?!")
#mensagem amigável para interação com usuário


nome = input('Qual o seu nome? ')
idade = int(input ('Qual a sua idade? '))
profissão = input('Me conta qual a tua profissão? ')
remedio = input('Para qual remédio você quer receber alerta? ')
intervalo = int(input("Qual intervalo em dias você deseja receber notificação? "))
#solicita dados aos usuários


print(f' Ficamos felizes em te ajudar, {nome}! Não se preocupe que a cada {intervalo} dias iremos te avisar sobre a compra de {remedio}. Estamos juntos!')
#imprime dados informados pelo usuário 

"""

