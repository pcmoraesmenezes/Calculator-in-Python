i = 0
cont = 0
var1 = 0.0
var2 = 0
numero = 0
numero2 = 0
while True:
    print ("Bem vindo a central da calculadora")
    print("Se deseja realizar uma soma pressione 1")
    print("Caso deseje realizar uma subtração pressione 2")
    print("Caso deseje realizar uma multiplicação pressione 3")
    print("Caso deseje realizar uma divisão pressione 4")
    print("Caso deseje sair da calculadora pressione a tecla 5!")
    cont = int(input())
    while cont != 1 and cont != 2 and cont!=3 and cont!=4 and cont!=5:
        print("Você não informou uma opção valida! Tente novamente")
        cont = int(input())
    if cont == 1:
        print("Você optou pela soma!")
        print("Informe o primeiro numero!")
        var1 = (input())
        print("Informe o segundo numero")
        var2 = input()
        try:
            numero = float(var1)
            numero2 = float(var2)
            print("-----------------------------")
            print(f'{numero} + {numero2} = {numero + numero2}')
            print("-----------------------------")
            continue
        except:
            continue
    if cont == 2:
        print("Você optou pela subtração")
        print("Informe o primeiro numero!")
        var1 = (input())
        print("Informe o segundo numero")
        var2 = input()
        try:
            numero = float(var1)
            numero2 = float(var2)
            print("-----------------------------")
            print(f'{numero} - {numero2} = {numero - numero2}')
            print("-----------------------------")
            continue
        except:
            continue
    if cont == 3:
        print("Você optou pela multiplicação!!!")
        print("Informe o primeiro numero!")
        var1 = (input())
        print("Informe o segundo numero")
        var2 = input()
        try:
            numero = float(var1)
            numero2 = float(var2)
            print("-----------------------------")
            print(f'{numero} * {numero2} = {numero * numero2}')
            print("-----------------------------")
            continue
        except:
            continue
    if cont == 4:
        print("Você optou pela divisão!!!")
        print("Informe o primeiro numero!")
        var1 = (input())
        print("Informe o segundo numero")
        var2 = input()
        try:
            numero = float(var1)
            numero2 = float(var2)
            print("-----------------------------")
            print(f'{numero} / {numero2} = {numero / numero2}')
            print("-----------------------------")
            continue
        except:
            continue
    if cont == 5:
        break




        


