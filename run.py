import streamlit as st
import pandas as pd 
import urllib.request

# TODO: this file should be received from the gdoc link and downloaded automatically, but doesn't.
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
