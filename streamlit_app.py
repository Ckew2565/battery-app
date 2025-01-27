import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ตั้งค่าหน้า Streamlit
st.set_page_config(page_title="Heat Distribution in Battery Cells", layout="wide")

# ส่วนหัวของแอป
st.title("Prediction of Heat Distribution in Battery Cells for Electric Vehicles")

# แบ่ง layout ออกเป็นสองคอลัมน์
col1, col2 = st.columns([2, 1])

# คอลัมน์แรก: แสดงกราฟ
with col1:
    st.subheader("Cell potential and load")
    
    # โหลดข้อมูลตัวอย่าง (แก้ไขให้เป็น path ของไฟล์ CSV)
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())  # แสดงตัวอย่างข้อมูล
        
        # ตัวอย่างการพล็อตกราฟ
        fig, ax1 = plt.subplots()
        
        ax2 = ax1.twinx()
        ax1.plot(data["Time"], data["Cell Potential"], 'g-')
        ax2.plot(data["Time"], data["Battery Load"], 'b-')
        
        ax1.set_xlabel("Time (s)")
        ax1.set_ylabel("Cell Potential (V)", color='g')
        ax2.set_ylabel("Battery Load (C-rate)", color='b')
        
        plt.title("Cell potential and load")
        st.pyplot(fig)

# คอลัมน์ที่สอง: อธิบายกราฟและปุ่ม
with col2:
    st.subheader("Explain")
    st.text_area("Graph Explanation", "Explain Cell potential and load")
    
    # ส่วนรับค่า Temperature
    st.subheader("Enter Temperature")
    temperature = st.number_input("Temperature (°C)", value=25, step=1)
    
    # ปุ่ม predict
    if st.button("Predict"):
        st.write(f"Prediction for {temperature}°C is under calculation...")

# ส่วนท้าย
st.write("---")
st.caption("Developed by Walailak University")
