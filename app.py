import streamlit as st
import qrcode
from io import BytesIO

st.title("🔳 QR Code Generator")

data = st.text_input("Enter your link")

if st.button("Generate QR"):
    if data:
        qr = qrcode.make(data)
        
        buf = BytesIO()
        qr.save(buf, format="PNG")
        
        st.image(buf.getvalue())
    else:
        st.warning("Enter a link")
