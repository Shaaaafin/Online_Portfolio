import streamlit as st
import pandas

st.set_page_config(layout="wide")  # sets the website to be wide

col1, col2 = st.columns(2)  # divides the page into 2 columns

with col1:  # treated as a file. we are working on column 1
    st.image("photo.png")  # shows the indicated image on the page.

with col2:
    st.title("Ahnaf Hasan Shafin")  # title on the page
    content = """Hi this is Shafin. Introduction will be added later."""    # Contains
    # multiline text

    st.info(content)    # can use st.write but st.info produces bluish box, looks cool

st.write("Below you can see a few apps that I tried to build.")

col3,empty_column, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('Images/' + row['image'])


with col4:
    for index, row in df[5:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('Images/' + row['image'])