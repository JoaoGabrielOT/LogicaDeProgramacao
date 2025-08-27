import random

nomes = []
recorde = 101

while(True):
    numeroAlvo = random.randint(1, 100)
    numeroTentativas = 0
    tentativa = 0
    numerosTestados = []
    try:

        while (tentativa != numeroAlvo):
            tentativa = int(input("\nDigite um numero de 1 a 100: "))
            if tentativa > 100 or tentativa < 1:
                print("Valor invalido...\n")
                
            elif tentativa in numerosTestados:
                print(f"Você ja tentou o numero {tentativa}, tente outro numero...\n")
                
            elif tentativa > numeroAlvo:
                print("Muito alto, tente um mais baixo...\n")
                numeroTentativas += 1
                
            elif tentativa < numeroAlvo:
                print("Muito baixo, tente um mais alto...\n")
                numeroTentativas += 1

            else:
                if recorde > numeroTentativas:
                    recorde = numeroTentativas

                numeroTentativas += 1
                numerosTestados = list(set(numerosTestados))
                numerosTestados.sort()

                print(f"\nAcertou o numero.\nQauntidade de tentativas: {numeroTentativas}\nSeu recorde é: {recorde}\nNumeros usados até acertar: {numerosTestados}")
                
            numerosTestados.append(tentativa)
    except:
        print("error")
     
    