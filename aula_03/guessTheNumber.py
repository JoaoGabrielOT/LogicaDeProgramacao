import random

nomes = []
recorde = 101

while(True):
    numeroAlvo = random.randint(1, 100)
    numeroTentativas = 0
    tentativa = 0
    try:

        while (tentativa != numeroAlvo):
            tentativa = int(input("\nDigite um numero de 1 a 100: "))
            if tentativa > numeroAlvo:
                print("Muito alto, tente um mais baixo...\n")
                numeroTentativas += 1
            elif tentativa < numeroAlvo:
                print("Muito baixo, tente um mais alto...\n")
                numeroTentativas += 1
            elif tentativa == numeroAlvo:
                numeroTentativas += 1
                if recorde > numeroTentativas:
                    recorde = numeroTentativas
                print(f"\nAcertou o numero.\nQauntidade de tentativas: {numeroTentativas}\nSeu recorde é: {recorde}")
    except:
        print("error")
    
    