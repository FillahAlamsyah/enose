import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Membaca dataset dari file .txt dengan pemisah ;
dataset = pd.read_csv('Dataset_Teh_Formatted.txt', delimiter=';')

# Memisahkan fitur dan kelas target
X = dataset.iloc[:, :-1].values
# Mengambil semua kolom kecuali kolom terakhir sebagai fitur
y = dataset.iloc[:, -1].values
# Mengambil kolom terakhir sebagai kelas target

# Melakukan PCA
pca = PCA(n_components=2)
# Mengganti 2 dengan jumlah komponen utama yang diinginkan
X_pca = pca.fit_transform(X)

# Menampilkan hasil PCA
print('Variance explained by each component:', \
      pca.explained_variance_ratio_)
print('Cumulative variance explained:', \
      np.cumsum(pca.explained_variance_ratio_))

# Membuat plot PCA tanda berbeda setiap kelas target dan pembatas kelas
unique_classes = np.unique(y)
for target_class in unique_classes:
    class_indices = np.where(y == target_class)
    plt.scatter(X_pca[class_indices, 0], X_pca[class_indices, 1],\
                label=f'Class {target_class}', s=10)

    # Menghitung batas-batas (boundaries) dari setiap kelas
    x_min, x_max = np.min(X_pca[class_indices, 0]), \
                   np.max(X_pca[class_indices, 0])
    y_min, y_max = np.min(X_pca[class_indices, 1]), \
                   np.max(X_pca[class_indices, 1])
    width = x_max - x_min
    height = y_max - y_min
    center = ((x_max + x_min) / 2, (y_max + y_min) / 2)

    # Membuat lingkaran atau elips pembatas
    ellipse = Ellipse(xy=center, width=width, height=height, \
                      edgecolor='black', facecolor='none')
    plt.gca().add_patch(ellipse)

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA Plot')
plt.legend(loc='best', prop={'size': 8})

# Menyimpan gambar dalam format PNG
plt.savefig('pca_plot.png', dpi=300)  # Ubah nama file sesuai kebutuhan

# Menampilkan plot
plt.show()
