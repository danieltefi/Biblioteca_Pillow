from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ExifTags

# atividade 1: filtro blur e preto e branco

imagem_foto1 = Image.open('foto1.jpg') # abre a foto

imagem_pb = imagem_foto1.convert('L') # deixa a imagem em preto e branco (modo 'L' significa ganho de cinza)
imagem_pb.save('resultado_pb.jpg')
print('Imagem em preto e branco criada.')

imagem_blur = imagem_foto1.filter(ImageFilter.BLUR) # aplica o desfoque (blur) na foto
imagem_blur.save('resultado_blur.jpg')
print('Imagem com blur criada.')

# atividade 2: aplicaçãod e marca d'água (texto na imagem)
imagem_foto2 = Image.open('foto2.jpg') # abre a foto

desenhar = ImageDraw.Draw(imagem_foto2) # cria uma ferramenta para desenhar em cima da imagem

desenhar.text((50, 50), 'PROPRIEDADE DA FATEC RC', fill='white') # escreve o texto na posição X=50, Y=50, na cor branca

imagem_foto2.save('resultado_marca_dagua.jpg') # salva o resultado
print('Marca d água adicionada com sucesso.')

# atividade 3: criação de gif animado

img1 = Image.open('frame1.jpg') # abre as 3 imagens da animação
img2 = Image.open('frame2.jpg')
img3 = Image.open('frame3.jpg')

img1.save( # salva a primeira imagem e "engata" as outras duas logo atrás para criar o GIF
    "animacao.gif", 
    save_all=True, 
    append_images=[img2, img3], 
    duration=500,  # tempo de cada foto na tela (500 milissegundos = 0.5 segundos)
    loop=0         # 0 significa que o GIF vai ficar rodando para sempre em loop
)
print('GIF animado gerado com sucesso.')

# atividade 4: conversão em lote (muda formato de várias fotos)

lista_de_fotos = ["fotoA.png", "fotoB.png", "fotoC.png"] # lista com o nome das fotos em formato .png que queremos converter para .jpg

for nome_da_foto in lista_de_fotos: # para cada foto dentro da lista...
    imagem_png = Image.open(nome_da_foto)
    
    novo_nome = nome_da_foto.replace('.png', '.jpg') # remove o ".png" do nome antigo e troca por ".jpg"
    
    imagem_png.save(novo_nome) # salva no novo formato
    print(f'Convertido de {nome_da_foto} para {novo_nome}')

# atividade 5: leitura de metadados ocultos (EXIF data)

imagem_celular = Image.open('foto_celular.jpg') # abre a foto tirada por celular (com dados reais)

dados_ocultos = imagem_celular.getexif() # extrai os dados ocultos (EXIF) da imagem

print('\n--- Atividade 5: Lendo dados ocultos da imagem ---')

for codigo, valor in dados_ocultos.items(): # varre os dados, mostra os códigos numéricos e respectivos valores
                                            # exemplos de códigos comuns: 271 (marca do celular), 272 (modelo do celular)
    
    nome_tag = ExifTags.TAGS.get(codigo, codigo) # traduz o código numérico para um nome legível (ex: 271 vira 'Make', 306 vira 'DateTime')
    
    print(f'Código do metadado: {nome_tag} -> Informação: {valor}')