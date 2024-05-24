import streamlit as st
import pandas as pd

def obtem_conexao():
    conn = st.connection("postgresql")
    return conn

@st.cache_data
def busca_dados(tabela):
    conn = obtem_conexao()
    df = conn.query("select * from %s"%tabela)
    return df
