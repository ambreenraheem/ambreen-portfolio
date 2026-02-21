# ============================================================
# 1_Home.py — Home Page: Hero Section, Stats Bar, Tool Cards, CTA Banner
# This is the main landing page of the portfolio website.
# It includes the hero with animated avatar, stats strip, tool cards, and a CTA.
# ============================================================

import streamlit as st  # Import Streamlit for building the page UI
import base64           # Import base64 for encoding the profile image to embed in HTML
import os               # Import os for file path operations

def get_image_base64(image_path):
    """Read an image file and return its base64-encoded string.
    This allows embedding the image directly in HTML via a data URI."""
    with open(image_path, "rb") as img_file:          # Open image in binary read mode
        return base64.b64encode(img_file.read()).decode()  # Encode to base64 and decode to string



# --- Page Config ---
# Set the browser tab title and icon for this specific page
st.set_page_config(
    page_title="Home | Ambreen Abdul Raheem",  # Browser tab title for this page
    page_icon="🏠",                             # Home emoji as favicon
    layout="wide",                              # Full-width page layout
    initial_sidebar_state="expanded"           # Sidebar starts visible
)

# Build the base64 data URI for the profile image
# This embeds the actual Profile.jpeg from assets/ into the HTML
profile_img_path = "assets/Profile.jpeg"  # Path to the real profile photo
if os.path.exists(profile_img_path):  # Check the image file exists
    profile_b64 = get_image_base64(profile_img_path)  # Encode image to base64
    profile_src = f"data:image/jpeg;base64,{profile_b64}"  # Create data URI for HTML img src
else:
    profile_src = "https://via.placeholder.com/280x280/132952/00D4C8?text=AR"  # Fallback placeholder


def load_css():
    """Load global CSS into this page.
    Each page must load CSS independently since Streamlit re-renders per page."""
    try:
        with open("assets/style.css", "r") as f:  # Open the global stylesheet
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  # Inject CSS
    except FileNotFoundError:
        pass  # Silently continue if CSS file is missing

# Apply the global CSS styles to this page
load_css()


# ============================================================
# HERO SECTION — Full viewport landing area with two-column layout
# ============================================================

# Inject the hero section HTML
# Left column: role tag, name, tagline, CTA buttons, social links
# Right column: animated avatar circle with glowing teal ring
st.markdown(f"""
<div class="hero-section" id="hero">
    <div class="hero-container">
        <!-- LEFT COLUMN: Text content -->
        <div class="hero-text">
            <!-- Role label tag — small teal badge above the name -->
            <div class="role-tag">Data Analyst & Web App Developer</div>
            <!-- Hero name — large Playfair Display heading -->
            <h1 class="hero-name">Ambreen<br>Abdul Raheem</h1>
            <!-- Tagline — subtitle in Inter font, soft white color -->
            <p class="hero-tagline">Turning Data into Decisions | Power BI | Python | Web Apps</p>
            <!-- Font Awesome CDN for real social icons -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
            <!-- Social media icon links row — teal on hover -->
            <div class="social-links">
                <a href="https://www.upwork.com/freelancers/~01d2856ced28d8eca8?s=1110580752008335360" target="_blank" title="Upwork"><i class="fa-brands fa-upwork"></i> Upwork</a>
                <a href="https://www.linkedin.com/in/ambreen-abdul-raheem-122509300/" target="_blank" title="LinkedIn"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
                <a href="https://github.com/Ambreen-AbdulRaheem" target="_blank" title="GitHub"><i class="fa-brands fa-github"></i> GitHub</a>
                <a href="https://www.youtube.com/@AmbreenAbdulRaheem-y8m" target="_blank" title="YouTube"><i class="fa-brands fa-youtube"></i> YouTube</a>
                <a href="https://www.facebook.com/profile.php?id=61557898913923" target="_blank" title="Facebook"><i class="fa-brands fa-facebook"></i> Facebook</a>
            </div>
        </div>
        <!-- RIGHT COLUMN: Animated avatar with glow ring -->
        <div class="hero-avatar">
            <!-- Circle container with CSS glow pulse animation -->
            <div class="avatar-circle">
                <!-- Profile image — loaded from assets/Profile.jpeg -->
                <img src="{profile_src}" alt="Ambreen Abdul Raheem">
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)  # Render the hero HTML directly

# ============================================================
# TOOLS & TECHNOLOGIES — Four icon + label cards
# ============================================================

# Section heading for tools
st.markdown('<h2 class="section-heading">Tools & Technologies</h2>', unsafe_allow_html=True)

# Inject four tool cards in a flex row
# Each card: Font Awesome icon + label text, teal glow on hover via CSS
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<div class="tool-cards">
    <!-- Card 1: Power BI — data visualization tool -->
    <div class="tool-card">
        <div class="tool-icon"><i class="fa-solid fa-chart-column"></i></div>
        <div class="tool-label">Power BI</div>
    </div>
    <!-- Card 2: Python — primary programming language -->
    <div class="tool-card">
        <div class="tool-icon"><i class="fa-brands fa-python"></i></div>
        <div class="tool-label">Python</div>
    </div>
    <!-- Card 3: SQL — database querying language -->
    <div class="tool-card">
        <div class="tool-icon"><i class="fa-solid fa-database"></i></div>
        <div class="tool-label">SQL</div>
    </div>
    <!-- Card 4: Web Apps — web application development -->
    <div class="tool-card">
        <div class="tool-icon"><i class="fa-solid fa-globe"></i></div>
        <div class="tool-label">Web Apps</div>
    </div>
    <!-- Card 5: Streamlit — FA icon nahi hai, isliye official SVG logo use kiya -->
    <div class="tool-card">
        <div class="tool-icon">
            <!-- Streamlit ka official logo SVG — seedha brand site se liya gaya -->
            <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg"
                 alt="Streamlit"
                 style="width:40px; height:40px; object-fit:contain;">
        </div>
        <div class="tool-label">Streamlit</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CTA BANNER — Call-to-action strip at the bottom of the Home page
# ============================================================

# Full-width gradient banner with a hiring call-to-action
st.markdown("""
<div class="cta-banner">
    <!-- CTA heading text — Playfair Display, white -->
    <h2>Let's Work Together — Open for Freelance Projects</h2>
    <!-- CTA button — white background, navy text, links to Upwork -->
    <a href="https://www.upwork.com/freelancers/~01d2856ced28d8eca8?s=1110580752008335360" class="cta-btn">Hire Me on Upwork</a>
</div>
""", unsafe_allow_html=True)  # Render the CTA banner HTML
