notasEMoedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

valorAReceber = float(input("""
Qual o valor a receber?
                            
R:"""))
#1700

valorRecebido = float(input("""
Qual o valor recebido?
                            
R:"""))
#2000

diferenca = valorRecebido - valorAReceber

print(f"\nTroco:")
for item in notasEMoedas:
    quantidadeDeItens = 0
    while item <= diferenca:
        quantidadeDeItens += 1
        diferenca -= item

    if quantidadeDeItens > 0:
        print(f"""{quantidadeDeItens} nota(s) de: {item}""")