import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Generator", layout="centered")

st.title("🔳 QR Code Generator")

# ---------------- SESSION STORAGE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- INPUT ----------------
data = st.text_input("Enter your link")

# ---------------- GENERATE ----------------
if st.button("Generate QR"):
    if data:
        qr = qrcode.make(data)

        buf = BytesIO()
        qr.save(buf, format="PNG")

        st.image(buf.getvalue(), caption="Your QR Code")

        # Save history
        st.session_state.history.append({
            "link": data,
            "image": buf.getvalue()
        })

        # Download button
        st.download_button(
            label="⬇️ Download QR",
            data=buf.getvalue(),
            file_name="qr_code.png",
            mime="image/png"
        )

    else:
        st.warning("Please enter a link")

# ---------------- HISTORY ----------------
st.subheader("📜 Recent QR Codes")

if st.session_state.history:
    for i, item in enumerate(reversed(st.session_state.history)):
        st.write(f"🔗 {item['link']}")
        st.image(item["image"], width=150)

        st.download_button(
            label=f"Download #{i+1}",
            data=item["image"],
            file_name=f"qr_{i+1}.png",
            mime="image/png",
            key=i
        )
else:
    st.write("No QR codes generated yet")
