import random

nomes = []
recordes = []

while(True):
    jogador = input("Digite seu nome: ")
    if jogador not in nomes:
        nomes.append(jogador)
        recordes.append(101)
    
    index = nomes.index(jogador)

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
                numeroTentativas += 1
                if recordes[index] > numeroTentativas:
                    recordes[index] = numeroTentativas

                numerosTestados = list(set(numerosTestados))
                numerosTestados.sort()

                print(f"""Acertou o numero.
                      Qauntidade de tentativas: {numeroTentativas}
                      Seu recorde é: {recordes[index]}
                      Numeros usados até acertar: {numerosTestados}
                      """)

            numerosTestados.append(tentativa)
    except:
        print("error")
     
    