string_um = input("Digite uma palavra ou frase: ")
string_dois = input("Digite uma outra palavra ou frase: ")

print("String 1: {}".format(string_um))
print("String 2: {}".format(string_um))
print("Tamanho de "'{}'": {} caracteres".format(string_um, len(string_um)))
print("Tamanho de "'{}'": {} caracteres".format(string_dois, len(string_dois)))

if len(string_um) == len(string_dois):
    print("As duas strings são do mesmo tamanho.")
    for posicao in range(len(string_um)):
        if string_um[posicao] != string_dois[posicao]:
            result = False
            break
        else:
            result = True

    if result:
        print("As duas strings possuem conteúdos iguais.")
    else:
        print("As duas strings possuem conteúdo diferente.")

else:
    print("As duas strings são de tamanhos diferentes.")
    print("As duas strings possuem conteúdo diferente.")
