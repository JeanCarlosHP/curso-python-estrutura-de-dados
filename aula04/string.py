string = 'Jean Carlos'
numero_de_letras = 2

nova_string = '|'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])

print(string)
print(nova_string)
