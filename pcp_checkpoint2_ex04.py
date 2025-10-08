
nome = input("Nome do cliente: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: R$ "))
valor_emprestimo = float(input("Valor desejado do empréstimo: R$ "))
parcelas = int(input("Número de parcelas (3 a 24): "))
if idade < 18:
    print("Empréstimo negado: menor de idade.")
    exit()
if valor_emprestimo > renda * 15:
    print("Empréstimo negado: valor excede 15x a renda.")
    exit()
if parcelas < 3 or parcelas > 24:
    print("Empréstimo negado: número de parcelas inválido.")
    exit()


if parcelas <= 6:
    taxa = 0.05
elif parcelas <= 12:
    taxa = 0.08
else:
    taxa = 0.10
valor_total = valor_emprestimo * ((1 + taxa) ** parcelas)
valor_parcela = valor_total / parcelas
juros_totais = valor_total - valor_emprestimo

if 100 <= valor_parcela <= 2000:
    print(f"\nEmpréstimo aprovado para {nome}!")
    print(f"Valor total com juros: R$ {valor_total:.2f}")
    print(f"Valor de cada parcela ({parcelas}x): R$ {valor_parcela:.2f}")
    print(f"Juros totais pagos: R$ {juros_totais:.2f}")
else:
    print("Empréstimo negado: valor das parcelas fora do limite permitido.")
