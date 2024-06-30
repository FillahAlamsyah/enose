import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Membaca dataset dari file .txt dengan pemisah ;
dataset = pd.read_csv('Database.txt', delimiter=';')

# Memisahkan fitur dan kelas target
X = dataset.iloc[:, :-1].values
# Mengambil semua kolom kecuali kolom terakhir sebagai fitur
y = dataset.iloc[:, -1].values
# Mengambil kolom terakhir sebagai kelas target

# Melakukan LDA
lda = LinearDiscriminantAnalysis(n_components=2)
# Mengganti 2 dengan jumlah komponen utama yang diinginkan
X_lda = lda.fit_transform(X, y)

# Menampilkan hasil LDA
print('Explained variance ratio:', lda.explained_variance_ratio_)

# Membuat plot LDA tanda berbeda setiap kelas target dan pembatas kelas
unique_classes = np.unique(y)
for target_class in unique_classes:
    class_indices = np.where(y == target_class)
    plt.scatter(X_lda[class_indices, 0], X_lda[class_indices, 1], \
                label=f'Class {target_class}', s=10)

    # Menghitung batas-batas (boundaries) dari setiap kelas
    x_min, x_max = np.min(X_lda[class_indices, 0]), \
                   np.max(X_lda[class_indices, 0])
    y_min, y_max = np.min(X_lda[class_indices, 1]), \
                   np.max(X_lda[class_indices, 1])
    width = x_max - x_min
    height = y_max - y_min
    center = ((x_max + x_min) / 2, (y_max + y_min) / 2)

    # Membuat lingkaran atau elips pembatas
    ellipse = Ellipse(xy=center, width=width, height=height, \
                      edgecolor='black', facecolor='none')
    plt.gca().add_patch(ellipse)

plt.xlabel('LD1')
plt.ylabel('LD2')
plt.title('LDA Plot')
plt.legend(loc='best', prop={'size': 8})

# Menyimpan gambar dalam format PNG
plt.savefig('lda_plot.png', dpi=300)  # Ubah nama file sesuai kebutuhan

# Menampilkan plot
plt.show()
