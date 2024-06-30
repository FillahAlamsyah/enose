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

# Fungsi untuk membuat diagram radar
def buat_diagram(rata_rata, standar_deviasi, judul, target_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    num_vars = len(judul)
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False).tolist()
    theta += theta[:1]

    rata_rata = np.append(rata_rata, rata_rata[0])
    standar_deviasi = np.append(standar_deviasi, standar_deviasi[0])

    ax.plot(theta, rata_rata, linewidth=2, linestyle='solid', label=target_name)
    ax.fill(theta, rata_rata, alpha=0.25)

    ax.set_xticks(theta[:-1])
    ax.set_xticklabels(judul)
    ax.set_yticklabels([])
    ax.set_title('Diagram Radar - ' + str(target_name))

    # Menyimpan gambar ke file
    nama_file_gambar = 'diagram_radar_' + str(target_name) + '.png'
    plt.savefig(nama_file_gambar)

    # Menampilkan gambar yang disimpan
    plt.show()

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

# Memproses setiap target untuk membuat diagram radar
for data in data_diagram_kurang:
    rata_rata, standar_deviasi, target_name = data
    buat_diagram(rata_rata, standar_deviasi, judul, target_name)
