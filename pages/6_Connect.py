# ============================================================
# 6_Connect.py — Connect / Contact Page
# Uses requests library instead of supabase — works on Python 3.13
# ============================================================

import streamlit as st   # Streamlit framework
import requests

# Built-in HTTP library — no extra install needed
# --- Page Config ---
st.set_page_config(
    page_title="Connect | Ambreen Abdul Raheem",
    page_icon="📬",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    """Load global CSS for consistent styling."""
    try:
        with open("assets/style.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()  # Apply styles

# ============================================================
# SUPABASE CONNECTION — Using requests (no supabase library)
# ============================================================

def save_to_supabase(name, email, message):
    """
    Send contact form data directly to Supabase REST API.
    Uses requests library only — no supabase module needed.
    """
    # Check if secrets exist (prevents crash on Streamlit Cloud)
    if "supabase" not in st.secrets:
        st.error("❌ Configuration Error: Supabase secrets are missing.")
        st.info("💡 If you are on Streamlit Cloud, please add your secrets in the App Settings dashboard.")
        return False

    # Build the full URL to your contacts table
    url = st.secrets["supabase"]["url"] + "/rest/v1/Connect"

    # Get the anon key from secrets
    key = st.secrets["supabase"]["key"]

    # Required headers for Supabase REST API
    headers = {
        "apikey": key,                       # API key header
        "Authorization": f"Bearer {key}",    # Bearer token for auth
        "Content-Type": "application/json",  # We are sending JSON data
        "Prefer": "return=minimal"           # Don't return the inserted row
    }

    # Data to insert into the table
    data = {
        "name": name,        # Name column
        "email": email,      # Email column
        "message": message   # Message column
    }

    # Send POST request to Supabase
    response = requests.post(url, json=data, headers=headers)
    # st.write("Status:", response.status_code)
    # st.write("Response:", response.text) error maloom krne kliye
    # Return True if successfully inserted (status 201)
    return response.status_code == 201

# ============================================================
# PAGE CONTENT — TWO COLUMN LAYOUT
# ============================================================

col1, col2 = st.columns([1, 1], gap="large")

with col1:
# ============================================================
# SOCIAL LINKS (Left Side)
# ============================================================
    st.markdown(f"""
    <h3 style="font-family: 'Playfair Display', serif; color: #FFFFFF;
               font-size: 1.5rem; text-align: left; margin-bottom: 20px;">
        Connect & Collaborate
    </h3>
    <p style="font-size: 1.1rem; color: #E0E0E0; line-height: 1.6; text-align: left;">
        Hi, I'm <strong>Ambreen Abdul Raheem</strong>. I specialize in bridging the gap between complex data challenges and actionable AI solutions. 
        Whether you need <strong>end-to-end web application development</strong>, <strong>advanced data analytics</strong>, or <strong>custom machine learning models</strong>, 
        I am here to help you turn your vision into reality. Let's connect to discuss how we can drive meaningful impact together.
    </p>
    <div style="margin: 25px 0;">
        <h4 style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 1.2rem;">Services Offered:</h4>
        <ul style="color: #E0E0E0; font-size: 1rem; line-height: 1.5;">
            <li>Custom Web App Development (Python, Streamlit, React)</li>
            <li>Advanced Data Visualization & Business Intelligence</li>
            <li>Machine Learning & Predictive Modeling</li>
            <li>API Integration & Backend Optimization</li>
        </ul>
        Email: ambreen.upwork.27@gmail.com
        Email: ambreen.a.raheem@outlook.com
    </div>
    """, unsafe_allow_html=True)

with col2:
    # ============================================================
    # CONTACT FORM (Right Side)
    # ============================================================
    st.markdown("""
    <h3 style="font-family: 'Playfair Display', serif; text-align:left; font-size: 1.5rem; color: #FFFFFF; margin-bottom: 20px;">
        Get In Touch
    </h3>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):   # Clear fields after submit
        name    = st.text_input("Your Name",    placeholder="Enter your name")             # Name field
        email   = st.text_input("Your Email",   placeholder="Enter your email address")    # Email field
        message = st.text_area("Your Message",  placeholder="Write your message here...",  # Message field
                               height=150)
        submitted = st.form_submit_button("Send Message")   # Submit button

        if submitted:                           # When button is clicked
            if name and email and message:      # All fields must be filled
                success = save_to_supabase(name, email, message)   # Send to Supabase
                if success:
                    st.success("✅ Thank you! Your message has been received.")
                else:
                    st.error("❌ Something went wrong. Please try again.")
            else:
                st.warning("⚠️ Please fill in all fields before submitting.")

# --- Bottom Divider ---
st.markdown("<hr style='border-color: #1E3A5F; margin: 20px 0 10px 0;'>", unsafe_allow_html=True)

# ============================================================
# SOCIAL LINKS (Bottom Centered)
# ============================================================
st.markdown(f"""
<div style="text-align: center; width: 100%;">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Social media icon links row — Centered at bottom -->
    <div class="social-links" style="display: flex; flex-direction: row; flex-wrap: wrap; gap: 30px; align-items: center; justify-content: center; width: 100%; margin-top: 10px;">
        <a href="https://www.upwork.com/freelancers/~01d2856ced28d8eca8?s=1110580752008335360" target="_blank" title="Upwork"><i class="fa-brands fa-upwork"></i> Upwork</a>
        <a href="https://www.linkedin.com/in/ambreen-abdul-raheem-122509300/" target="_blank" title="LinkedIn"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
        <a href="https://github.com/Ambreen-AbdulRaheem" target="_blank" title="GitHub"><i class="fa-brands fa-github"></i> GitHub</a>
        <a href="https://www.youtube.com/@AmbreenAbdulRaheem-y8m" target="_blank" title="YouTube"><i class="fa-brands fa-youtube"></i> YouTube</a>
        <a href="https://www.facebook.com/profile.php?id=61557898913923" target="_blank" title="Facebook"><i class="fa-brands fa-facebook"></i> Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)
