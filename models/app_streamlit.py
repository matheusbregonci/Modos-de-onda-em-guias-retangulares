import streamlit as st
from TEmn_model import Modo_TEmn
from TMmn_model import Modo_TMmn


@st.cache_resource
def get_state():
    return {}
state = get_state()
# # Recuperar o estado persistente
# state = get_state()
# if 'navio' not in state:
#     # Se o objeto não estiver presente, inicialize-o
#     state['navio'] = Navio()


def input_dados():
    # Título da aplicação
    st.title("Modelo de simulação para campos em Guias retangulares")

    # Parâmetros da guia
    largura_guia = st.number_input("Largura da Guia (mm)", value=22.86, step=0.1)
    altura_guia = st.number_input("Altura da Guia (mm)", value=10.16, step=0.1)

    # Parâmetros da onda
    frequencia_onda = st.number_input("Frequência da Onda (GHz)", value=12.0, step=0.1)

    # Parâmetros do meio
    permissividade_meio = st.number_input("Permissividade do Meio", value=1.0, step=0.1)
    permeabilidade_meio = st.number_input("Permeabilidade do Meio", value=1.0, step=0.1)

    # Escolha do plano
    plano_opcoes = ['xy', 'xz', 'yz']
    plano = st.selectbox("Plano", plano_opcoes)

    campo = st.selectbox("Campo", ["eletrico", "magnetico"])
    componente = st.selectbox("Componente", ['x', 'y', 'z'])

    state['campo_componente'] = [campo,componente]

    # Botão para aplicar os parâmetros e continuar
    if st.button("Aplicar Parâmetros"):
        # Substituir esses parâmetros em um objeto ou executar qualquer lógica necessária
        objeto_simulacao = {
            'largura_guia': largura_guia,
            'altura_guia': altura_guia,
            'frequencia_onda': frequencia_onda,
            'permissividade_meio': permissividade_meio,
            'permeabilidade_meio': permeabilidade_meio,
            'plano': plano
        }
        TEmn = Modo_TEmn(largura = largura_guia, 
                 altura = altura_guia, 
                 frequencia = frequencia_onda, 
                 permissividade = permissividade_meio, 
                 permeabilidade = permeabilidade_meio, 
                 plano = plano)
        TEmn.calcula_campos()
        state['TEmn'] = TEmn

    if st.button("Plotar Campo 3D"):
        TEmn = state['TEmn']
        campo, componente = state['campo_componente']
        plot = TEmn.plot3DField(campo = campo, componente = componente)
        st.pyplot(plot)

# def plot_campo():

# def main():
#     # st.sidebar.title('Plano de Carregamento Automatizado')
#     opcoes_abas = ["Parâmetros"]

#     aba_selecionada = st.sidebar.radio("Abas", opcoes_abas)
#     if aba_selecionada == "Parâmetros":
#         input_dados()
    # elif aba_selecionada == "Plot do campo":
    #     plot_campo()
# Executa a função principal
if __name__ == "__main__":
    input_dados()