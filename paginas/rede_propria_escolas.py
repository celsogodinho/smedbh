import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px


from helpers import busca_dados 

def rede_propria_escolas():
    st.header("Secretaria Municipal de Educação - PBH", divider='rainbow')
    st.subheader("Rede Própria - Escolas")

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Buscando dados do banco ...')
    # Load 10,000 rows of data into the dataframe.
    data = busca_dados('escola_sge')
    data_load_state.text('')

    total_escolas = data.shape[0]
    total_emefs = len(data[data.CATEGORIA == 'EMEF'])
    total_emeis = len(data[data.CATEGORIA == 'EMEI'])

    lin1col1, lin1col2, lin1col3 = st.columns(3)
    lin1col1.metric(label='Total de Escolas', value=total_escolas)
    lin1col2.metric(label='Total de EMEFs', value=total_emefs)
    lin1col3.metric(label='Total de EMEIs', value=total_emeis)
    style_metric_cards()

    df = data[["CATEGORIA", "REGIONAL", "ESCOLA"]].groupby(["CATEGORIA","REGIONAL"]).count().reset_index().rename(columns={"ESCOLA":"TOTAL"})
    fig1 = px.bar(df, x='REGIONAL', y='TOTAL', color='CATEGORIA', text='TOTAL', title="Total de escolas por regional e categoria")
    st.plotly_chart(fig1, use_container_width=True) 

    data_aluno = busca_dados('aluno_sge')
    df2 = data_aluno[["REGIONAL","ENSINO", "ESCOLA"]].groupby(["ENSINO","REGIONAL"]).nunique().reset_index().rename(columns={"ESCOLA":"TOTAL"})
    fig2 = px.bar(df2, x='REGIONAL', y='TOTAL', color='ENSINO', text='TOTAL', title="Total de escolas por regional e ensino")
    st.plotly_chart(fig2, use_container_width=True) 

    df3 = data_aluno[["REGIONAL","TURNO", "ESCOLA"]].groupby(["TURNO","REGIONAL"]).nunique().reset_index().rename(columns={"ESCOLA":"TOTAL"})
    fig3 = px.bar(df3, x='REGIONAL', y='TOTAL', color='TURNO', text='TOTAL',title="Total de escolas por regional e turno")
    st.plotly_chart(fig3, use_container_width=True) 

    rename = {
        "REGIONAL":"Regional", 
        "ESCOLA":"Escola", 
        "TELEFONE1":"Telefone 1", 
        "TELEFONE2":"telefone 2",
        "EMAIL":"E-mail"    
    }
    
    df=data[["REGIONAL", "ESCOLA", 	"TELEFONE1", "TELEFONE2", "EMAIL"]].rename(columns=rename)
    df.fillna('', inplace=True)
    st.write('Lista de Escolas')
    st.dataframe(df, hide_index=True, use_container_width=True)