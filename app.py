import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def load_data():
    data = pd.read_csv(
        "./data/micro_world.csv",
        encoding='latin-1'
    )
    return data

df = pd.read_csv("./data/micro_world.csv",encoding="latin1", engine="python")

st.title("Hello world!") 

fig = sns.histplot(data=df, x='age', bins=30, kde=True)
plt.title('Distribution of Respondent Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
st.pyplot(fig.figure)