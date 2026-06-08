from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ExifTags
from pillow_heif import register_heif_opener
from PIL import ImageFont

register_heif_opener() # biblioteca lê arquivos heic (necessário para a atividade 5)

# atividade 1: filtro blur e preto e branco

imagem_foto1 = Image.open('originais/foto1.jpg') # abre a foto

imagem_pb = imagem_foto1.convert('L') # deixa a imagem em preto e branco (modo 'L' significa ganho de cinza)
imagem_pb.save('modificadas/resultado_pb.jpg')
print('Imagem em preto e branco criada.')

imagem_blur = imagem_foto1.filter(ImageFilter.GaussianBlur(radius=20)) # aplica o desfoque (blur) na foto
imagem_blur.save('modificadas/resultado_blur.jpg')
print('Imagem com blur criada.')

# atividade 2: aplicaçãod e marca d'água (texto na imagem)
imagem_foto2 = Image.open('originais/foto2.jpg') # abre a foto

desenhar = ImageDraw.Draw(imagem_foto2) # cria uma ferramenta para desenhar em cima da imagem

try: # carrega a fonte arial no tamanho 30
    fonte = ImageFont.truetype("arial.ttf", 30)
except IOError:
    fonte = ImageFont.load_default() # caso não ache a arial, usa a padrão

desenhar.text((50, 50), 'PROPRIEDADE DA FATEC RC', fill='white', font=fonte) # escreve o texto na posição X=50, Y=50, na cor branca

imagem_foto2.save('modificadas/resultado_marca_dagua.jpg') # salva o resultado
print('Marca d água adicionada com sucesso.')

# atividade 3: criação de gif animado

img1 = Image.open('originais/frame1.png') # abre as 3 imagens da animação
img2 = Image.open('originais/frame2.png')
img3 = Image.open('originais/frame3.png')

img1.save( # salva a primeira imagem e "engata" as outras duas logo atrás para criar o GIF
    'modificadas/animacao.gif', 
    save_all=True, 
    append_images=[img2, img3], 
    duration=500,  # tempo de cada foto na tela (500 milissegundos = 0.5 segundos)
    loop=0         # 0 significa que o GIF vai ficar rodando para sempre em loop
)
print('GIF animado gerado com sucesso.')

# atividade 4: conversão em lote (muda formato de várias fotos)

lista_de_fotos = ['originais/fotoA.png', 'originais/fotoB.png', 'originais/fotoC.png'] # lista com o nome das fotos em formato .png que queremos converter para .jpg

for nome_da_foto in lista_de_fotos: # para cada foto dentro da lista...
    imagem_png = Image.open(nome_da_foto)

    imagem_png = imagem_png.convert('RGB') # transforma a imagem para o modo RGB (resolve o erro 'mode P')
    
    novo_nome = nome_da_foto.replace('.png', '.jpg') # remove o ".png" do nome antigo e troca por ".jpg"
    
    novo_nome = novo_nome.replace('originais/', 'modificadas/') # troca a pasta originais para modificadas para salvamento no local correto

    imagem_png.save(novo_nome) # salva no novo formato
    print(f'Convertido de {nome_da_foto} para {novo_nome}')

# atividade 5: leitura de metadados ocultos (EXIF data)

imagem_celular = Image.open('originais/foto_celular.heic') # abre a foto tirada por celular (com dados reais)

dados_ocultos = imagem_celular.getexif() # extrai os dados ocultos (EXIF) da imagem

print('\n--- Atividade 5: Lendo dados ocultos da imagem ---')

for codigo, valor in dados_ocultos.items(): # varre os dados, mostra os códigos numéricos e respectivos valores
                                            # exemplos de códigos comuns: 271 (marca do celular), 272 (modelo do celular)
    
    nome_tag = ExifTags.TAGS.get(codigo, codigo) # traduz o código numérico para um nome legível (ex: 271 vira 'Make', 306 vira 'DateTime')
    
    print(f'Código do metadado: {nome_tag} -> Informação: {valor}')