import streamlit as st
from helpers import busca_dados 

def rede_propria_alunos():
    st.header("Secretaria Municipal de Educação - PBH", divider='rainbow')
    st.subheader("Rede Própria - Alunos")

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Buscando dados do banco ...')
    # Load 10,000 rows of data into the dataframe.
    data = busca_dados('escola_sge')
    data_load_state.text('')
    st.dataframe(data)


