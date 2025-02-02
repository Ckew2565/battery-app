import streamlit as st
import os

# ตั้งค่าหน้า Streamlit
st.set_page_config(page_title="Battery Cell Heat Prediction", layout="wide")

# ส่วนหัวของหน้า
st.markdown(
    "<h1 style='text-align: center;'> Heat Distribution in Battery Cells for Electric Vehicles</h1>",
    unsafe_allow_html=True,
)

# ฟังก์ชันแสดงภาพจากโฟลเดอร์
def display_image(temperature):
    image_folder = r"F:\st\Projectfinall\web\battery-app\imagescellpotential"  # ใช้ r-string เพื่อหลีกเลี่ยงปัญหา path
    image_file = f"{temperature}_degC.png"  # รูปแบบชื่อไฟล์ เช่น 25_degC.png
    image_path = os.path.join(image_folder, image_file)
    if os.path.exists(image_path):
        st.image(image_path, caption=f"Graph for {temperature}°C", width=900)
    else:
        st.error("No graph available for this temperature!")

# Layout หลัก
col1, col2 = st.columns([2, 1])  # กำหนดคอลัมน์ (ซ้าย: กราฟ, ขวา: อธิบาย)

with col1:
    # กล่องสำหรับแสดงกราฟ
    st.subheader("Graph: Temperature")
    graph_placeholder = st.empty()  # Placeholder สำหรับกราฟ

with col2:
    # ส่วนอธิบาย
    st.subheader("Explain")
    st.text_area("Graph Temperature", "Battery heat dissipation is in the temperature range of 28.9°C to 29.9°C", height=600)

# คอลัมน์ล่างสำหรับการป้อนอุณหภูมิและแสดงภาพ
col3, col4 = st.columns([1, 1])

with col3:
    # กรอกอุณหภูมิ
    st.subheader("Enter Temperature")
    temperature = st.number_input("Temperature (°C)", value=25, step=1)

with col4:
    # ปุ่ม Predict
    st.subheader("View")
    if st.button("Click"):
        with col1:
            st.write(f"Displaying graph for {temperature}°C...")
            display_image(temperature)
