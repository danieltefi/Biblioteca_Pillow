# Mini Projeto Manipulação de Imagens com Pillow
> **Projeto FATEC - Apresentação da Biblioteca Pillow**

## Sobre o Projeto
Este projeto foi desenvolvido como material prático para uma apresentação de 5 minutos. O objetivo é demonstrar o poder e a simplicidade da biblioteca **Pillow (PIL)** para o processamento, manipulação e automação de operações em imagens utilizando Python. O sistema aborda desde o tratamento de filtros básicos até automação em lote e análise de metadados de arquivos.

- **Atividade 1:** Processamento visual básico através da conversão de uma imagem para tons de cinza (Preto e Branco) e aplicação de filtro nativo de desfoque (Blur).
- **Atividade 2:** Manipulação de camadas visuais com a aplicação automatizada de marca d'água textual sobreposta à imagem em coordenadas específicas.
- **Atividade 3:** Criação de arquivos de mídia dinâmicos através da junção sequencial de frames estáticos para a geração de um GIF animado.
- **Atividade 4:** Automação em lote utilizando estruturas de repetição para abrir, converter o formato interno (PNG para JPG) e salvar múltiplos arquivos simultaneamente.
- **Atividade 5:** Extração e decodificação de metadados ocultos (dados EXIF) para leitura de informações estruturais do arquivo, como o modelo do dispositivo e data/hora da captura.

## Tecnologias
- **Linguagem:** Python 3
- **Bibliotecas:** Pillow (PIL - Python Imaging Library)
- **Saída:** Arquivos de imagem processados (JPG/PNG).

## Configuração do ambiente
O projeto utiliza **ambiente virtual (venv)** para isolamento de dependências.

### Instalação:
1. **Criar o Ambiente Virtual:**
   O ambiente virtual isola as bibliotecas do projeto:
   python -m venv .venv

2. **Ative o ambiente:**
   - Windows (PowerShell): .\.venv\Scripts\Activate.ps1
   - Windows (CMD): .\.venv\Scripts\activate.bat
   - Linux/macOS: source .venv/bin/activate

3. **Dependências:**
   pip install -r requirements.txt

### Execução:
Garanta que possui todos os arquivos de imagem de teste listados na estrutura abaixo dentro da mesma pasta do script.

- python manipulador_imagem.py

## Estrutura de Arquivos
## Estrutura de Arquivos
```text
├── .venv/                  # Ambiente virtual isolado com as bibliotecas instaladas
├── .gitignore              # Define arquivos que o Git deve ignorar
├── manipulador_imagem.py   # Código-fonte principal contendo as instruções da biblioteca Pillow
├── README.md               # Documentação descritiva do projeto
├── requirements.txt        # Arquivo de dependências (Pillow e pillow-heif)
├── originais/              # PASTA DE ENTRADA: Imagens brutas para os testes
│   ├── foto1.jpg           # Utilizada para o filtro Blur e Preto e Branco (atividade 1)
│   ├── foto2.jpg           # Utilizada para receber a marca d'água (atividade 2)
│   ├── frame1.png          # Frame 1 para a composição do GIF (atividade 3)
│   ├── frame2.png          # Frame 2 para a composição do GIF (atividade 3)
│   ├── frame3.png          # Frame 3 para a composição do GIF (atividade 3)
│   ├── fotoA.png           # Imagem A para conversão em lote (atividade 4)
│   ├── fotoB.png           # Imagem B para conversão em lote (atividade 4)
│   ├── fotoC.png           # Imagem C para conversão em lote (atividade 4)
│   └── foto_celular.heic   # Foto original do celular com metadados (atividade 5)
└── modificadas/            # Pasta de sáida: Onde os resultados são salvos automaticamente
    ├── resultado_pb.jpg
    ├── resultado_blur.jpg
    ├── resultado_marca_dagua.jpg
    ├── animacao.gif
    ├── fotoA.jpg
    ├── fotoB.jpg
    └── fotoC.jpg
```
---

### Status do Projeto:
*Concluído*