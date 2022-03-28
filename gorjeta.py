import os
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
valor = str(input("Digite o valor da conta: "))
valor = valor.replace(",",".")  
while not isfloat(valor):
    valor = str(input("Digite o valor da conta: "))
    valor = valor.replace(",",".")  
valor = float(valor)
os.system('cls')
pessoas = int(input("Quantas pessoas no grupo: "))
os.system('cls')
gorjeta = int(input(f"Gorjeta sobre o valor [{valor}R$] 5% a 15%: "))
while gorjeta < 5 or gorjeta > 15:
    print("Porfavor digite um valor entre 5 e 15.")
    gorjeta = int(input(f"Gorjeta sobre o valor [{valor}R$] 5% a 15%: "))
os.system('cls')
tot_pessoa = valor / pessoas
f_tot_pessoa = "{:.2f}".format(tot_pessoa)
f_tot_pessoa = float(f_tot_pessoa)
por_gorjeta = gorjeta * 0.01
gorjeta_pessoa = f_tot_pessoa * por_gorjeta
f_gorjeta_pessoa = "{:.2f}".format(gorjeta_pessoa)
f_gorjeta_pessoa = float(f_gorjeta_pessoa)
tot_tudo = f_gorjeta_pessoa + f_tot_pessoa
print(f"O valor total da conta por pessoa é: {f_tot_pessoa}R$")
print(f"O total de gorjeta por pessoa é: {f_gorjeta_pessoa}R$")
print(f"Valor total com gorjeta por pessoa é: {tot_tudo}R$")