import streamlit as st
###################################################################################################################
#configuração do nome da aba e cabeçalhos do app

st.set_page_config(
    page_title='Orbe.ai Dimension',
    page_icon='🤖')

st.title('🤖 Orbe.ai Dimension')

with st.expander("Sobre o App"):
  st.markdown('''
  Este aplicativo é a plataforma de modelos da Orbe.ai, a escola infinita de inteligência articial.
  https://orbe.ai
  ''')
