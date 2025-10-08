

nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: R$ "))
horas_extras = int(input("Total de horas extras: "))
faltas = int(input("Total de faltas: "))
bonus_desempenho = input("Recebeu bônus por desempenho (s/n)? ").lower()


valor_hora_extra = salario_base * 0.015 * horas_extras
desconto_faltas = salario_base * 0.02 * faltas


bonus = 0
if bonus_desempenho == "s":
    if cargo == 1:
        bonus = 1000
    elif cargo == 2:
        bonus = 500
    elif cargo == 3:
        bonus = 300
    elif cargo == 4:
        bonus = 100
acrescimos = valor_hora_extra + bonus
descontos = desconto_faltas
salario_bruto = salario_base + acrescimos
salario_final = salario_bruto - descontos
print(f"\nFuncionário: {nome}")
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Acréscimos: R$ {acrescimos:.2f}")
print(f"Descontos: R$ {descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
