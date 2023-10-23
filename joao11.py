# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
distanciakm = float(input(" digite distancia em km: "))
if distanciakm <= 200 or distanciakm >= 2000:
    print(("o preço da passagem será"), distanciakm * 0.50)
else:
    print(( " o preço da passagem será"), distanciakm * 0.45)
    