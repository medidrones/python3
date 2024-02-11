# os.listdir para navegar em caminhos
# /Users/jorge/Pictures/EXEMPLO => Caminho no Linux e MAC
# C:\Users\jorge\Pictures\EXEMPLO => Caminho no Windows
# caminho = r'C:\\Users\\jorge\\Pictures\\EXEMPLO'
import os

caminho = os.path.join('/Users', 'jorge', 'Pictures', 'EXEMPLO')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)