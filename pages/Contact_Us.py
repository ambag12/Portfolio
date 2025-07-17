import os
import streamlit as st
import base64

st.set_page_config(page_title="Contact Me", layout="wide")
st.header("📬 Contact Me")
st.markdown("### 🧭 Reach me via:")

def contact_row(icon_path, label, href):
    # Normalize href to ensure it's absolute
    if not any(href.startswith(prefix) for prefix in ("http://", "https://", "mailto:", "tel:")):
        href = "https://" + href

    # Load & encode icon
    if not os.path.exists(icon_path):
        st.warning(f"Icon not found: {icon_path}")
        return

    with open(icon_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    img_html = (
        f'<img src="data:image/png;base64,{b64}" '
        f'width="50" style="vertical-align:middle; margin-right:10px;" />'
    )

    link_html = f'<a href="{href}" target="_blank">{img_html}{label}</a>'
    st.markdown(link_html, unsafe_allow_html=True)

# Usage:
contact_row(
    icon_path="images/linkedin.png",
    label="Connect on LinkedIn",
    href="www.linkedin.com/in/ahmed-mujtaba-baig"
)

st.markdown("---")

# Phone / WhatsApp
contact_row(
    icon_path="images/call.png",
    label="+92 302424221",
    href="tel:03302424221"
)

st.markdown("---")

# Gmail
contact_row(
    icon_path="images/email.png",
    label="Send me an email",
    href="mailto:ambaigbaig@gmail.com"
)

st.markdown("_Click any icon or label above to start your preferred contact method._")
