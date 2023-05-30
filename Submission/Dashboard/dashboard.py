import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


sns.set(style='dark')

#load data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")


with st.sidebar:
    # Menambahkan gambar 
    st.subheader("Bike Sharing")
    st.image("https://www.intelligenttransport.com/wp-content/uploads/Dott-6.jpg")
    st.caption("This was made for learning purpose only")
    st.divider()
    


#slice dataset per tahun
df_2011 = day_df[day_df["yr"] ==0]
df_2012 = day_df[day_df["yr"] ==1]

st.header('Bike Sharing Dashboard :sparkles:')
st.subheader('By Kayla Alysa Adra')

st.subheader("Total Count in 2011 & 2012")
col1, col2 = st.columns(2)

with col1:
    total_count_2011 = df_2011.cnt.sum()
    st.metric("Total Count in 2011", value=total_count_2011)

    
with col2:
    total_count_2012 = df_2012.cnt.sum()
    st.metric("Total Count 2012",value=total_count_2012)

st.subheader("Total Registered in 2011 & 2012")
             
col1, col2 = st.columns(2)
    
with col1:
    registered_2011 = df_2011.registered.sum()
    st.metric("Total Registered in 2011", registered_2011)
    
with col2:
    registered_2012 = df_2012.registered.sum()
    st.metric("Total Registered in 2012", registered_2012)
    
    
st.subheader("Bike Sharing in Working Day")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    colors=["#9BABB8","#967E76"]
    sns.countplot(x='workingday', data=df_2011, palette=colors)
    plt.title('Bike Sharing in Working Day (2011)', fontsize=18)
    plt.xlabel("Working Day")
    plt.ylabel("Total Count")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    colors=["#9BABB8", "#967E76"]
    sns.countplot(x='workingday', data=df_2012, palette=colors)
    plt.title('Bike Sharing in Working Day (2012)', fontsize=18)
    plt.xlabel("Working Day")
    plt.ylabel("Total Count")
    st.pyplot(fig)
    
st.subheader("Bike Sharing per Month in 2011 & 2012")
fig, ax = plt.subplots(figsize=(20, 10))

df_2011.groupby("mnth").cnt.sum().plot(marker='o', linewidth=2,color="#D7C0AE")

plt.title("Total Bike Sharing per Month (2011)", loc="center", fontsize=20)
plt.xlabel("month")
plt.ylabel("total count")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(20, 10))

df_2012.groupby("mnth").cnt.sum().plot(kind='barh', color="#D7C0AE")
plt.title('Total Bike Sharing per Month (2012)', fontsize=20)
plt.xlabel("Total Count")
plt.ylabel("Month")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
season_data = day_df.copy()
season_data['season']= season_data['season'].replace(
    to_replace=[1,2,3,4], 
    value=['spring', 'summer','fall','winter'])
colors = ['#EEE3CB','#D7C0AE' ,'#9BABB8', '#967E76']
season_data.groupby(by='season').cnt.sum().plot.pie(subplots=True, figsize=(12,8), colors=colors ,autopct = '%1.1f%%',)
plt.legend()
plt.title('Distribution Customer for Every Season', fontsize=20, loc='center')
st.pyplot(fig)                      
    


st.caption('Copyright © Kayla Alysa Adra 2023')

