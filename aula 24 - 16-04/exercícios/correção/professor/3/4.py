import random

# Definindo as cartas e seus valores
cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
valores = {carta: i + 1 for i, carta in enumerate(cartas)}  # Dicionário com valores numéricos

# Função para embaralhar as cartas
def embaralhar(cartas):
  random.shuffle(cartas)

# Função para distribuir cartas para os jogadores
def distribuir_cartas(cartas, jogadores, numero_cartas_por_jogador):
  for jogador in jogadores:
    jogador["cartas"] = []
    for _ in range(numero_cartas_por_jogador):
      jogador["cartas"].append(cartas.pop())

# Função para mostrar as cartas de um jogador
def mostrar_cartas(jogador):
  print(f"Cartas de {jogador['nome']}:")
  for carta in jogador["cartas"]:
    print(carta)

# Função para comparar cartas
def comparar_cartas(carta1, carta2):
  return valores[carta1] - valores[carta2]

# Função para iniciar o jogo
def iniciar_jogo():
  # Criando jogadores e definindo o número de cartas por jogador
  jogadores = [{"nome": "Jogador 1"}, {"nome": "Jogador 2"}]
  numero_cartas_por_jogador = 2

  # Embaralhando as cartas
  embaralhar(cartas)

  # Distribuindo cartas para os jogadores
  distribuir_cartas(cartas, jogadores, numero_cartas_por_jogador)

  # Mostrar as cartas dos jogadores
  for jogador in jogadores:
    mostrar_cartas(jogador)

  # Jogada 1: Comparar cartas
  carta_jogador1 = jogadores[0]["cartas"][0]
  carta_jogador2 = jogadores[1]["cartas"][0]

  vencedor_jogada1 = comparar_cartas(carta_jogador1, carta_jogador2)
  if vencedor_jogada1 > 0:
    print(f"{jogadores[0]['nome']} vence a primeira jogada com {carta_jogador1}!")
  elif vencedor_jogada1 < 0:
    print(f"{jogadores[1]['nome']} vence a primeira jogada com {carta_jogador2}!")
  else:
    print("Empate na primeira jogada!")


iniciar_jogo()
