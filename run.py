import streamlit as st
# https://docs.google.com/spreadsheets/d/1wCT96SP92FHnOkvLzEBELc6CYzYce_8YsFBmAKhxpDU/edit?usp=sharing
import pandas as pd 
import urllib.request

# url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQsmMfuH1mNMYfZen_KtNSm99oxvMIxBX2dP-A3X9nC2z-UMZeGiGoGJC3kc6a4e5JM3gsvF8av_C-R/pub?gid=1518743404&single=true&output=csv'
# urllib.request.urlretrieve(url,"file.csv")

st.title("Date ideas bc can is stupid")

df = pd.read_csv('file.csv')

st.write("Select location to go to")
value = st.selectbox("Location", df['Name'].unique())

if st.button("Submit"):
    st.write("You selected", value)

st.write("Select location to go FROM")
part_of_town= st.selectbox("Location", ["Midtown", "Downtown"])
 
#st.write(df.loc[df['Name'] == value])
if part_of_town == "Midtown":
    st.write(df.loc[df['Name'] == value]['Distance from MT'])
    # find the row that matches the value, than get the value from walking Directions from MT
    st.write(df.loc[df['Name'] == value]['walking Directions from MT'].values[0])
else: 
    st.write(df.loc[df['Name'] == value]['Distance from DT'])
    st.write(df.loc[df['Name'] == value]['walking Directions from DT'].values[0])