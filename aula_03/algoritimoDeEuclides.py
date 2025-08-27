A = int(input("\nDigite um numero\n"))
B = int(input("\nDigite outro numero\n"))


while (A != B):
    if(A>B):
        A-=B
    elif(B>A):
        B-=A


print(f"\nPrimeiro numero: {A}\nSegundo numero: {B}")

#