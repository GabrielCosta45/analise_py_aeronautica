import pandas as pd
import streamlit as st
import plotly.express as px
from utils.preprocessing import carregar_dados

st.set_page_config(layout="wide")

st.title("📊 Dashboard Interativo: Total de ocorrências 2010 - 2021")

# Carregar Dados
df = carregar_dados("data/brazil_total_aeronautical_occurrences_2010_2021.csv")

# Converter coluna de data com dayfirst=True e tratar erros
df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], errors='coerce', dayfirst=True)
df['ano'] = df['ocorrencia_dia'].dt.year

# Remover linhas com data inválida
df = df.dropna(subset=['ano'])
df['ano'] = df['ano'].astype(int)

# Sidebar
st.sidebar.header("Início")
st.sidebar.success("Seu dashboard interativo para análise")

pagina = st.sidebar.selectbox(
    "Selecione uma página",
    ("Total de Ocorrências", "Ocorrências por Ano", "Ocorrências por Tipo", "Ocorrências por Aeronave"),
)

# Página: Total de Ocorrências
if pagina == "Total de Ocorrências":
    st.subheader('Análise temporal das Ocorrências no Brasil')
    st.write("Escrever a sua análise aqui...")

    def plot_total_ocorrencias(df):
        counts_ano = df.groupby('ano').size()
        fig = px.bar(counts_ano, x=counts_ano.index, y=counts_ano.values,
                     title='Total de Ocorrências por Ano',
                     labels={'x': 'Ano', 'y': 'Total de Ocorrências'})
        fig.update_layout(xaxis_title='Ano', yaxis_title='Total de Ocorrências')
        return fig

    fig = plot_total_ocorrencias(df)
    st.plotly_chart(fig, use_container_width=True)


# Página: Ocorrências por Tipo
elif pagina == "Ocorrências por Tipo":
    st.subheader('Análise temporal das Ocorrências no Brasil')
    st.write("Escrever a sua análise aqui...")

    def plot_ocorrencias_por_tipo(df):
        counts_tipo = df['tipo_ocorrencia'].value_counts()
        fig = px.bar(counts_tipo, x=counts_tipo.index, y=counts_tipo.values,
                     title='Total de Ocorrências por Tipo',
                     labels={'x': 'Tipo de Ocorrência', 'y': 'Total de Ocorrências'})
        fig.update_layout(xaxis_title='Tipo de Ocorrência', yaxis_title='Total de Ocorrências')
        return fig

    fig = plot_ocorrencias_por_tipo(df)
    st.plotly_chart(fig, use_container_width=True)