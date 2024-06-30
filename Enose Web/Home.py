import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Enose System Web",
    page_icon="👃",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("👃 Enose System")

st.header("Overview")

st.text('''E-Nose (Electronic-Nose) atau "Hidung Elektronik" adalah rangkaian elektronik yang bertujuan untuk mendeteksi gas menggunakan sensor dari suatu sampel yang akan diteliti
sebagaimana cara Hidung bekerja. Pada penerapannya, E-Nose dapat digunakan pada beberapa aktivitas seperti melakukan identifikasi gas yang dihasilkan
oleh suatu objek yang selanjutnya akan digunakan untuk mengklasifikasikan objek sejenis.''')

st.divider()


database = r"Database\Database.txt"
dataframe = pd.read_csv(database, header=0, sep=";")
columns = dataframe.columns
st.dataframe(columns.to_frame().T, use_container_width=True, hide_index=True)
st.markdown(
    """
    <style>
    .dataframe-container {
        width: 100%;
        overflow-x: auto;
    }
    .dataframe-container table {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.dataframe(data=dataframe)

