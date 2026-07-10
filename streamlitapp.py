import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.write("Hello, *World!* :sunglasses:")
st.write("Bootcamp de Analisys e Data de Dados")

df = pd.read_csv(r'Projeto Base\data\penguins.csv')

species = df['species'].unique()

species_selected = st.multiselect(
    "What are your favorite pinguin spicies?",
    species,
    default=species,
)

st.write("You selected:", species_selected)

df_filtrado = df[ df['species'].isin(species_selected) ]

if not pd.isnull(df_filtrado['body_mass_g'].mean()):
    media_massa = df_filtrado['body_mass_g'].mean().round(3)
    delta = round((df['body_mass_g'].mean() - media_massa) / df['body_mass_g'].mean() * 100, 2)
    st.metric(label="Média de Peso", value=f"{media_massa} g", delta=f"{delta} %")
else:
    media_massa = 0
    delta = 0
    st.metric(label="Média de Peso", value=f"{media_massa} g")
    

st.dataframe(df_filtrado)

grafico_on = st.toggle("Visualiza Gráfico de Barras?")

st.write(grafico_on)

if grafico_on:
    dfg = (
        df
        .groupby(['island', 'species'])
        ['body_mass_g'].mean()
        .reset_index()
        .round(2)
        .rename(columns={
            'island': 'Ilha'
            , 'species': 'Espécies'
            , 'body_mass_g': 'Massa (g)'
        })
    )

    fig = (
        px.bar(
            dfg
            , x="Ilha"
            , y="Massa (g)"
            , color='Espécies'
            , title="Peso Médio dos Pinguins por ilha"
            , barmode="group"
        )
    )


    st.plotly_chart(fig)

