A = float(input("\nDigite um numero\n"))
B = float(input("\nDigite outro numero\n"))



if(A>B):
    A-=B
elif(B>A):
    B-=A
else:
    print("\nOs números são iguais, não há diferença para calcular.")


print(f"\nPrimeiro numero: {A}\nSegundo numero: {B}")