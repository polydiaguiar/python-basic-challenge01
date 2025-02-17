"""1. Faça um Programa que peça dois números e imprima o maior deles.

n1 =int(input('Digite um número: '))
n2 =int(input('Digite um segundo número: '))

if n1>n2:
    print(f'O maior número é {n1}')
else:
    print(f'O maior número é {n2}')


"""
#----------------------------------------------------------

"""2. Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turno = input(f'Em qual turno você estuda? Digite "M"-matutino ou "V"-Vespertino ou "N"- Noturno ')

if turno == "M":
    print('Bom dia!')
elif turno=="V":
    print('Boa Tarde!')
elif turno=="N":
    print('Boa Noite!')
else:
    print('Valor inválido!')

#outra opção 


mensagem = {
    "M": "Bom Dia!",
    "V": "Boa Tarde!",
    "N": "Boa Noite!"
}

turno = input(f'Em qual turno você estuda? Digite "M"-matutino ou "V"-Vespertino ou "N"- Noturno ').upper()

while len(turno) != 1 or turno not in mensagem:   
    print('Opção inválida! Por favor, digite apenas um caractere entre "M", "V" ou "N".')
    turno = input(f'Em qual turno você estuda? ').upper()
    
print(mensagem[turno])

#----------------------------------------------------------

    
"""3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido."""


nota = int(input('Digite uma nota entre 0 e 10: '))

while nota< 0 or nota>10:
    print("Valor inválido.")
    nota = int(input('Digite uma nota entre 0 e 10: '))

#----------------------------------------------------------

"""4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado."""

nota = int(input('Digite uma nota entre 0 e 10: '))

while nota< 0 or nota>10:
    print("Valor inválido.")
    nota = int(input('Digite uma nota entre 0 e 10: '))

if nota >= 7:
    print("Aluno aprovado. Parabéns!")

else:
    print("Aluno reprovado.")

#----------------------------------------------------------

"""5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas."""

print("Vamos aprender a classificar os triângulos? ")

a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
b = float(input("Digite o comprimento do secundo lado do triângulo: "))
c = float(input("Digite o comprimento do terceiro lado do triângulo: "))

while a<=0 or b<=0 or c<=0:
    print("\nLembre que grandezas físicas não podem ser negativas, o número tem que ser maior que 0.")
    a = float(input("\nDigite o comprimento do primeiro lado do triângulo: "))
    b = float(input("Digite o comprimento do secundo lado do triângulo: "))
    c = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if a==b==c:
    print("Triângulo equilátero.")
    
elif a!=b!=c:
    print("Triângulo é escaleno.")

else:
    print("Triângulo isósceles.")

#----------------------------------------------------------

"""6 Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for admin e a senha
for "admin123", caso contrário imprima uma mensagem de erro"""


while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == "admin" and senha == "admin123":
        print ("Login realizado com sucesso.")
        break 
     
    else:
        print("\nSenha ou usuário errado. Tente novamente.")


#----------------------------------------------------------

"""7. Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso
Criança: Até 12 anos incompletos
Adolescente: Entre 12 e 18 anos incompletos
Adulto: Entre 18 e 59 anos
Idoso: A partir de 60 anos"""

while True:
    idade = int(input("Idade: "))    
    
    if idade <= 0:
        print("\nIdade inválida. Digite novamente.")
    
    else:
        if idade<12:
            print("Criança")

        elif idade<18:
            print("Adolescente")
            
        elif idade<60:
            print("Adulto")
        else:
            print("Idoso")
        break
    


#----------------------------------------------------------

"""8. Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado."""


num1 = float(input("Escolha o primeiro número: "))
num2 = float(input("Escolha o segundo número: "))
num3 = float(input("Escolha o terceiro número: "))

if num1==num2==num3:
    print("Os números são iguais.")
    exit()

if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)


#----------------------------------------------------------

"""9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos."""


par=[]
impar=[]

print(" \nPara encerrar o programa digite 0.\n")

while True:
    
    numero = int(input("Digite um número: "))
    
    if numero ==0:
        break
    
    if numero <0:
        print("Número inválido, certifique-se que o número escolhido é maior que 0.")
        
    elif numero%2==0:
        par.append(numero)
    
    else:
        impar.append(numero)
    

total_pares = len(par)    
total_impar = len(impar)


def concordancia(total, plural, singular):
    if total>1: 
        return plural 
    else:
        return singular


a = concordancia(total_pares, "números pares", "número par")
b = concordancia(total_impar, "números ímpares", "número ímpar")

    
print (f'Você digitou {total_pares} {a} e {total_impar} {b}.')


#----------------------------------------------------------

"""10. Faça um programa que lê três números inteiros e os mostra em ordem
crescente."""

num1= 8
num2=-1
num3=-22

numeros=[]
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)

numeros.sort()

print(numeros)

#----------------------------------------------------------

"""11. Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.

Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%."""


bruto = float(input("Informe o seu salário bruto: "))

while bruto<=0:
    print("Valor inválido.")
    bruto = float(input("Informe o seu salário bruto: "))
    
def liquido(bruto, aliquota):
    liquido = bruto - (bruto*aliquota)
    return liquido

def mensagem(liquido, aliquota):
    print(f'Salário líquido: R${liquido(bruto,aliquota):.2f}   (aliquota: {aliquota*100:.1f}%) ')  
    

    

if bruto <= 1903.98:
    print("Salário isento de IR.")
    
elif bruto <= 2826.65:
    
    aliquota = 7.5/100
    mensagem(liquido,aliquota)
    
elif bruto <= 3751.05:
    
    aliquota = 15/100
    mensagem(liquido,aliquota)    

elif bruto <=4664.68:
    aliquota = 22.5/100
    mensagem(liquido,aliquota) 


else:
    aliquota = 27.5/100
    mensagem(liquido,aliquota) 



    

    

