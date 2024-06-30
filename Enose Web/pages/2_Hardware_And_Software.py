import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hardware dan Software",
    page_icon="👃",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Hardware dan Software")
st.header("Hardware")

Hardware_data = [
    {"No": 1, "Alat dan Bahan": "Raspberry PI 4", "Jumlah": "1 buah"},
    {"No": 2, "Alat dan Bahan": "Arduino Mega", "Jumlah": "1 buah"},
    {"No": 3, "Alat dan Bahan": "Sensor MQ-2", "Jumlah": "1 buah"},
    {"No": 4, "Alat dan Bahan": "Sensor MQ-3", "Jumlah": "1 buah"},
    {"No": 5, "Alat dan Bahan": "Sensor MQ-4", "Jumlah": "1 buah"},
    {"No": 6, "Alat dan Bahan": "Sensor MQ-5", "Jumlah": "1 buah"},
    {"No": 7, "Alat dan Bahan": "Sensor MQ-6", "Jumlah": "1 buah"},
    {"No": 8, "Alat dan Bahan": "Sensor MQ-7", "Jumlah": "1 buah"},
    {"No": 9, "Alat dan Bahan": "Sensor MQ-8", "Jumlah": "1 buah"},
    {"No": 10, "Alat dan Bahan": "Sensor MQ-9", "Jumlah": "1 buah"},
    {"No": 11, "Alat dan Bahan": "Sensor MQ-131", "Jumlah": "1 buah"},
    {"No": 12, "Alat dan Bahan": "Sensor MQ-135", "Jumlah": "1 buah"},
    {"No": 13, "Alat dan Bahan": "Sensor MQ-136", "Jumlah": "1 buah"},
    {"No": 14, "Alat dan Bahan": "Sensor MQ-137", "Jumlah": "1 buah"},
    {"No": 15, "Alat dan Bahan": "Sensor MQ-138", "Jumlah": "1 buah"},
    {"No": 16, "Alat dan Bahan": "Sensor TGS813", "Jumlah": "1 buah"},
    {"No": 17, "Alat dan Bahan": "Sensor TGS822", "Jumlah": "1 buah"},
    {"No": 18, "Alat dan Bahan": "Sensor TGS2600", "Jumlah": "1 buah"},
    {"No": 19, "Alat dan Bahan": "Sensor TGS2611", "Jumlah": "1 buah"},
    {"No": 20, "Alat dan Bahan": "Kabel Jumper", "Jumlah": "Secukupnya"},
    {"No": 21, "Alat dan Bahan": "Akrilik Transparan", "Jumlah": "Secukupnya"},
    {"No": 22, "Alat dan Bahan": "Keyboard Bluetooth", "Jumlah": "1 buah"},
    {"No": 23, "Alat dan Bahan": "Mouse Bluetooth", "Jumlah": "1 buah"},
    {"No": 24, "Alat dan Bahan": "Kipas 8 cm", "Jumlah": "2 buah"},
    {"No": 25, "Alat dan Bahan": "5 inch HDMI LCD (H) Capacitive Touch Screen 800x480 Support Various Systems", "Jumlah": "1 buah"}
]

st.caption("Tabel Hardware")
st.table(pd.DataFrame(Hardware_data).iloc[:,1:],)

st.subheader("Arduino Mega 2560")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("https://store-usa.arduino.cc/cdn/shop/products/A000067_00.front_1000x750.jpg?v=1637830354", width=500,
        caption="Arduino Mega 2560")

st.markdown(''' [Pinout Arduino Mega 25560](https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf)''')
st.markdown(''' [Datasheet Arduino Mega 25560](https://docs.arduino.cc/resources/datasheets/A000067-datasheet.pdf)''')

st.text("Spesifikasi Teknis Arduino Mega 2560")
table_html = """
<table border="1" style="width:100%">
  <tr>
    <th colspan="2">Papan (Board)</th>
  </tr>
  <tr>
    <td>Nama</td>
    <td>Arduino®Mega 2560 Rev3</td>
  </tr>
  <tr>
    <td>SKU</td>
    <td>A000067</td>
  </tr>
  <tr>
    <td>Mikrokontroler</td>
    <td>ATmega2560</td>
  </tr>
  <tr>
    <td>konektor USB</td>
    <td>USB-B</td>
  </tr>
  <tr>
    <th colspan="2">Pin</th>
  </tr>
  <tr>
    <td>Pin LED bawaan</td>
    <td>1300%</td>
  </tr>
  <tr>
    <td>Pin I/O Digital</td>
    <td>5400%</td>
  </tr>
  <tr>
    <td>Pin masukan analog</td>
    <td>1600%</td>
  </tr>
  <tr>
    <td>Pin PWM</td>
    <td>1500%</td>
  </tr>
  <tr>
    <th colspan="2">Komunikasi</th>
  </tr>
  <tr>
    <td>UART</td>
    <td>Ya, 4</td>
  </tr>
  <tr>
    <td>I2C</td>
    <td>Ya</td>
  </tr>
  <tr>
    <td>SPI</td>
    <td>Ya</td>
  </tr>
  <tr>
    <th colspan="2">Kekuatan/Daya</th>
  </tr>
  <tr>
    <td>Tegangan I/O</td>
    <td>5V</td>
  </tr>
  <tr>
    <td>Tegangan masukan (nominal)</td>
    <td>7-12V</td>
  </tr>
  <tr>
    <td>Arus DC per Pin I/O</td>
    <td>20mA</td>
  </tr>
  <tr>
    <td>Baterai yang didukung</td>
    <td>Baterai 9V</td>
  </tr>
  <tr>
    <td>Konektor Catu Daya</td>
    <td>Steker barel</td>
  </tr>
  <tr>
    <th colspan="2">Kecepatan Clock</th>
  </tr>
  <tr>
    <td>Prosesor Utama</td>
    <td>ATmega2560 16MHz</td>
  </tr>
  <tr>
    <td>Prosesor Serial USB</td>
    <td>ATmega16U2 16MHz</td>
  </tr>
  <tr>
    <th colspan="2">Penyimpanan</th>
  </tr>
  <tr>
    <td>ATmega2560</td>
    <td>SRAM 8KB, FLASH 256KB, EEPROM 4KB</td>
  </tr>
  <tr>
    <th colspan="2">Ukuran</th>
  </tr>
  <tr>
    <td>Berat</td>
    <td>37 gram</td>
  </tr>
  <tr>
    <td>Lebar</td>
    <td>53,3 mm</td>
  </tr>
  <tr>
    <td>Panjang</td>
    <td>101,5mm</td>
  </tr>
</table>
"""

# Tampilkan tabel dengan streamlit
st.markdown(table_html, unsafe_allow_html=True)

st.subheader("Raspberry Pi 4")

left,center,right = st.columns(3)
with center:
  # https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png?hash=df7d7847c57a1ca6d5b2617695de6d46
    st.image("https://assets.raspberrypi.com/static/blueprint-labelled-97975f4b1159239a8e248d180be87e3e.svg", width=500,
        caption="Raspberry Pi 4 Pinout")

st.markdown("[Datasheet Raspberry Pi 4](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-product-brief.pdf)")
data = {
    "Spesifikasi": [
        "Prosesor",
        "Memori",
        "Konektivitas",
        "GPIO",
        "Video & suara",
        "Multimedia",
        "Dukungan kartu SD",
        "Daya input",
        "Lingkungan",
        "Masa produksi",
        "Kepatuhan"
    ],
    "Rincian": [
        "Broadcom BCM2711, quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz",
        "1GB, 2GB, 4GB atau 8GB LPDDR4 (tergantung model) dengan ECC on-die",
        "• LAN nirkabel IEEE 802.11b/g/n/ac 2.4 GHz dan 5.0 GHz, Bluetooth 5.0, BLE\n• Gigabit Ethernet\n• 2 × port USB 3.0\n• 2 × port USB 2.0",
        "Header GPIO 40-pin standar (sepenuhnya kompatibel dengan papan sebelumnya)",
        "• 2 × port micro HDMI (mendukung hingga 4Kp60)\n• port tampilan MIPI DSI 2-lane\n• port kamera MIPI CSI 2-lane\n• port audio stereo 4-pole dan video komposit",
        "H.265 (dekode 4Kp60); H.264 (dekode 1080p60, enkode 1080p30); grafis OpenGL ES 3.0",
        "Slot kartu Micro SD untuk memuat sistem operasi dan penyimpanan data",
        "• 5V DC melalui konektor USB-C (minimal 3A)\n• 5V DC melalui header GPIO (minimal 3A)\n• Mendukung Power over Ethernet (PoE) (memerlukan PoE HAT terpisah)",
        "Suhu operasi 0–50ºC",
        "Raspberry Pi 4 Model B akan tetap diproduksi setidaknya hingga Januari 2034.",
        "Untuk daftar lengkap persetujuan produk lokal dan regional, silakan kunjungi pip.raspberrypi.com"
    ]
}

# Buat DataFrame
df = pd.DataFrame(data)
st.table(df)

st.divider()
st.header("Software")

software_data = [
    {"No": 1, "Perangkat Lunak": "Sistem Operasi", "Spesifikasi": "Raspberry Pi OS System 64-bit Kernel version: 6.1 Debian version: 11 (bullseye)"},
    {"No": 2, "Perangkat Lunak": "Bahasa Pemrograman", "Spesifikasi": "Python versi 3.9.6 dan Arduino IDE 2.0.4"},
    {"No": 3, "Perangkat Lunak": "Editor Rangkaian Elektronika", "Spesifikasi": "Fritzing 0.9.3"},
    {"No": 4, "Perangkat Lunak": "Editor Gambar", "Spesifikasi": "Inkscape 0.92"}
]

# Convert the list of dictionaries to a pandas DataFrame
software_df = pd.DataFrame(software_data)
st.dataframe(software_df, hide_index=True)
