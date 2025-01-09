import time
import math

def exe1_1():
    #Crie um programa que armazene seu nome e sua idade em variáveis separadas e imprima uma saída formatada com elas.
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    print(f"Seu nome é {nome} e sua idade é de {idade} anos")

def exe1_2():
    #Crie um programa que armazene dois números em variáveis separadas e imprima a soma, subtração, multiplicação e divisão desses números.
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    print(f"A soma do {num1} com o {num2} é igual a {num1+num2} \nA subtração de {num1} por {num2} é igual a {num1-num2}")
    print(f"A multiplicação do {num1} por {num2} é igual a  {num1*num2} \nA divisão do {num1} por {num2} é igual a {num1/num2:.2f}")

def exe1_3():
    #Crie um programa que peça ao usuário para digitar três números, armazenando-os em variáveis distintas. Em seguida, imprima a média aritmética dos três números.
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite segundo número: "))
    num3 = int(input("Digite terceiro número: "))
    numeros = [num1, num2, num3]
    media = sum(numeros)/len(numeros)
    print(f"A média aritmética dos números digitados é {media:.2f}")

def exe1_4():
    #Crie um programa que peça ao usuário para digitar seu peso e sua altura. Em seguida, calcule o índice de massa corporal(IMC) e imprima o resultado. A fórmula do IMC é: IMC = peso/altura
    peso = float(input("Digite seu peso: "))
    alt = float(input("Digite sua altura: "))
    print(f"O seu IMC é {peso/(alt**2):.2f}")
    #ou
    # imc = peso/(alt**2)
    # print(f"Seu IMC é de {imc:.2f}")

def exe1_5():
    #Crie um programa que peça ao usuário para digitar tr~es números e imprima a soma do dobro de cada um deles.
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite segundo número: "))
    num3 = int(input("Digite terceiro número: "))
    soma = (num1*2)+(num2*2)+(num3*2)
    print(f"A soma do dobro de números de é {soma}")

def exe1_6():
    #Crie um programa que peça ao usuário para digitar um número. Em seguida, o programa deve calcular e mostrar a raiz quadrada desse número
    num = int(input("Digite um número: "))
    print(f"A raiz quadrada do número é {num*num}")

def exe1_7():
    #Crie um programa que peça ao usuário para digitar um número inteiro. Em seguida, o programa deve calcular e 
    # mostrar o valor dos inteiros anterior e posterior a esse número.
    num= int(input("Digite um número: "))
    ant = num - 1
    post = num + 1
    print(f"O número anterior é {ant} e o posterior é {post}")

def exe1_8():
    #Crie um programa que peça ao usuário para digitar um ângulo entre 0 e 360 graus. 
    #Em seguida, o programa deve calcular e mostrar o seno, cosseno e tangente desse número.
    ang = int(input("Digite um ângulo entre 0  e 360: "))
    seno = math.sin(math.radians(ang))
    coss = math.cos(math.radians(ang))
    tang = math.tan(math.radians(ang))
    print(f"O ângulo digitado foi {ang} \nO Seno é de {seno:.2f}\nO Cosseno é de {coss:.2f} \nA Tangente é de {tang:.2f}")

def exe1_9():
    #Crie um programa que peça ao usuário para digitar dois números quaisquer. 
    #Em seguida, o programa deve calcular e mostrar a potência do primeiro número pelo segundo.
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um outro número: "))
    pot = num1**num2
    print(f"A potênciação de {num1} por {num2} é igual a {pot}")

def exe1_10():
    #Crie um programa que peça ao usuário para digitar três números (A, B e C). 
    # Em seguida, o programa deve calcular e mostrar os valores das raízes da seguinte equação, usando a fórmula de Bhaskara.
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = (b)**2 - (4*a*c)

    if delta == 0: #delta = a 0 possui apenas uma raiz
        raiz = (-b)/2*a
        print(f"A raiz da equação é {raiz}")
    elif delta > 0:
        raiz1 = ((-b)+math.sqrt(delta))/2*a
        raiz2 = ((-b)-math.sqrt(delta))/2*a
        print(f"A raiz x' da equação é {raiz1} \nA raiz x'' da equação é {raiz2}")
    else: #quando o número é negativo, não possui raiz
        print("Não possui raízes reais.")

def exe1_11():
    #Crie um programa que peça ao usuário para digitar o raio de um círculo. 
    #Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.
    raio = int(input("Digite o raio do círculo: "))
    print(f"A área do círculo é {math.pi*(raio**2):.2f}") #por estar usando a biblioteca math.pi, o valor vai tender para acima
    print(f"O comprimento do círculo é {2 * math.pi * raio:.2f}") #se fosse 3.14 definido, o valor seria um pouco mais baixo

#08/01/2025
def exe1_12():
    #Crie um programa que peça ao usuário para digitar as dimensões de um retângulo (largura e altura). 
    #Em seguida, o programa deve calcular e mostrar a área e o perímetro desse retângulo.
    larg = int(input("Digite a largura do retângulo: "))
    altu = int(input("Digite a altura do retângulo: "))
    area = larg * altu
    perim = larg*2 + altu * 2
    print(f"A área do retâgulo é {area} e o perímetro do retângulo é {perim}")

def exe1_13():
    #Crie um programa que peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, o programa deve calcular e mostrar a área desse triângulo.
    base = int(input("Digite a base do triângulo: "))
    altu = int(input("Digite a altura do triângulo: "))
    area = (base*altu)/2
    print(f"A área do triãngulo é {area}")

def exe1_14():
    #Crie um programa que peça ao usuário para digitar o nome, o preço de custo, o preço de venda e a quantidade em estoque de determinado produto. 
    #Em seguida, o programa deve calcular e mostrar o lucro que esse produto pode gerar se todo o estoque for vendido.
    nome = input("Digite o nome do produto: ")
    p_custo = float(input("Digite o preço de custo do produto: "))
    p_venda = float(input("Digite o preço de venda do produto: "))
    estoq = int(input("Digite a quantidade em estoque od produto: "))
    lucro = (p_venda*estoq) - (p_custo*estoq)
    print(f"Caso {nome} seja tenha todo o estoque vendido, o lucro será de R${lucro}")

def exe1_15():
    #Crie um programa que peça ao usuário para digitar o valor total de uma venda, o percentual de desconto aplicado e o percentual de imposto cobrado. 
    #Ao fim, o programa deve mostrar o preço final da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.
    val_tot = float(input("Digite o valor total da venda: "))
    desc = float(input("Digite o percentual de desconto do produto: "))
    imposto = float(input("Digite o percentual do imposto: "))
    v_final = val_tot*(1-desc/100)*(1+imposto/100)
    print(f"O produto teve valor final de R${v_final:.2f}")





def menu():
    while True:
        time.sleep(2)
        print("\n")
        for i in range(1,16):
            print(f"Questão {i}")

        op = int(input("\nDigite uma opção:"))

        match op:
            case 1:
                exe1_1()
            case 2:
                exe1_2()
            case 3:
                exe1_3()
            case 4:
                exe1_4()
            case 5:
                exe1_5()
            case 6:
                exe1_6()
            case 7:
                exe1_7()
            case 8:
                exe1_8()
            case 9:
                exe1_9()
            case 10:
                exe1_10()
            case 11:
                exe1_11()
            case 12:
                exe1_12()
            case 13:
                exe1_13()
            case 14:
                exe1_14()
            case 15:
                exe1_15()

menu()

#Por enquanto está assim, por conta de não está conseguindo importar outro arquivo para o main

# Exercício 1.16 (Difícil):
# Crie um programa que peça ao usuário para digitar a massa e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a força resultante.

# Exercício 1.17:
# Crie um programa que peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de transição de uma velocidade para a outra. Em seguida, o programa deve calcular e mostrar a aceleração.

# Exercício 1.18:
# Crie um programa que peça ao usuário para digitar o valor da medida de um ângulo em radianos. Em seguida, o programa deve calcular e mostrar o valor desse ângulo em graus.

# Exercício 1.19:
# Crie um programa que peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo. Em seguida, o programa deve calcular e mostrar o comprimento da hipotenusa.

# Exercício 1.20:
# Crie um programa que peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto no trajeto. Em seguida, o programa deve calcular e mostrar a velocidade média do objeto.

# Exercício 1.21 (Difícil):
# Crie um programa que peça ao usuário para digitar a distância percorrida, o tempo gasto e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a velocidade inicial e final.

# Exercício 1.22:
# Crie um programa que calcule e mostre o perímetro de um círculo dado o seu raio como entrada.

# Exercício 1.23:
# Crie um programa que calcule e mostre o volume de uma esfera dado o seu raio como entrada.

# Exercício 1.24:
# Crie um programa que calcule e mostre a área de um triângulo retângulo dadas as medidas dos seus catetos como entrada.