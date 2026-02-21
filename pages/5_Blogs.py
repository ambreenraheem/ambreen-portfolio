# ============================================================
# 5_Blogs.py — Blogs & Sessions Page
# Displays session entries and informative blog posts as cards
# with a teal left border accent. Owner replaces placeholders.
# ============================================================

import streamlit as st  # Import Streamlit framework

# --- Page Config ---
# Configure browser tab title, icon, and layout for this page
st.set_page_config(
    page_title="Blogs | Ambreen Abdul Raheem",  # Browser tab title
    page_icon="📝",                               # Blog emoji favicon
    layout="wide",                                # Full-width layout
    initial_sidebar_state="expanded"             # Sidebar visible by default
)

def load_css():
    """Load the global CSS file for consistent styling."""
    try:
        with open("assets/style.css", "r") as f:  # Open global stylesheet
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  # Inject CSS
    except FileNotFoundError:
        pass  # Continue if CSS file is missing

# Apply global CSS styles
load_css()

# ============================================================
# PAGE HEADING
# ============================================================

# Main heading — "Blogs & Sessions" styled with Playfair Display
st.markdown('<h2 class="section-heading">Blogs & Sessions</h2>', unsafe_allow_html=True)

# ============================================================
# SUBSECTION 1: SESSIONS I CONDUCTED
# Cards with teal left border accent for each session entry
# ============================================================

# Subsection heading for sessions — teal colored, centered
st.markdown("""
<h3 style="
    font-family: 'Playfair Display', serif;
    color: #00D4C8;
    font-size: 1.5rem;
    margin: 30px 0 20px;
    text-align: center;
">Sessions I Conducted</h3>
""", unsafe_allow_html=True)  # Render subsection heading

# --- Session Card 1 ---
# A card with teal left border, navy background, placeholder content
st.markdown("""
<div class="content-card card-left-accent" style="max-width: 800px; margin: 0 auto 20px;">
    <!-- Session title — white text -->
    <h3 class="card-title">Introduction to Power BI for Beginners</h3>
    <!-- Session date — teal colored, small text -->
    <p style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 0.85rem; margin-bottom: 10px;">
        📅 [Date] — [Location/Platform]
    </p>
    <!-- Session description — soft white text -->
    <p class="card-desc">
        Conducted a hands-on session introducing Power BI fundamentals,
        including data import, basic visualizations, and dashboard creation.
    </p>
    <!-- Optional link to session recording or materials -->
    <a href="#" style="color: #00D4C8; text-decoration: none; font-size: 0.9rem;">
        View Details →
    </a>
</div>
""", unsafe_allow_html=True)  # Render session card HTML

# --- Session Card 2 ---
# Second placeholder session card — owner replaces with real content
st.markdown("""
<div class="content-card card-left-accent" style="max-width: 800px; margin: 0 auto 20px;">
    <h3 class="card-title">Python for Data Analysis Workshop</h3>
    <p style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 0.85rem; margin-bottom: 10px;">
        📅 [Date] — [Location/Platform]
    </p>
    <p class="card-desc">
        Led a workshop on using Python libraries (Pandas, NumPy, Matplotlib)
        for data cleaning, analysis, and visualization.
    </p>
    <a href="#" style="color: #00D4C8; text-decoration: none; font-size: 0.9rem;">
        View Details →
    </a>
</div>
""", unsafe_allow_html=True)  # Render session card HTML

# --- Horizontal separator between subsections ---
st.markdown("<hr style='border-color: #1E3A5F; margin: 40px 0;'>", unsafe_allow_html=True)

# ============================================================
# SUBSECTION 2: INFORMATIVE POSTS
# Blog post cards with teal left border accent
# ============================================================

# Subsection heading for informative blog posts
st.markdown("""
<h3 style="
    font-family: 'Playfair Display', serif;
    color: #00D4C8;
    font-size: 1.5rem;
    margin: 30px 0 20px;
    text-align: center;
">Informative Posts</h3>
""", unsafe_allow_html=True)  # Render subsection heading

# --- Blog Post Card 1 ---
# Placeholder blog post — owner replaces with real content
st.markdown("""
<div class="content-card card-left-accent" style="max-width: 800px; margin: 0 auto 20px;">
    <h3 class="card-title">5 Power BI Tips Every Analyst Should Know</h3>
    <p style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 0.85rem; margin-bottom: 10px;">
        📅 [Date]
    </p>
    <p class="card-desc">
        Essential tips for getting the most out of Power BI — from DAX formulas
        to custom visuals and performance optimization techniques.
    </p>
    <a href="#" style="color: #00D4C8; text-decoration: none; font-size: 0.9rem;">
        Read More →
    </a>
</div>
""", unsafe_allow_html=True)  # Render blog post card HTML
