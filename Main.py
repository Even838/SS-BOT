import os

# Mensagem inicial
print("OI SOU A SS")

# Captura a entrada do usuário (não usada no exemplo, mas pode ser útil para expandir a funcionalidade)
mem = input("")

print("Pode fazer um favor?")
mem1 = input("")

# Texto a ser escrito no arquivo
texto = "SOS"

# Nome do arquivo
nome_arquivo = 'mensagem.txt'

# Abre o arquivo para escrita ('w' significa que será escrito e o arquivo será criado se não existir)
with open(nome_arquivo, 'w') as arquivo:
    # Escreve o texto no arquivo
    arquivo.write(texto)

print(f"Veja o texto na sua área de trabalho em {nome_arquivo}")
