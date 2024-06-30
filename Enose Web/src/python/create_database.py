import tkinter as tk

import serial
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

COM = 'COM4'
serial_port = serial.Serial(COM, baudrate=9600)

columns = ["Time", "Propana", "Hexana", "LPG_2", "CO", "CH4_a", "H2", "Alcohol",
        "LPG_1", "NOX", "CL2", "O3", "CO2", "Toluena", "H2S", "Amonia",
        "Etanol", "Benzena", "Aseton", "Butana", "CH4_b", "Target"]
df = pd.DataFrame(columns=columns)

Target = 0    # Ubah Setiap Kali Menjalankan kode

# Setup plot
plt.rcParams['figure.constrained_layout.use'] = True
figsize = (9,6)
dpi = 150
fig, ax = plt.subplots(dpi=dpi, figsize=figsize)
lines = {sensor: ax.plot([], [], label=sensor)[0] for sensor in columns[1:-1]}
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.xticks(rotation=30)
plt.title(f"Sensor Data - Target: {Target}")
plt.xlabel("Time (seconds)")
plt.ylabel("Sensor Value")

# Enable interactive mode
plt.ion()
plt.show()

# Define a flag to indicate if the plot window is closed
plot_closed = False

# Define a function to handle the plot close event
def on_close(event):
    global plot_closed
    plot_closed = True
    print("Plot closed. Exiting...")

# Connect the close event to the handler
fig.canvas.mpl_connect('close_event', on_close)
print("Mulai Membuat Database".center(50, "="))

try:
    while not plot_closed:
        line = serial_port.readline().decode('utf-8').strip()
        values = list(map(float, line.split()))

        now = pd.Timestamp.now()
        data = [now] + values + [Target]
        print(f"{len(df)} : {data} {len(list(df.columns))-2}:{len(values)}")
        df.loc[len(df)] = data

        # Membuat Plot
        x = df["Time"]
        y = df.iloc[:, 1:-1]

        for sensor in columns[1:-1]:
            lines[sensor].set_data(df["Time"], df[sensor])

        ax.relim()
        ax.autoscale_view()
        ax.set_xmargin(0)
        fig.canvas.draw_idle()
        fig.canvas.flush_events()

except Exception as e:
    print(f"Exception : {e}")
    print("Berhenti Membuat Database".center(50, "="))
    serial_port.close()

finally:
    if serial_port.is_open:
        serial_port.close()
    print("Menyimpan Data dan Plot".center(50, "="))

    # Membuat File Database
    nama_file = f"Database_{Target}"
    df.to_excel(f"{nama_file}.xlsx", index=False)
    df.to_csv(f"{nama_file}.csv", index=False)
    df.to_csv(f"{nama_file}.txt", sep=";", index=False)

    # Membuat Plot
    x = df["Time"]
    y = df.iloc[:, 1:-1]

    fig, ax = plt.subplots(dpi=dpi, figsize=figsize)
    for i, sensor in enumerate(columns[1:-1]):
        ax.plot(x, y.iloc[:, i], label=sensor)

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xmargin(0)
    plt.title(f"Sensor Data - Target: {Target}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    ax.relim()
    ax.autoscale_view()
    plt.savefig(f"{nama_file}.png")
