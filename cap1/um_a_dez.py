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