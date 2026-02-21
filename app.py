# ============================================================
# app.py — Main Entry Point for the Portfolio Streamlit App
# This file configures the page settings and loads the global CSS.
# Streamlit uses this as the entry point; pages/ folder holds sub-pages.
# ============================================================

import streamlit as st  # Import Streamlit — the web framework for the entire app
import os
import base64


def get_image_base64(image_path):
    """Read an image file and return its base64-encoded string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


# --- Page Configuration ---
# Must be the first Streamlit command in the script
# Sets the browser tab title, icon, layout width, and collapsed sidebar
st.set_page_config(
    page_title="Ambreen Abdul Raheem | Portfolio",  # Browser tab title
    page_icon="🌐",                                  # Favicon emoji shown in browser tab
    layout="wide",                                   # Use full-width layout (not centered narrow)
    initial_sidebar_state="expanded"                # Start with sidebar visible
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
    """Load the global custom CSS file (assets/style.css) into the app.
    This injects all custom styles (navbar, hero, cards, etc.) into every page."""
    try:
        # Open and read the CSS file from the assets folder
        with open("assets/style.css", "r") as css_file:
            css_content = css_file.read()  # Read entire CSS file content as a string
        # Inject the CSS into the page using a <style> HTML tag via st.markdown
        # unsafe_allow_html=True is required to render raw HTML/CSS
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # If style.css is missing, silently pass — the app still works without custom styles
        pass

# Call the CSS loader function to apply styles on app load
load_css()

# --- Landing Page Content ---
# This appears when the user first visits the root URL (before selecting a page)
# It acts as a welcome/redirect to the Home page

# Inject centered welcome message styled with the design system
st.markdown("""
<div style="
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 80vh;
    text-align: center;
">
    <!-- Welcome heading using Playfair Display font in white -->
    <h1 style="
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: #FFFFFF;
        margin-bottom: 16px;
    ">Welcome to My Portfolio</h1>
    <!-- Subtitle using Inter font in soft white -->
    <p style="
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #CBD5E1;
        margin-bottom: 30px;
    ">Navigate using the sidebar to explore pages</p>
    <!-- Instruction text pointing to sidebar navigation -->
    <p style="
        font-family: 'Inter', sans-serif;
        color: #00D4C8;
        font-size: 1rem;
    ">Hi, I'm Ambreen Abdul Raheem. Want to explore my work?</p>
</div>
""", unsafe_allow_html=True)  # unsafe_allow_html allows raw HTML rendering
