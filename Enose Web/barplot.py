import numpy as np
import matplotlib.pyplot as plt
import csv

# Fungsi untuk membaca dataset dari file
def baca_dataset(nama_file):
    data = np.genfromtxt(nama_file, delimiter=';', skip_header=1)
    return data[:, 1:-1], data[:, -1]

# Fungsi untuk menghitung rata-rata dan standar deviasi
def hitung_statistik(data):
    rata_rata = np.mean(data, axis=0)
    standar_deviasi = np.std(data, axis=0)
    return rata_rata, standar_deviasi

# Nama file dataset
nama_file = 'Dataset_Teh_Formatted.txt'

# Membaca dataset
fitur, target = baca_dataset(nama_file)

# Mendapatkan daftar unik target
daftar_target = np.unique(target)

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
for data in data_diagram:
    rata_rata, standar_deviasi, target_name = data
    rata_rata_kurang = np.abs(rata_rata - rata_rata_pertama)
    standar_deviasi_kurang = np.abs(standar_deviasi - standar_deviasi_pertama)
    data_diagram_kurang.append((rata_rata_kurang, standar_deviasi_kurang, target_name))

# Mendapatkan judul kolom dari file dataset
with open(nama_file, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    judul = next(reader)[1:-1]

# Mengatur posisi dan lebar setiap baris data
posisi = np.arange(len(judul))
lebar_baris = 0.8 / (len(daftar_target) - 1)

# Membuat diagram batang dalam satu frame grafik
fig, ax = plt.subplots(figsize=(10, 6))

for i, data in enumerate(data_diagram_kurang):
    rata_rata, standar_deviasi, target_name = data
    posisi_baris = posisi + (i * lebar_baris) - (lebar_baris * (len(daftar_target) - 2) / 2)
    ax.bar(posisi_baris, rata_rata, yerr=standar_deviasi, width=lebar_baris, align='center', alpha=0.5, label=target_name)

ax.set_xticks(posisi)
ax.set_xticklabels(judul)
ax.set_ylabel('Nilai')
ax.set_title('Analisis Respon Sensor')

plt.legend()
plt.tight_layout()

# Menyimpan gambar diagram batang ke file
nama_file_gambar_batang = 'diagram_batang.png'
plt.savefig(nama_file_gambar_batang)

# Menampilkan gambar diagram batang
plt.show()
