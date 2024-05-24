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

    # Filtros
    fil1, fil2, fil3, fil4, fil5, fil6 = st.columns(6)
    with fil1:
        fil_regional = st.selectbox(
            "",
            ("DIRE-B", "DIRE-CS", "DIRE-L", "DIRE-N", "DIRE-NE", "DIRE-NO", "DIRE-O", "DIRE-P", "DIRE-VN"),
            index=None,
            placeholder="Regional",            
        )

    with fil2:
        fil_categoria = st.selectbox(
            "",
            ("EMEI", "EMEF"),
            index=None,
            placeholder="Categoria",            
        )

    total_escolas = data.shape[0]
    total_emefs = len(data[data.CATEGORIA == 'EMEF'])
    total_emeis = len(data[data.CATEGORIA == 'EMEI'])

    lin1col1, lin1col2, lin1col3 = st.columns(3)
    lin1col1.metric(label='Total de Escolas', value=total_escolas)
    lin1col2.metric(label='Total de EMEFs', value=total_emefs)
    lin1col3.metric(label='Total de EMEIs', value=total_emeis)
    style_metric_cards()

    lin2col1, lin2col2 = st.columns(2)

    df = data[["CATEGORIA", "REGIONAL", "ESCOLA"]].groupby(["CATEGORIA","REGIONAL"]).count().reset_index().rename(columns={"ESCOLA":"TOTAL"})
    fig1 = px.bar(df, x='REGIONAL', y='TOTAL', color='CATEGORIA', text='TOTAL')
    lin2col1.plotly_chart(fig1) 
