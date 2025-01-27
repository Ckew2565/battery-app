import streamlit as st
import os

# ตั้งค่าหน้า Streamlit
st.set_page_config(page_title="Battery Cell Heat Prediction", layout="wide")

# ส่วนหัวของหน้า
st.markdown(
    "<h1 style='text-align: center;'>Prediction of Heat Distribution in Battery Cells for Electric Vehicles</h1>",
    unsafe_allow_html=True,
)

# เมนูด้านข้าง (Sidebar) สำหรับเลือกหน้า
menu = st.sidebar.radio("Select Page", ["Home", "Graph Temperature and flow", "Graph Temperature change and load", "Graph Battery Surface Temperature", "Graph Temperature of Terminals and Core"])

# ฟังก์ชันแสดงภาพจากโฟลเดอร์
def display_image(temperature, graph_type, custom_folder=None):
    if custom_folder:
        image_folder = custom_folder
    else:
        image_folder = r"F:\st\Projectfinall"  # ใช้ r-string เพื่อหลีกเลี่ยงปัญหา path
    image_file = f"{graph_type}_{temperature}_degC.png"  # รูปแบบชื่อไฟล์ เช่น graphTemperature_25_degC.png
    image_path = os.path.join(image_folder, image_file)
    
    if os.path.exists(image_path):
        st.image(image_path, caption=f"Graph for {temperature}°C - {graph_type}", width=900)
    else:
        st.error(f"No graph available for {graph_type} at {temperature}°C!")

# กรณีเลือกหน้า "Home"
if menu == "Home":
    # Layout หลัก
    col1, col2 = st.columns([2, 1])  # กำหนดคอลัมน์ (ซ้าย: กราฟ, ขวา: อธิบาย)

    with col1:
        # กล่องสำหรับแสดงกราฟ
        st.subheader("Graph: Cell potential and load")
        graph_placeholder = st.empty()  # Placeholder สำหรับกราฟ

    with col2:
        # ส่วนอธิบาย
        st.subheader("Explain")
        st.text_area("Graph Cell potential and load", "Explain the graph here.", height=600)

    # คอลัมน์ล่างสำหรับการป้อนอุณหภูมิและแสดงภาพ
    col3, col4 = st.columns([1, 1])

    with col3:
        # กรอกอุณหภูมิ
        st.subheader("Enter Temperature")
        temperature = st.number_input("Temperature (°C)", value=25, step=1)

    with col4:
        # ปุ่ม Predict
        st.subheader("Predict")
        if st.button("Click"):
            with col1:
                st.write(f"Displaying graph for {temperature}°C...")
                display_image(temperature, "Temperature and flow")

# กรณีเลือกหน้าอื่นๆ เช่น "Graph Temperature and flow"
elif menu == "Graph Temperature and flow":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Graph Temperature and flow")
        temperature = st.number_input("Enter Temperature (°C):", key="temp_flow", value=25, step=1)
        if st.button("Show Graph", key="flow_btn"):
            display_image(temperature, "Temperature and flow")

    with col2:
        st.subheader("Explain")
        st.text_area("Graph Temperature and flow", "Explain the graph here.", height=600)

elif menu == "Graph Temperature change and load":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Graph Temperature change and load")
        temperature = st.number_input("Enter Temperature (°C):", key="temp_change", value=25, step=1)
        if st.button("Show Graph", key="change_btn"):
            display_image(temperature, "Temperature change and load")

    with col2:
        st.subheader("Explain")
        st.text_area("Graph Temperature change and load", "Explain the graph here.", height=600)

elif menu == "Graph Battery Surface Temperature":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Graph Battery Surface Temperature")
        temperature = st.number_input("Enter Temperature (°C):", key="temp_surface", value=25, step=1)
        if st.button("Show Graph", key="surface_btn"):
            display_image(temperature, "Battery Surface Temperature", custom_folder=r"F:\st\Projectfinall\Dataset\3 cycle\Battery Surface Temperature\Graphs")

    with col2:
        st.subheader("Explain")
        st.text_area("Graph Battery Surface Temperature", "Explain the graph here.", height=600)

elif menu == "Graph Temperature of Terminals and Core":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Graph Temperature of Terminals and Core")
        temperature = st.number_input("Enter Temperature (°C):", key="temp_core", value=25, step=1)
        if st.button("Show Graph", key="core_btn"):
            display_image(temperature, "Temperature of Terminals and Core", custom_folder=r"F:\st\Projectfinall\Dataset\3 cycle\Temperature of Terminals and Core\Graphs")

    with col2:
        st.subheader("Explain")
        st.text_area("Graph Temperature of Terminals and Core", "Explain the graph here.", height=600)
