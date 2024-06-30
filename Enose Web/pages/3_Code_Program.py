import streamlit as st
import pandas as pd

def read_code_file(path):
    with open(path, 'r') as file:
        return file.read()

st.set_page_config(
    page_title="Program ENose",
    page_icon="👃",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Program ENose")

st.header("Program Arduino ")
st.markdown('''
Program arduino ini berfungsi untuk membaca nilai ppm gas dari setiap sensor. Untuk mendapatkan nilai ppm,  [ Library MQUnifiedsensor ](https://github.com/miguel5612/MQSensorsLib)  digunakan agar mempermudah pembacaan sensor.

Terdapat 4 tahap untuk memprogram Arduino.
1. Mendefinisikan variabel.
```cpp
#include <MQUnifiedsensor.h>
#define         Board                   ("Arduino UNO")
#define         Pin                     (A2)
#define         Type                    ("MQ-2") //MQ2
#define         Voltage_Resolution      (5)
#define         ADC_Bit_Resolution      (10) // For arduino UNO/MEGA/NANO
#define         RatioMQ2CleanAir        (9.83) //RS / R0 = 9.83 ppm 
```

2. Mendeklarasikan Sensor.
```cpp
MQUnifiedsensor MQ2(Board, Voltage_Resolution, ADC_Bit_Resolution, Pin, Type);
```
3. Melakukan kalibrasi sensor.
```cpp
void setup() {
    Serial.begin(9600);

    //Set math model to calculate the PPM concentration and the value of constants
    MQ2.setRegressionMethod(1); //_PPM =  a*ratio^b
    MQ2.setA(574.25); MQ2.setB(-2.222); // Configure the equation to to calculate LPG concentration
    MQ2.init();

    Serial.print("Calibrating please wait.");
    float calcR0 = 0;
    for(int i = 1; i<=10; i ++){
        MQ2.update(); // Update data, the arduino will read the voltage from the analog pin
        calcR0 += MQ2.calibrate(RatioMQ2CleanAir);
        Serial.print(".");
    }
    MQ2.setR0(calcR0/10);
    Serial.println("  done!.");

    if(isinf(calcR0)) {Serial.println("Warning: Conection issue, R0 is infinite (Open circuit detected) please check your wiring and supply"); while(1);}
    if(calcR0 == 0){Serial.println("Warning: Conection issue found, R0 is zero (Analog pin shorts to ground) please check your wiring and supply"); while(1);}
}
```
4. Membaca sensor.
```cpp
void loop(){
    MQ2.update();
    Serial.println(MQ2.readSensor());
}
```
''')
with st.expander("Show Full Code"):
    example_code = r"src\arduino\example.ino"
    st.code(read_code_file(example_code), language='cpp',line_numbers=True)



with st.expander("Show Full Code"):
    arduino_file_path = r"src\arduino\Program_Arduino_Enose_2024.ino"
    st.code(read_code_file(arduino_file_path), language='cpp',line_numbers=True)

st.divider()
st.header("Program Python")
st.subheader("Program Membuat Database")

database_code = '''
import serial
import pandas as pd
import matplotlib.pyplot as plt

COM = 'COM4'
serial_port = serial.Serial(COM, baudrate=9600)

columns = ["Time", "Propana", "Hexana", "LPG_2", "CO", "CH4_a", "H2", "Alcohol",
        "LPG_1", "NOX", "CL2", "O3", "CO2", "Toluena", "H2S", "Amonia",
        "Etanol", "Benzena", "Aseton", "Butana", "CH4_b", "Target"]
df = pd.DataFrame(columns=columns)

Target = 0    # Ubah Setiap Kali Menjalankan kode

print("Mulai Membuat Database".center(50, "="))

try:
    while True:
        line = serial_port.readline().decode('utf-8').strip()
        values = list(map(float, line.split()))

        now = pd.Timestamp.now()
        data = [now] + values + [Target]
        print(f"{len(df)} : {data}")
        df.loc[len(df)] = data

        # Membuat Plot
        x = df["Time"]
        y = df.iloc[:, 1:-1]

        fig, ax = plt.subplots(dpi=300)
        for i, sensor in enumerate(columns[1:-1]):
            ax.plot(x, y.iloc[:, i], label=sensor)

        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.title(f"Sensor Data - Target: {current_target}")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Sensor Value")
        plt.show()

except KeyboardInterrupt:
    print("Berhenti Membuat Database".center(50, "="))
    serial_port.close()

finally:
    print("Menyimpan Data dan Plot".center(50, "="))

    # Membuat File Database
    nama_file = "Database_" + Target
    df.to_excel(f"{nama_file}.xlsx", index=False)
    df.to_csv(f"{nama_file}.csv", index=False)
    df.to_csv(f"{nama_file}.txt", sep=";", index=False)

    # Membuat Plot
    x = df["Time"]
    y = df.iloc[:, 1:-1]

    fig, ax = plt.subplots(dpi=300)
    for i, sensor in enumerate(columns[1:-1]):
        ax.plot(x, y.iloc[:, i], label=sensor)

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.title(f"Sensor Data - Target: {current_target}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    plt.savefig(f"{nama_file}.png")
    #plt.show()
'''
st.code(database_code, language="python", line_numbers=True)

st.subheader("Program Membuat Prediksi")
prediction_code = '''
import serial
import pandas as pd
import matplotlib.pyplot as plt

'''
st.code(prediction_code, language="python", line_numbers=True)

st.subheader("Program GUI")
GUI_code = '''
import serial
import pandas as pd
import matplotlib.pyplot as plt

'''
st.code(GUI_code, language="python", line_numbers=True)