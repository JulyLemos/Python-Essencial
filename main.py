import time

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


def menu():
    while True:
        time.sleep(2)
        print("\n")
        for i in range(1,7):
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

menu()

#Por enquanto está assim, por conta de não está conseguindo importar outro arquivo para o main