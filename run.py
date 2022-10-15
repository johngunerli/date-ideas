import streamlit as st
# https://docs.google.com/spreadsheets/d/1wCT96SP92FHnOkvLzEBELc6CYzYce_8YsFBmAKhxpDU/edit?usp=sharing
import pandas as pd 
import urllib

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQsmMfuH1mNMYfZen_KtNSm99oxvMIxBX2dP-A3X9nC2z-UMZeGiGoGJC3kc6a4e5JM3gsvF8av_C-R/pub?gid=1518743404&single=true&output=csv'
urllib.request.urlretrieve(url,"file.csv")

st.title("Date ideas bc can is stupid")



df = pd.read_csv('file.csv')
df.head(5)

st.write("Select location")
value = st.selectbox("Location", df['Name'].unique())

if st.button("Submit"):
    st.write("You selected", value)

 
#st.write(df.loc[df['Name'] == value])
st.write(df.loc[df['Name'] == value, 'Distance from MT'].values[0])