###################################################################################################################
#importação das bibliotecas utilizadas
import streamlit as st
    
###################################################################################################################
#configuração do nome da aba e cabeçalhos do app

st.set_page_config(
    page_title='Orbe.ai Escola',
    page_icon='📖')

st.title('📖 Orbe.ai Escola')

###################################################################################################################

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Escolha o curso",
        ("Canis Minor", "Canis Major", "Órion", "Kósmos")
    )

if add_radio=="Canis Minor":
    with st.expander('Canis Minor'):
        st.header("FUNDAMENTAL 01")
        st.write("Este é o nosso curso de introdução à Inteligência Artificial, no qual você vai entender contexto e cenário da IA e como ela está sendo aplicada nas empresas. Vamos compreender a anatomia de um projeto de ciência de dados e a importância do cientista de dados. O aluno vai aprender a coletar, limpar, preparar e analisar os dados, além de elaborar gráficos. Vamos ver três tipos de algoritmo de machine learning e construir um projeto de ciência de dados do início ao fim.")
if add_radio=="Canis Major":
    with st.expander('Canis Major'):
        st.header("FUNDAMENTAL 02")
        st.write("Você vai aprender como construir storytelling com dados, entender o que é API e aprender como construir e publicar a sua, construir um site com uma solução de IA desenvolvida por você, explorar o machine learning com mais profundidade e entrar no conceito de deep learning com VC (visão computacional), ou seja, IA aplicada a imagens como reconhecimento facial, carros autônomos e assim por diante.")
if add_radio=="Órion":
    with st.expander('Órion'):
        st.header("FUNDAMENTAL 03")
        st.write("No último módulo do curso fundamental vamos ver como aplicar a IA aos negócios, entrar em algoritmos mais avançados de deep learning e entrar em visão computacional, que é a aplicação de IA em fotos e vídeos. Encerramos o módulo construindo um mini carro autônomo, a partir de conceitos de Internet das Coisas.")
if add_radio=="Kósmos":
    with st.expander('Kósmos'):
        st.header("AI PARA GESTORES")
        st.write("Esse módulo é voltado para gestores, coordenadores, product owners / managers, para trazer ordem ao kháos de informação que é o mundo da inteligência artificial.")
