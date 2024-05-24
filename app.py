import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

from paginas import rede_propria_alunos as pra
from paginas import rede_propria_escolas as pre
from paginas import rede_propria_quadro_pessoal as prqp 
from paginas import rede_parceira_atendimento as paa
from paginas import educacao_infantil_alunos as eia
from paginas import educacao_infantil_escolas as eie


def obtem_conexao():
    conn = st.connection("postgresql")
    return conn

@st.cache_data
def busca_dados(tabela):
    conn = obtem_conexao()
    df = conn.query("select * from %s"%tabela)
    return df

st.set_page_config(page_title='Perfil de Atendimento - SMED - PBH', page_icon='static/favicon.png', layout="wide", initial_sidebar_state="auto", menu_items=None)

with st.sidebar:
    options = [
        "Rede Própria - Escolas",
        "Rede Própria - Alunos",
        "Rede Própria - Quadro Pessoal",
        "Rede Parceira - Atendimento",
        "Educação Infantil - Escolas",
        "Educação Infantil - Alunos"
    ]
    selected = option_menu("Menu Principal", options, 
        icons=['building', 'people-fill', 'person-vcard','mortarboard', 'buildings', 'people'], 
        menu_icon="house", 
        default_index=0)

if selected == "Rede Própria - Escolas":
    pre.rede_propria_escolas()    
elif selected == "Rede Própria - Alunos":
    pra.rede_propria_alunos()
elif selected == "Rede Própria - Quadro Pessoal":
    prqp.rede_propria_quadro_pessoal()
elif selected == "Rede Parceira - Atendimento":
    paa.rede_parceira_atendimento()
elif selected == "Educação Infantil - Escolas":
    eie.educacao_infantil_escolas()
elif selected == "Educação Infantil - Alunos":
    eia.educacao_infantil_alunos()



