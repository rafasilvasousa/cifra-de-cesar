chave = 7
CARACTERES='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encriptar(texto):
    convertido=''
    for caracter in texto:
        if caracter in CARACTERES:
            num = CARACTERES.find(caracter)
            num = num +chave
            if num>=len(CARACTERES):
                num = num-len(CARACTERES)
            elif num<0:
                num = num+len(CARACTERES)
            
            convertido=convertido+CARACTERES[num]
        else:
            convertido=convertido+caracter
    return convertido


def desencriptar(texto):
    convertido=''
    for caracter in texto:
        if caracter in CARACTERES:
            num = CARACTERES.find(caracter)
            num = num - chave
            if num>=len(CARACTERES):
                num = num-len(CARACTERES)
            elif num<0:
                num = num+len(CARACTERES)
            
            convertido =convertido+CARACTERES[num]
        else:
            convertido=convertido+caracter
    return convertido


print("ALGORITMO SIMULANDO CIFRA DE CESAR")
print("Escolha a Opção.")
print("1. ENCRIPTAR")
print("2. DECRIPTAR")
opcao1 = int(input())
if opcao1==1:#ENCRIPTAR
    print("Escolha a Opção.")
    print("1. Texto Digitado")
    print("2. Arquivo")
    opcao = int(input())
    if opcao==1:
        print ('Digite o texto Desejado') 
        texto=input()
        texto = texto.upper()
        print(encriptar(texto))
    elif opcao==2:
        texto = open("texto").read()
        texto = texto.upper()
        print(encriptar(texto))
    else:
        print('Opção inválida')
elif opcao1==2: #DECRIPTAR
    print("Escolha a Opção.")
    print("1. Texto Digitado")
    print("2. Arquivo")
    opcao = int(input())
    if opcao==1:
        print ('Digite o texto Desejado') 
        texto=input()
        texto = texto.upper()
        print(desencriptar(texto))
    elif opcao==2:
        texto = open("textoencrip").read()
        texto = texto.upper()
        print(desencriptar(texto))
    else:
        print('Opção inválida')
else:
    print('Opção inválida')
