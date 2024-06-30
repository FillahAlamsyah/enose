import streamlit as st

st.title("Sensor Gas")

st.header("Spesifikasi Sensor Gas")

list_sensor = [
    "MQ-2 Sensor", "MQ-3 Sensor", "MQ-4 Sensor", "MQ-5 Sensor", "MQ-6 Sensor", "MQ-7 Sensor", "MQ-8 Sensor","MQ-9 Sensor",
    "MQ-131 Sensor", "MQ-135 Sensor", "MQ-136 Sensor", "MQ-137 Sensor", "MQ-138 Sensor",
    "TGS813 Sensor", "TGS822 Sensor", "TGS2600 Sensor", "TGS2602 Sensor","TGS2611 Sensor"
]

for sensor in list_sensor:
    with st.expander(label=sensor):
        st.subheader(sensor)
        st.text("Gas")

