"""1. Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".


print("Responda cada uma das perguntas com 'SIM' ou 'NÃO'")
#imprime orientações aos usuários 

perguntas = [
            "\nTelefonou para a vítima? ",
            "Esteve no local do crime? ",
            "Mora perto da vítima? ",
            "Devia para a vítima? ",
            "Já trabalhou com a vítima? "
]
#inicializa a linta


sim = []
#inicializa lista vazia


for pergunta in perguntas:
#loop que percorre toda a lista de perguntas 
    
    while True:       
    #loop repete-se até a entrada de respostas válidas
    
        resposta = input(pergunta).upper()
        #inicialização das respostas recebidas pelo input dos usuários e conversão para maiúsculo 
        
        if resposta == "SIM":
            sim.append("SIM")
            break
        elif resposta =="NÃO":
            break
        else:
            ("Resposta inválida. ")
        #bloco que aloca as respostas positivas na lista sim e faz validação de respostas inválidas

if len(sim)>0 and len(sim)<=2:
    print("Suspeito.")
    
elif len(sim)<=4:
    print("Cúmplice.")
    
else:
    print("Assassino.")
#bloco de classificação conforme quantidade de sim e impressão 


"""


#------------------------------------------------------------------------------------------------------------

"""2. Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0. 



medias = []
#inicializa lista vazia

def notas_medias():
#calcula média de 4 notas de 5 alunos e as armazena na lista medias   
    
    for aluno in range(1,6):
        
        soma_nota = 0
        contador = 0
        
        for n in range (1,5):
        
            while True:
                try:            
                    nota = float(input(f'Insira a nota {n} do aluno {aluno}: '))
                    #atribui entrada de dado a variável nota e as converte para float em cada iteração do loop while
                    
                    if nota< 0:
                    #valida nota entrada pelo usuário
                        
                        print("Certifique-se que o valor é maior ou igual a zero.")
                   
                    else:
                        break #encerra loop se a nota for válida
                    
                except ValueError:
                    print("Certifique-se que o valor é um número.")
                    

            soma_nota += nota #atribui variável soma_nota como o somatório das 4 notas
            contador +=1  #contabiliza quantas notas válidas foram inseridas
       
        print("\n")
        
        media = soma_nota/contador #calcula média das notas válidas
        medias.append(media) #concatena os valores da média à lista médias


def media_acima_sete(medias):
#Conta quantas médias são acima de 7 e imprime o valor

    cont=0
    
    for nota_media in medias:
        if nota_media>=7.0:
            cont+=1
            
    print(f'\nQuatidade de aluno com média acima de 7: {cont}')
  

notas_medias() 
media_acima_sete(medias)
#chama funções

print(f'\nMédias: {medias}\n')
#imprime a lista de médias
"""
        
#------------------------------------------------------------------------------------------------------------

"""3. Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra."""



lista_compras_dic = { }
#inicializa dicionário que receberá os itens das compras

print(lista_compras_dic)

lista_compras_dic["Sabonete"] = 10
lista_compras_dic["Chocolate"] = 2
lista_compras_dic["Brócolis"] = 3

print(lista_compras_dic.values() )

quantidade = int(lista_compras_dic["Sabonete"])+ int(lista_compras_dic["Chocolate"])+ int(lista_compras_dic["Brócolis"])

print(f' Total: {quantidade} ')

print(lista_compras_dic)


#------------------------------------------------------------------------------------------------------------

"""4. Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.

dicionario = {"PAULA":5527, "ITALO":5550, "POLYANA":9632, "RAMON":8015, "PAULA FELIX": 89645}
#cria dicionário e atribui a variável dicionario

while True:
#loop para novas consultas ao dicionário

    nome = input("Digite nome ou S para sair: ").upper()
    #solicita chave ao usuário, atribui a vaiável nome e converte a string para maiúscula com método upper
    
    if nome =="S":
    #verifica se o usuário digitou condição que encerrar programa
    
        print("\nAté a próxima.")
        break

    else:

        if nome in dicionario:
        #verifica se a chave informada pelo usuário está no dicionário e imprime seu valor
            print(f'O número de {nome} é {dicionario[nome]}')
        else:
        #imprime msg caso a chave não conste no dicionário
            print(f'\nInfelizmente {nome} não consta em nossa base de dados.')
            

"""


#------------------------------------------------------------------------------------------------------------
"""5. Crie duas tuplas. Concatene-as para formar uma nova tupla.

tupla1 = ("maçã", 3,)
#atribui valor a variável tupla1

tupla2 = ("x", "Python",)
#atribui valor a variável tupla2

tupla3 = tupla1 + tupla2
#concatena tupla 1 com tupla2 e atribui resultado a tupla3


print(tupla1, tupla2, tupla3)
#imprime cada uma das tuplas

"""

#------------------------------------------------------------------------------------------------------------

"""6. Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.        
        

nome = input("Digite o seu nome: ").upper()
#solicita nome ao usuário, passa toda a string para maiúscula e guarda valor na variável nome

print(nome[::-1])
#imprime variável str nome ao contrário

"""

