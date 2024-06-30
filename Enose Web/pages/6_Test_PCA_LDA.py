import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from scipy.stats import chi2

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Calculate max n_components for PCA and LDA
max_pca_components = min(X.shape)
max_lda_components = min(len(target_names) - 1, X.shape[1])

# Function to perform PCA and LDA
def perform_pca_lda(X, y, target_names, n_pca_components, n_lda_components):
    # PCA
    pca = PCA(n_components=n_pca_components)
    X_r = pca.fit_transform(X)

    # Create a DataFrame for PCA
    df_pca = pd.DataFrame(data=X_r, columns=[f'PC{i+1}' for i in range(X_r.shape[1])])
    df_pca['target'] = y
    df_pca['target_name'] = df_pca['target'].apply(lambda x: target_names[x])

    # LDA
    lda = LinearDiscriminantAnalysis(n_components=n_lda_components)
    X_r2 = lda.fit(X, y).transform(X)

    # Create a DataFrame for LDA
    df_lda = pd.DataFrame(data=X_r2, columns=[f'LD{i+1}' for i in range(X_r2.shape[1])])
    df_lda['target'] = y
    df_lda['target_name'] = df_lda['target'].apply(lambda x: target_names[x])

    return df_pca, df_lda

# Helper function to create ellipses
def get_ellipse_points(mean, cov, chi2_val=5.991, num_points=100):
    # Get eigenvalues and eigenvectors
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]

    # Compute the angle
    theta = np.arctan2(*vecs[:, 0][::-1])

    # Width and height of ellipse
    width, height = 2 * np.sqrt(vals * chi2_val)

    # Generate points on ellipse
    t = np.linspace(0, 2 * np.pi, num_points)
    ellipse = np.array([width/2 * np.cos(t), height/2 * np.sin(t)])
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    ellipse_rotated = np.dot(R, ellipse)

    ellipse_rotated[0] += mean[0]
    ellipse_rotated[1] += mean[1]

    path = "M " + " L ".join([f"{x},{y}" for x, y in zip(ellipse_rotated[0], ellipse_rotated[1])]) + " Z"
    return path

# Streamlit app
st.title('PCA and LDA Visualization')

# User input for number of components
num_pca_components = st.slider('Select number of PCA components to plot', 2, max_pca_components, 2)
num_lda_components = st.slider('Select number of LDA components to plot', 1, max_lda_components, 2)

# Perform PCA and LDA
df_pca, df_lda = perform_pca_lda(X, y, target_names, num_pca_components, num_lda_components)

# Plot PCA
fig_pca = px.scatter_matrix(df_pca,
                            dimensions=[f'PC{i+1}' for i in range(num_pca_components)],
                            color='target_name',
                            title='PCA of IRIS dataset',
                            labels={'target_name': 'Species'},
                            symbol='target_name')

# Adding ellipses to PCA plot
for target in target_names:
    target_data = df_pca[df_pca['target_name'] == target]
    mean = target_data[[f'PC{i+1}' for i in range(num_pca_components)]].mean().values
    cov = np.cov(target_data[[f'PC{i+1}' for i in range(num_pca_components)]].values.T)

    for i in range(num_pca_components):
        for j in range(i+1, num_pca_components):
            path = get_ellipse_points(mean[[i, j]], cov[np.ix_([i, j], [i, j])])
            fig_pca.add_shape(
                type='path',
                path=path,
                line=dict(color= '#FECB52'),
                opacity=0.5,
                xref=f'x{i+1}',
                yref=f'y{j+1}'
            )

# Plot LDA
fig_lda = px.scatter(df_lda, x='LD1', y='LD2', color='target_name',
                     title='LDA of IRIS dataset', labels={'target_name': 'Species'})

# Adding ellipses to LDA plot
for target in target_names:
    target_data = df_lda[df_lda['target_name'] == target]
    mean = target_data[['LD1', 'LD2']].mean().values
    cov = np.cov(target_data[['LD1', 'LD2']].values.T)
    
    path = get_ellipse_points(mean, cov)
    fig_lda.add_shape(
        type='path',
        path=path,
        line=dict(color=  '#FECB52'),
        opacity=0.5,
        xref='x',
        yref='y'
    )

st.plotly_chart(fig_pca)
st.plotly_chart(fig_lda)
