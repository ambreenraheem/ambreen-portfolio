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
st.markdown(f"""
<div style="flex: 1; min-width: 300px;">
    <!-- Hero name — large Playfair Display heading -->
    <h4 style="font-family: 'Playfair Display', serif; text-align:center; font-size: 2rem; color: #FFFFFF; margin-bottom: 16px;">Blogs & Sessions</h4>
</div>
""", unsafe_allow_html=True)

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
# Second placeholder session card — owner replaces with real content
st.markdown("""
<div class="content-card card-left-accent" style="max-width: 800px; margin: 0 auto 20px;">
    <h3 class="card-title">Navigating Computer Science in the Age of AI</h3>
    <p style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 0.85rem; margin-bottom: 10px;">
        📅 [January-2026] — [Physical Session at The Sufi Institute, Lauri Sharif, Sindh, Pakistan]
    </p>
    <p class="card-desc">
        <h5 class="card-title">Session Conducted By AMBREEN ABDUL RAHEEM (THE EDUCATION EXPERT)</h5>
        A discussion on how AI is reshaping computer science education and careers, and how students can prepare for the future.
        I shared my insights on the latest trends in AI, the skills that are in demand, and how students can leverage AI to enhance their learning and career prospects.
        The session recording is available on YouTube.
    </p>
    <a href="https://youtu.be/Xi5YfJKhqsQ?si=4XxbNKtnYYfGCj9l" style="color: #00D4C8; text-decoration: none; font-size: 0.9rem;">
        Watch Session →
    </a>
</div>
""", unsafe_allow_html=True)  # Render session card HTML

# --- Session Card 2 ---
# A card with teal left border, navy background, placeholder content — owner replaces with real session details

st.markdown("""
<div class="content-card card-left-accent" style="max-width: 800px; margin: 0 auto 20px;">
    <!-- Session title — white text -->
    <h3 class="card-title">How I Turned Skills into a Freelance Career on Upwork</h3>
    <!-- Session date — teal colored, small text -->
    <p style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 0.85rem; margin-bottom: 10px;">
        📅 [May-2025] — [Online Session with CRUX INTERNATIONAL CANADA]
    </p>
    <!-- Session description — soft white text -->
    <p class="card-desc">
        <h5 class="card-title">Session Conducted By AMBREEN ABDUL RAHEEM (THE FREELANCING EXPERT)</h5>
        I shared my journey of building a freelance career on Upwork, from landing my first client to scaling my business. I discussed the strategies I used to find clients, deliver high-quality work, and build long-term relationships. I also shared tips on how to create a compelling profile, write winning proposals, and negotiate rates. 
    </p>
    <!-- Optional link to session recording or materials -->
    <a href="https://youtu.be/Z-PZZTe1vvk?si=to3USR2tFGACiFhl" style="color: #00D4C8; text-decoration: none; font-size: 0.9rem;">
        Watch Session →
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
st.markdown("""
<div class="content-card card-left-accent" style="max-width: 800px; margin: 0 auto 20px;">
    <h3 class="card-title">Interactive Science Learning for Kids</h3>
    <p style="color: #00D4C8; font-family: 'Inter', sans-serif; font-size: 0.85rem; margin-bottom: 10px;">
        📅 [March - 2026] - [Science E-Book. / . AGE: 6 to 10]
    </p>
    <p class="card-desc">
        <h5 class="card-title">Authored By AMBREEN ABDUL RAHEEM (THE EDUCATION EXPERT)</h5>
        In today’s rapidly evolving high-tech world, many aspects of life have become digitalized, and education is no exception. 
        Around the world, modern learning methods are transforming how children understand and explore new concepts. 
        However, in many parts of Pakistan, digital learning is still limited. Most educational environments focus mainly on 
        traditional methods or simple online classes, and in early classrooms children often only watch rhymes or poems on screens.
    </p>
    <p class="card-desc">
        In contrast, many international education systems have fully digitalized their learning materials and curriculum. 
        These modern approaches use interactive visuals, engaging activities, and child-friendly explanations that help 
        children understand concepts more effectively and develop curiosity for learning.
    </p>
    <p class="card-desc">
        Inspired by this modern approach, and built on more than <strong>15 years of educational experience</strong>, 
        I have developed a fully informative and interactive <strong>Science E-Book for young learners</strong>. 
        This book is designed to make science simple, engaging, and enjoyable for children.
    </p>
    <p class="card-desc">
        Instead of long and difficult explanations, the e-book focuses on visual learning, interactive ideas, 
        and easy-to-understand concepts that keep children curious and motivated.
    </p>
    <p class="card-desc"><strong>This e-book helps children:</strong></p>
    <ul style="font-family: 'Inter', sans-serif; font-size: 0.95rem; line-height: 1.6;">
        <li>Understand basic science concepts in a simple and enjoyable way</li>
        <li>Learn through interactive activities and visual explanations</li>
        <li>Develop curiosity, creativity, and critical thinking skills</li>
        <li>Experience science as an exciting adventure rather than a difficult subject</li>
    </ul>
    <p class="card-desc">
        Parents can also sit with their children and explore the book together, turning learning into a shared and enjoyable 
        experience at home.
    </p>
    <p class="card-desc">
        If you want your child to learn science in a fun, modern, and engaging way, this <strong>Science E-Book</strong> 
        can become a wonderful companion in their early learning journey.
    </p>
    <p class="card-desc">
        Give your child the joy of discovering science through interactive digital learning. 📚✨
    </p>
    <a href="https://science-e-book-01.streamlit.app/" style="color: #00D4C8; text-decoration: none; font-size: 0.9rem;">
        Read & Explore: SCIENCE-E-BOOK→
    </a>
</div>
""", unsafe_allow_html=True)
