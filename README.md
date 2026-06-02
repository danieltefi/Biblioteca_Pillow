# Mini Projeto Manipulação de Imagens com Pillow
> **Projeto FATEC - Apresentação da Biblioteca Pillow**

## Sobre o Projeto
Este projeto foi desenvolvido como material prático para uma apresentação de 5 minutos. O objetivo é demonstrar o poder e a simplicidade da biblioteca **Pillow (PIL)** para o processamento, manipulação e automação de operações em imagens utilizando Python. O sistema processa uma imagem original aplicando filtros de otimização, transformações geométricas e salvamento automatizado.

- **Atividade 1:** Abertura e validação de arquivos de imagem em formatos populares (JPG/PNG) tratando possíveis exceções de arquivo não encontrado.
- **Atividade 2:** Aplicação de filtros de processamento visual nativos (efeito de desfoque/Blur para simular efeitos de privacidade ou estética de plano de fundo).
- **Atividade 3:** Transformação geométrica da imagem através de rotação (90 graus) para demonstrar a manipulação de eixos e metadados de layout.
- **Atividade 4:** Criação de um pipeline automatizado que recebe uma imagem bruta e exporta a versão tratada de forma transparente e rápida.

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
- Garanta que possui uma imagem chamada foto_original.jpg na mesma pasta do script.

- python manipulador_imagem.py

## Estrutura de Arquivos
```
├── .venv/                   # Ambiente virtual isolado com a biblioteca Pillow instalada
├── .gitignore               # Define arquivos que o Git deve ignorar
├── foto_original.jpg        # Imagem de entrada utilizada como teste para a apresentação
├── foto_modificada.jpg      # Resultado final gerado pelo script após a aplicação dos filtros
├── manipulador_imagem.py    # Código-fonte principal contendo as instruções da biblioteca Pillow
├── README.md                # Documentação descritiva
└── requirements.txt         # Arquivo de dependências
```
---

### Status do Projeto:
*Em andamento*