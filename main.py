import time
from cap1 import um_a_dez, onze_a_vinte


def menu():
    while True:
        time.sleep(2)
        print("\n")
        for i in range(1,19):
            print(f"Questão {i}")

        op = int(input("\nDigite uma opção:"))

        match op:
            case 1:
                um_a_dez.exe1_1()
            case 2:
                um_a_dez.exe1_2()
            case 3:
                um_a_dez.exe1_3()
            case 4:
                um_a_dez.exe1_4()
            case 5:
                um_a_dez.exe1_5()
            case 6:
                um_a_dez.exe1_6()
            case 7:
                um_a_dez.exe1_7()
            case 8:
                um_a_dez.exe1_8()
            case 9:
                um_a_dez.exe1_9()
            case 10:
                um_a_dez.exe1_10()
            case 11:
                onze_a_vinte.exe1_11()
            case 12:
                onze_a_vinte.exe1_12()
            case 13:
                onze_a_vinte.exe1_13()
            case 14:
                onze_a_vinte.exe1_14()
            case 15:
                onze_a_vinte.exe1_15()
            case 16:
                onze_a_vinte.exe1_16()
            case 17:
                onze_a_vinte.exe1_17()
            case 18:
                onze_a_vinte.exe1_18()

menu()



