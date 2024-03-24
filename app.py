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
#Introduction
st.title("Exploring Global Financial Inclusion Trends: Insights from the Global Findex Database 2021") 
st.markdown(
    """
    Financial inclusion is the availability and equality of opportunities to access financial services. The 2021 edition of the Global Findex Database showcases the global economic update thru surveys of about 128,000 adults in 123 economic countries during the ongoing global pandemic of "COVID-19". The source data identifies disparities in accessing and utilizing financial services based on socioeconomic status, gender, and other factors."  
    """
)
#Objectives
st.subheader("Objectives")
st.image("./assets/objective.png")

#Methodology
st.subheader("Methodology")
st.image("./assets/Method.png")

#Scope and Limitations
st.subheader("Scope and Limitations")
st.markdown("- The data in the following analysis is from the year 2021, and doesn't reflect the current financial status of socioeconomic countries in the survey.")
st.markdown("- The scope is limited to what is available to the visualizations presented and does not include in-depth and validated analysis on the subject matters.")
st.markdown("- The analysis does not cover the wide aspects of the datasets provided by the global findex financial access and usage.")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)




#Visualization
st.subheader("1. Understanding the age distribution of respondents.")
fig = sns.histplot(data=df, x='age', bins=30, kde=True)
plt.title('Distribution of Respondent Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
st.pyplot(fig.figure)
st.write("the histogram shows that a large range of respondents are in the mid 30's and that most of the respondents within this age engage with financial services. This insight could be used by companies by focusing on targeting that age group and cater to them to an extent. ")


st.subheader("2. Main financial concern among respondents")
categories = {
    1: "Old Age",
    2: "Medical Cost",
    3: "Bills",
    4: "Education"
}

df['financially_most_worried'] = df['fin45'].map(categories)

category_counts = df['financially_most_worried'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue', ax=ax) 
plt.title('Financial Worries Among Respondents')
plt.xlabel('Concern Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
st.write("The graph shows that a high number of respondents worry the most financially about Medical costs, this information could be seen as a stepping stone on how to alleviate their concerns.")

st.subheader("3.  Visualizing the Percentage of Respondents with Mobile Money Accounts by Region")
filtered_df = df[df['regionwb'] != 'High income']  
fig, ax = plt.subplots()
sns.barplot(ax=ax, data=filtered_df, x='regionwb', y='account_mob', estimator=lambda x: sum(x)/len(x)*100)
plt.title('Percentage of Respondents with a Mobile Money Account by Region (excluding High Income)')
plt.xlabel('Region')
plt.ylabel('Percentage with Mobile Money Account')
plt.xticks(rotation=85)
st.pyplot(fig)
st.write("A large amount of respondents with Mobile money accounts came from the sub-Saharan africa region, This information could be used by mobile money companies as to why such high concentration of users originate from that particular region and how it compares to other regions.")

st.subheader("4. Understanding the Relationship between Income Quintile and Debit Card Ownership")

fig, ax = plt.subplots()  
sns.boxplot(ax=ax, data=df, x='account_fin', y='inc_q') 
plt.xlabel('Has Account at Financial Institution')
plt.ylabel('Income Quintile')
plt.xticks(rotation=45)  
st.pyplot(fig)  
st.write("Through boxplot analysis, it is evident that individuals who has debit cards has a larger gap in income quartile than those who doesn't have debit cards, which highlights potential disparities in financial access based on incoome levels.")


st.subheader("5. Analyzing the Comparison of Reasons for Not Having a Bank Account")
reason_columns = ['fin11a', 'fin11b', 'fin11c', 'fin11d', 'fin11e', 'fin11f', 'fin11g', 'fin11h']
reason_labels = ['Too far', 'Too expensive', 'Lack documentation', 'Lack trust', 'Religious reasons', 'Lack money', 'Family member has one', 'No need for financial services']

reason_counts = df[reason_columns].sum().reset_index()
reason_counts.columns = ['Reason', 'Count']

fig, ax = plt.subplots(figsize=(10, 6))  
sns.barplot(ax=ax, data=reason_counts, x='Count', y='Reason', palette='muted')  

plt.title('Comparison of Reasons for Not Having a Bank Account (Custom Title)')  
plt.xlabel('Count (Custom Label)')  
plt.ylabel('Reason (Custom Label)')  
plt.xticks(rotation=45)  
plt.tick_params(bottom=False)  
ax.bar_label(ax.containers[0])  
st.pyplot(fig)
st.write("Investigation shows that the most common reason for not having a bank account are due to religious reasons followed by other factors such as lack of documentation and distrust, this reasons could help policy makers and financial institutions to tackle those problems and convince them with better policies and format.")


st.subheader("Conclusion")
st.write("In conclusion Global Findex Database 2021 provides valuable information into the different financial disparities and segregation, putting us into perspective on how factors contribute to reasons of various problems financial institutions are looking to solve. These insights could help policy makers, financial institutions and stakeholders promote financial inclusion and address barriers to banking access globally.")

st.write("Created by Niño B. Garcia, 3rd- Year BSCS - Data Science, 19001618300")