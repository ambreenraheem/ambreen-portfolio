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
def load_profile_image(image_path, fallback_color="#132952"):
    """Load image and return complete data URI (not just raw base64)."""
    if not os.path.exists(image_path):
        return f"https://via.placeholder.com/280x280/{fallback_color[1:]}/00D4C8?text=IMG"
    
    ext = os.path.splitext(image_path)[1].lower()
    mime_map = {".png": "image/png", ".jpg": "image/jpeg", 
                ".jpeg": "image/jpeg", ".gif": "image/gif", ".webp": "image/webp"}
    mime = mime_map.get(ext, "image/jpeg")  # Extension se correct MIME type
    
    with open(image_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode("utf-8")
    
    return f"data:{mime};base64,{b64}"  # ✅ Complete data URI return ho raha hai  # Fallback placeholder

# --- Load Images ---
# Load images from assets folder and convert to base64 for embedding
profile_src = load_profile_image("assets/Profile.jpeg")
image1_src = load_profile_image("assets/the_sufi_post.png")
image2_src = load_profile_image("assets/nishat.jpeg")
image3_src = load_profile_image("assets/The_Sufi_Institute1.jpeg")
image4_src = load_profile_image("assets/crux_post.jpg")


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
st.markdown(f"""
<div style="
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 80vh;
    text-align: center;
">
    <img src="{profile_src}" alt="Profile" style="width: 160px; height: 160px; border-radius: 50%; object-fit: cover; border: 2px solid #00D4C8; box-shadow: 0 8px 32px rgba(0, 212, 200, 0.3);" alt="Ambreen Abdul Raheem">
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
    <!--2x2 image grid-->
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px;">
<!-- Image-1 -->
    <img src="{image1_src}" alt="The Sufi Post" style="
    width: 600px; 
    height: 300px; 
    border-radius: 12px; 
    object-fit: cover; 
    border: 2px solid #1e3a5f; 
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
<!-- Image-2 -->    
    <img src="{image2_src}" alt="Nishat" style="
    width: 600px;
    height: 300px;
    border-radius: 12px; 
    object-fit: cover; 
    border: 2px solid #1e3a5f; 
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
<!-- Image-3 -->
    <img src="{image3_src}" alt="The Sufi Institute" style="
    width: 600px;
    height: 300px; 
    border-radius: 12px; 
    object-fit: cover; 
    border: 2px solid #1e3a5f; 
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
<!-- Image-4 -->
    <img src="{image4_src}" alt="Crux Post" style="
    width: 300px;
    height: 300px; 
    border-radius: 12px; 
    object-fit: cover;
    border: 2px solid #1e3a5f; 
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
</div>
""", unsafe_allow_html=True)  # unsafe_allow_html allows raw HTML rendering
