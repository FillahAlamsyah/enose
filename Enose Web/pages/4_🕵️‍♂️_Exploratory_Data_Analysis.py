import streamlit as st
from read_dataframe import read_dataframe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from io import BytesIO

st.set_page_config(
    page_title="Exploratory Data Analysis (EDA)",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🕵️‍♂️ Exploratory Data Analysis (EDA)")

st.markdown(''' Pada halaman ini adalah berfokus pada Analisis Dataset yang telah dibuat. Terdapat dua jenis analisis.
1. Visualisasi data
2. Dimensionality Reduction

Sebelum menuju kedua jenis analisis, persiapkan data terlebih dahulu.
''')

df : pd.DataFrame = pd.DataFrame([])
file_default = r"Database\Database.txt"
file_input = None

with st.expander("Persiapkan Dataset",expanded=True):
    input_data = st.toggle("Input Data")
    if input_data:
        uploaded_files = st.file_uploader("Upload Data", accept_multiple_files=True)
        if uploaded_files is not None:
            for file in uploaded_files:
                file_input = file
    else:
        file_input = file_default

    separator = st.selectbox("Pilih Jenis separator",("Titik Koma (;)", "Tab (\\t)", "Koma (,)"))
    if file_input is not None:
        if input_data:
            st.text(file_input.name)
        st.text(file_input)
        df = read_dataframe(file_input ,separator=";")
    if st.checkbox("Show Dataframe", value=True):
        st.dataframe(df)

st.header("Visualisasi Data")
st.subheader("Diagram Batang")

def plot_bar(data: pd.DataFrame):
    fitur = data.iloc[:, 1:-1]
    target = data.iloc[:, -1]

    def hitung_statistik(data):
        rata_rata = data.mean()
        standar_deviasi = data.std()
        return rata_rata, standar_deviasi

    # Mendapatkan daftar unik target
    daftar_target = target.unique()

    # Menghitung rata-rata dan standar deviasi untuk setiap target
    data_diagram = []
    rata_rata_pertama = None
    standar_deviasi_pertama = None
    for t in daftar_target:
        fitur_target = fitur[target == t]
        rata_rata, standar_deviasi = hitung_statistik(fitur_target)
        if t == daftar_target[0]:
            rata_rata_pertama = rata_rata
            standar_deviasi_pertama = standar_deviasi
        else:
            data_diagram.append((rata_rata, standar_deviasi, t))

    # Mengurangi rata-rata dan standar deviasi dengan nilai dari target pertama dan membuatnya absolut
    data_diagram_kurang = []
    for rata_rata, standar_deviasi, target_name in data_diagram:
        rata_rata_kurang = (rata_rata - rata_rata_pertama).abs()
        standar_deviasi_kurang = (standar_deviasi - standar_deviasi_pertama).abs()
        data_diagram_kurang.append((rata_rata_kurang, standar_deviasi_kurang, target_name))

    # Mengatur posisi dan lebar setiap baris data
    judul = fitur.columns
    posisi = np.arange(len(judul))
    lebar_baris = 0.8 / (len(daftar_target) - 1)

    # Membuat diagram batang dalam satu frame grafik menggunakan Matplotlib
    fig1, ax = plt.subplots(figsize=(10, 6))

    for i, (rata_rata_kurang, standar_deviasi_kurang, target_name) in enumerate(data_diagram_kurang):
        posisi_baris = posisi + (i * lebar_baris) - (lebar_baris * (len(daftar_target) - 2) / 2)
        ax.bar(posisi_baris, rata_rata_kurang, yerr=standar_deviasi_kurang, width=lebar_baris, align='center', alpha=0.5, label=str(target_name))

    ax.set_xticks(posisi)
    ax.set_xticklabels(judul, rotation=45)
    ax.set_ylabel('Nilai')
    ax.set_title('Analisis Respon Sensor')

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()

    # Membuat diagram batang dalam satu frame grafik menggunakan Plotly
    fig2 = go.Figure()

    for i, (rata_rata_kurang, standar_deviasi_kurang, target_name) in enumerate(data_diagram_kurang):
        posisi_baris = posisi + (i * lebar_baris) - (lebar_baris * (len(daftar_target) - 2) / 2)
        fig2.add_trace(go.Bar(
            x=judul,
            y=rata_rata_kurang,
            error_y=dict(type='data', array=standar_deviasi_kurang),
            name=str(target_name),  # Ensure target_name is a string
            width=lebar_baris
        ))

    fig2.update_layout(
        barmode='group',
        xaxis_title='Fitur',
        yaxis_title='Nilai',
        title='Analisis Respon Sensor',
        legend_title_text='Target',
        xaxis_tickangle=-45
    )
    return fig1, fig2

def save_matplotlib_fig(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return buf

def save_plotly_fig(fig):
    buf = BytesIO()
    fig.write_image(buf, format="png")
    buf.seek(0)
    return buf

fig1, fig2 = plot_bar(df)

if st.checkbox("Tampilkan Diagram Batang", value=True):
    st.pyplot(fig1)
    st.plotly_chart(fig2)

buf1 = save_matplotlib_fig(fig1)
st.download_button(
    label="Download Matplotlib Figure",
    data=buf1,
    file_name="matplotlib_figure.png",
    mime="image/png"
)

# Download button for Plotly figure
buf2 = save_plotly_fig(fig2)
st.download_button(
    label="Download Plotly Figure",
    data=buf2,
    file_name="plotly_figure.png",
    mime="image/png"
)

st.subheader("Diagram Radar")

# Fungsi untuk membuat diagram radar matplotlib
def buat_diagram_matplotlib(rata_rata, judul, target_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    num_vars = len(judul)
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False).tolist()
    theta += theta[:1]

    rata_rata = np.append(rata_rata, rata_rata[0])

    ax.plot(theta, rata_rata, linewidth=2, linestyle='solid', label=target_name)
    ax.fill(theta, rata_rata, alpha=0.25)

    ax.set_xticks(theta[:-1])
    ax.set_xticklabels(judul)
    ax.set_yticklabels([])
    ax.set_title('Diagram Radar - ' + str(target_name))

    return fig

# Fungsi untuk membuat diagram radar plotly
def buat_diagram_plotly(rata_rata, judul, target_name):
    rata_rata = np.append(rata_rata, rata_rata[0])

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=rata_rata,
        theta=judul + [judul[0]],
        fill='toself',
        name=str(target_name)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True)
        ),
        showlegend=True,
        title='Diagram Radar - ' + str(target_name)
    )

    return fig

# Fungsi utama untuk memproses dataset dan menghasilkan diagram radar
def proses_dataset(data:pd.DataFrame):
    fitur = data.iloc[:, 1:-1]
    target = data.iloc[:, -1]

    # Mendapatkan daftar unik target
    daftar_target = target.unique()

    # Fungsi untuk menghitung rata-rata dan standar deviasi
    def hitung_statistik(data):
        rata_rata = data.mean()
        standar_deviasi = data.std()
        return rata_rata, standar_deviasi

    # Menghitung rata-rata dan standar deviasi untuk setiap target
    data_diagram = []
    rata_rata_pertama = None
    for t in daftar_target:
        fitur_target = fitur[target == t]
        rata_rata, standar_deviasi = hitung_statistik(fitur_target)
        if rata_rata_pertama is None:
            rata_rata_pertama = rata_rata
        else:
            data_diagram.append((np.abs(rata_rata - rata_rata_pertama), t))

    # Mendapatkan judul kolom dari file dataset
    judul = fitur.columns.tolist()

    # Membuat kolom untuk setiap plot
    cols1 = st.columns(len(data_diagram))

    # Memproses setiap target untuk membuat diagram radar
    for i, (rata_rata, target_name) in enumerate(data_diagram):
        fig_matplotlib = buat_diagram_matplotlib(rata_rata, judul, target_name)
        with cols1[i]:
            st.pyplot(fig_matplotlib, use_container_width=True)

    cols2 = st.columns(len(data_diagram))
    for i, (rata_rata, target_name) in enumerate(data_diagram):
        fig_plotly = buat_diagram_plotly(rata_rata, judul, target_name)
        with cols2[i]:
            st.plotly_chart(fig_plotly, use_container_width=True)

# Menjalankan proses dataset

proses_dataset(df)


st.divider()
st.header("Dimensionality Reduction")
st.subheader("PCA (Principal Component Analysis)")

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
def plot_pca(dataframe, n_components=2, feature_columns=None, target_column=None):
    # If feature_columns and target_column are not provided, assume the last column is the target
    if feature_columns is None:
        feature_columns = dataframe.columns[1:-1]
    if target_column is None:
        target_column = dataframe.columns[-1]

    # Splitting features and target
    X = dataframe[feature_columns].values
    y = dataframe[target_column].values

    # Performing PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)

    # Printing variance explained
    st.text(f'Variance explained by each component: {pca.explained_variance_ratio_}')
    st.text(f'Cumulative variance explained:{ np.cumsum(pca.explained_variance_ratio_)}')

    # Creating PCA plot
    fig, ax = plt.subplots()
    unique_classes = np.unique(y)
    for target_class in unique_classes:
        class_indices = np.where(y == target_class)
        ax.scatter(X_pca[class_indices, 0], X_pca[class_indices, 1],
                label=f'Class {target_class}', s=10)

        # Calculating boundaries
        x_min, x_max = np.min(X_pca[class_indices, 0]),\
                    np.max(X_pca[class_indices, 0])
        y_min, y_max = np.min(X_pca[class_indices, 1]),\
                    np.max(X_pca[class_indices, 1])
        width = x_max - x_min
        height = y_max - y_min
        center = ((x_max + x_min) / 2, (y_max + y_min) / 2)

        # Adding ellipse
        ellipse = Ellipse(xy=center, width=width, height=height,
                        edgecolor='black', facecolor='none')
        ax.add_patch(ellipse)

    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_title('PCA Plot')
    ax.legend(loc='best', prop={'size': 8})

    # Returning the figure
    return fig
fig3 = plot_pca(df)
st.pyplot(fig3)

st.subheader("LDA (Linear Discriminant Analysis)")

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def plot_lda(dataframe, n_components=2, feature_columns=None, target_column=None):
    # If feature_columns and target_column are not provided, assume the last column is the target
    if feature_columns is None:
        feature_columns = dataframe.columns[1:-1]
    if target_column is None:
        target_column = dataframe.columns[-1]
    
    # Splitting features and target
    X = dataframe[feature_columns].values
    y = dataframe[target_column].values

    # Performing LDA
    lda = LinearDiscriminantAnalysis(n_components=n_components)
    X_lda = lda.fit_transform(X, y)

    # Printing explained variance ratio
    if hasattr(lda, 'explained_variance_ratio_'):
        st.text(f'Explained variance ratio: {lda.explained_variance_ratio_}')
    else:
        st.text('Explained variance ratio not available.')

    # Creating LDA plot
    fig, ax = plt.subplots()
    unique_classes = np.unique(y)
    for target_class in unique_classes:
        class_indices = np.where(y == target_class)
        ax.scatter(X_lda[class_indices, 0], X_lda[class_indices, 1], label=f'Class {target_class}', s=10)

        # Calculating boundaries
        x_min, x_max = np.min(X_lda[class_indices, 0]), np.max(X_lda[class_indices, 0])
        y_min, y_max = np.min(X_lda[class_indices, 1]), np.max(X_lda[class_indices, 1])
        width = x_max - x_min
        height = y_max - y_min
        center = ((x_max + x_min) / 2, (y_max + y_min) / 2)

        # Adding ellipse
        ellipse = Ellipse(xy=center, width=width, height=height, edgecolor='black', facecolor='none')
        ax.add_patch(ellipse)

    ax.set_xlabel('LD1')
    ax.set_ylabel('LD2')
    ax.set_title('LDA Plot')
    ax.legend(loc='best', prop={'size': 8})

    # Returning the figure
    return fig

fig4 = plot_lda(df)
st.pyplot(fig4)