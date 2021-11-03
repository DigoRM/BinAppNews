import pandas as pd
import numpy as np
import requests
import streamlit as st

# Title of the app
st.set_page_config(page_title="BiNewsApp", page_icon=":bar_chart:", layout="wide")
st.title('Binance News App')

link = "https://api2.binance.com/api/v3/ticker/24hr"
requisicao = requests.get(link)
dic_requisicao = requisicao.json()
cotacao = dic_requisicao
data_df = pd.DataFrame(cotacao)
#data_df = data_df[data_df['symbol'] == "ADABRL"]
data_df['valor_em']=data_df['symbol'].str[3:]
data_df['COIN']=data_df['symbol'].str[:3]

st.header('Top 10 variação POSITIVA')

variacao_positiva = data_df.sort_values('priceChangePercent',ascending=False)
variacao_positiva = variacao_positiva.head(10)
variacao_positiva

st.header('Top 10 variação NEGATIVA')

variacao_negativa = data_df.sort_values('priceChangePercent',ascending=True)
variacao_negativa = variacao_negativa.head(10)
variacao_negativa


# Filter in SideBar
moeda1 = st.sidebar.multiselect ("Valor em", options=data_df['valor_em'].unique())
# Resultado da Query
st.header('Lista 1:')
df_selection_operador = data_df.query("valor_em == @moeda1")
st.dataframe(df_selection_operador)

# Filter in SideBar
moeda2 = st.sidebar.multiselect ("Selecione Moedas para análises", options=data_df['COIN'].unique(),default=df_selection_operador['COIN'])
# Resultado da Query
st.header('Lista 2')
df_selection_operador1 = df_selection_operador.query("COIN == @moeda2")
st.dataframe(df_selection_operador1)

st.header('Top 10 variação POSITIVA')

variacao_positiva = df_selection_operador1.sort_values('priceChangePercent',ascending=False)
variacao_positiva = variacao_positiva.head(10)
variacao_positiva

st.header('Top 10 variação NEGATIVA')

variacao_negativa = df_selection_operador1.sort_values('priceChangePercent',ascending=True)
variacao_negativa = variacao_negativa.head(10)
variacao_negativa