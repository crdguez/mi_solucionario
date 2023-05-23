import streamlit as st
import base64
import os

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



st.title('Ejercicios de Matemáticas')

show_pdf('ecuaciones.pdf')

st.download_button(label="Descargar fichero", 
        data=open("ecuaciones.pdf", "rb").read(),
        file_name="ecuaciones.pdf",
        mime='application/octet-stream')

# files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
files = [f for f in os.listdir('.') if f.endswith('.pdf')]
st.write(files)
