import math

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


def exe1_16():
# Crie um programa que peça ao usuário para digitar a massa e a aceleração de um objeto. Em seguida, o programa deve calcular e mostrar a força resultante.
# f = m*a
    massa = float(input("Digite a massa de um objeto em kg: "))
    acel = int(input("Digite a aceleração em m/s: "))
    print(f"A força resultante do objeto é de {massa*acel:.2f}N")


def exe1_17():
# Crie um programa que peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de transição de uma velocidade para a outra. Em seguida, o programa deve calcular e mostrar a aceleração.
#am= delta v / delta t
    vinit = float(input("Digite a aceleração inicial - em m/s: "))
    vfinal = float(input("Digite a velocidade final - em m/s: "))
    tinit = float(input("Digite o tempo inicial - em segundos: "))
    tfinal = float(input("Digite o tempo final - em segundos: "))
    acel = (vfinal-vinit)/(tfinal-tinit)
    print(f"A aceleração média final foi de {acel}m/s²")


def exe1_18():
# Crie um programa que peça ao usuário para digitar o valor da medida de um ângulo em radianos. Em seguida, o programa deve calcular e mostrar o valor desse ângulo em graus.
    rad = int(input("Digite o radiano: "))
    divisor = int(input("Digite o divisor do rad - se não tiver, digite 1: "))
    if divisor == 1:
        graus = (rad*180)/math.pi
    else:
        graus = (rad * 180)/divisor
    print(f"O valor do ângulo em graus é de {graus:.1f}°")

# Exercício 1.19:
# Crie um programa que peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo. Em seguida, o programa deve calcular e mostrar o comprimento da hipotenusa.

# Exercício 1.20:
# Crie um programa que peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto no trajeto. Em seguida, o programa deve calcular e mostrar a velocidade média do objeto.
