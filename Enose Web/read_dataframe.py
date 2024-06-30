import pandas as pd
import sqlite3
import requests
from io import BytesIO
import streamlit as st

def cek_format(file):
    if file.endswith(".xlsx") or file.endswith(".xls"):
        return "excel"
    elif file.endswith(".csv"):
        return "csv"
    elif file.endswith(".txt"):
        return "txt"
    elif file.endswith(".db"):
        return "db"
    else:
        return None

def read_dataframe(file, separator=None):
    if isinstance(file, str):
        if file.startswith("http://") or file.startswith("https://"):
            response = requests.get(file)
            response.raise_for_status()  # Ensure we notice bad responses
            file = BytesIO(response.content)
        format_file = cek_format(file)
    else:
        format_file = cek_format(file.name)

    if format_file == "excel":
        return pd.read_excel(file)
    elif format_file == "csv":
        if separator is not None:
            return pd.read_csv(file, sep=separator)
        else:
            return pd.read_csv(file, sep=",")
    elif format_file == "txt":
        if separator is not None:
            return pd.read_csv(file, sep=separator)
        else:
            return pd.read_csv(file, sep="\t")
    elif format_file == "db":
        conn = sqlite3.connect(file)
        query = "SELECT * FROM your_table_name"  # Ganti dengan query yang sesuai
        return pd.read_sql_query(query, conn)
    else:
        raise ValueError("Unsupported file format")

# Contoh penggunaan
if __name__ == "__main__":
    file_path = 'your_file_path_or_url_here'
    df = read_dataframe(file_path)
    print(df)
