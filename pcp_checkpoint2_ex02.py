

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))


lados = sorted([a, b, c], reverse=True)
A, B, C = lados

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")
elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")
    if A == B == C:
print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
print("TRIANGULO ISOSCELES")
