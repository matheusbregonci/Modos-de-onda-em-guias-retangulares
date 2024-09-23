# Simulação de Campos em Guias Retangulares

Este projeto é uma aplicação web construída com Streamlit que permite simular campos elétricos e magnéticos em guias de onda retangulares. Utiliza modelos para calcular modos transversais elétricos (TE) e magnéticos (TM).

## Funcionalidades

- Entrada de parâmetros da guia (largura, altura).
- Definição de parâmetros da onda (frequência).
- Definição de propriedades do meio (permissividade e permeabilidade).
- Escolha do plano (xy, xz, yz) e do componente do campo (elétrico ou magnético).
- Plotagem dos campos em 3D.

## Tecnologias Usadas

- [Streamlit](https://streamlit.io/) - Framework para criação de aplicações web interativas.
- [Python](https://www.python.org/) - Linguagem de programação usada para desenvolvimento.
- Modelos `Modo_TEmn` e `Modo_TMmn` - Implementações personalizadas para calcular os campos.

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/matheusbregonci/Modos-de-onda-em-guias-retangulares
   cd seurepositorio

2. **Instale as dependências.**:
  python -m venv env
  source env/bin/activate  # Para Linux/Mac
  env\Scripts\activate     # Para Windows
  pip install streamlit
  streamlit run app_streamlit.py

