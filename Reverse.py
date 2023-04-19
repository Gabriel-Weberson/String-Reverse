palavra = str(input('Informe uma palavra para ver sua escrita invertida: '))
quantidadeLetras = len(palavra)
index = quantidadeLetras - 1

while (index) >= 0:
    print(palavra[index], end="")
    index = index - 1
