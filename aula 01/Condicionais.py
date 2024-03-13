#testando if, else if, e else
numero = int(input("Digite um número: "))
#tive que usar cast int pq estava considerando como string
if numero > 5:
    print("Número é maior que 5.")
elif numero == 5:
    print("Número é igual a 5.")
else:
    print("número é menor que 5.")