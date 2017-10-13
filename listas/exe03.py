soma = 0
for nota in range(1, 5):
    valor_nota = int(input("Digite sua nota {}: ".format(nota)))
    soma += valor_nota

media = soma / 4
print("Media: {}".format(media))
