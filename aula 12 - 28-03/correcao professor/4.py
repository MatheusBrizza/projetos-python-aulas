#4Subconjuntos:
#Crie um conjunto com os países da América do Sul e outro com os países que você já visitou.
#Verifique se o conjunto dos países que você já visitou é um subconjunto do conjunto dos países da América do Sul.


paises_america_sul = {"Brasil", "Argentina", "Uruguai", "Chile", "Paraguai"}
paises_visitados = {"Brasil", "Argentina"}

if paises_visitados <= paises_america_sul:
  print("Você já visitou todos os países da América do Sul que estão no conjunto.")
else:
  print("Você ainda não visitou todos os países da América do Sul que estão no conjunto.")
