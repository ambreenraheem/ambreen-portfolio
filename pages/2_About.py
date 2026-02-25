# ============================================================
# 2_About.py — About Page: Bio, Journey Timeline, Values, References
# NOTE: Section 2 (Animated Skill Bars) has been REMOVED per user request.
# This page contains: Bio (Section 1), Timeline (Section 3),
# Values (Section 4), and References (Section 5).
# ============================================================

import streamlit as st  # Import Streamlit framework
import base64           # Import base64 for encoding the profile image into HTML
import os               # Import os for file path checks
from PIL import Image
from pathlib import Path

def get_image_base64(image_path):
    """Read an image file and return its base64-encoded string for HTML embedding."""
    with open(image_path, "rb") as img_file:          # Open image in binary mode
        return base64.b64encode(img_file.read()).decode()  # Encode and return as string


# Build base64 data URI for the profile image from assets/Profile.png
profile_img_path = "assets/Profile.png"  # Path to the actual profile photo
if os.path.exists(profile_img_path):  # Verify the image exists
    profile_b64 = get_image_base64(profile_img_path)  # Encode to base64
    profile_src = f"data:image/png;base64,{profile_b64}"  # Create data URI
else:
    profile_src = "https://via.placeholder.com/250x250/132952/00D4C8?text=AR"  # Fallback

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


image1_path = "assets/BADSHAHKAREEM.png"
image2_path = "assets/nishat.jpeg"
image3_path = "assets/Kashif.jpg"
image4_path = "assets/titli.jpg"
image5_path = "assets/ned.jpeg"
image6_path = "assets/crux.png"
badshah_src = load_profile_image(image1_path)
nishat_src = load_profile_image(image2_path)
kashif_src = load_profile_image(image3_path)
noureen_src = load_profile_image(image4_path)
ned_src = load_profile_image(image5_path)
crux_src = load_profile_image(image6_path)





# --- Page Config ---
# Configure browser tab title, icon, and layout for this page
st.set_page_config(
    page_title="About | Ambreen Abdul Raheem",  # Browser tab title
    page_icon="assets/Profile.png",                              # About page favicon
    layout="wide",                               # Full-width layout
    initial_sidebar_state="expanded"            # Sidebar starts visible
)

def load_css():
    """Load the global CSS file to apply consistent styling across all pages."""
    try:
        with open("assets/style.css", "r") as f:  # Open the shared CSS file
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  # Inject CSS
    except FileNotFoundError:
        pass  # Continue without styles if file is missing

# Apply global styles
load_css()

# ============================================================
# SECTION 1: ABOUT ME — Bio with Profile Photo
# Two-column layout: photo on left, bio text on right
# ============================================================

# Section heading — "About Me" in Playfair Display
st.markdown(f"""
<div style="flex: 1; min-width: 300px;">
    <!-- Hero name — large Playfair Display heading -->
    <h4 style="font-family: 'Playfair Display', serif; text-align:center; font-size: 2rem; color: #FFFFFF; margin-bottom: 16px;">About Me</h4>
</div>
""", unsafe_allow_html=True)

# Inject the two-column bio section HTML
# Left: circular profile photo with teal glow border
# Right: bio paragraph text in Inter font, soft white
st.markdown(f"""
<div style="
    display: flex;
    align-items: center;
    gap: 50px;
    max-width: 1000px;
    margin: 0 auto;
    flex-wrap: wrap;
    padding: 20px;
">
    <!-- Left Column: Circular profile image with teal glow -->
    <div style="flex: 0 0 250px; display: flex; justify-content: center;">
        <!-- Profile photo — loaded from assets/Profile.jpeg -->
        <img src="{profile_src}"
             alt="Ambreen Abdul Raheem"
             class="about-profile">
    </div>
    <!-- Right Column: Bio paragraph text -->
    <div style="flex: 1; min-width: 300px;">
        <p class="bio-text">
            I am Ambreen Abdul Raheem, a passionate Data Analyst and Web App Developer
            with 4+ years of experience. I currently work at Nishat Welfare Organization
            and freelance on Upwork helping clients turn raw data into actionable insights.
            My expertise includes Power BI dashboards, Python automation, data analysis,
            and building web applications using Streamlit and modern web technologies.
        </p>
        <!-- Owner can expand or replace the above bio text with their own content -->
    </div>
</div>
""", unsafe_allow_html=True)  # Render bio section HTML

# --- Horizontal separator between bio and next section ---
st.markdown("<hr style='border-color: #1E3A5F; margin: 40px 0;'>", unsafe_allow_html=True)

# ─── Helper: convert image file to base64 src string ───────────────────────
def img_to_base64(image_path: str) -> str:
    """
    Yeh function ek image file ko base64 string mein convert karta hai
    taake hum usse HTML ke andar directly use kar sakein.
    Agar file na mile to empty string return karta hai.
    """
    path = Path(image_path)
    if path.exists():
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        ext = path.suffix.lstrip(".")          # e.g. "jpg", "png"
        return f"data:image/{ext};base64,{encoded}"
    return ""   # file nahi mili to blank return karo



# ─── Timeline HTML ───────────────────────────────────────────────────────────
timeline_html = f"""
<style>
  :root {{
    --accent: #00D4C8;
    --navy:   #132952;
  }}

  .timeline-item {{
    margin-bottom: 2rem;
  }}

  .timeline-year {{
    color: var(--accent);
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 0.5rem;
  }}

  .timeline-card {{
    background: var(--navy);
    border-left: 3px solid var(--accent);
    border-radius: 8px;
    padding: 1rem 1.25rem;
  }}

  .card-desc {{
    color: #CBD5E1;
    line-height: 1.7;
    font-size: 0.95rem;
  }}

  .card-desc a {{
    color: var(--accent);
    text-decoration: none;
  }}

  .card-desc a:hover {{
    text-decoration: underline;
  }}

  .timeline-images {{
    display: flex;
    gap: 10px;
    margin-top: 15px;
    justify-content: center;
    flex-wrap: wrap;
  }}

  .timeline-images img {{
    width: 150px;
    border-radius: 8px;
    border: 2px solid var(--accent);
    box-shadow: 0 4px 10px rgba(0,212,200,0.2);
  }}
</style>

<div class="timeline" style="max-width: 800px; margin: 0 auto;">
<!-- ── Entry 0: Graduation ─────────────────────────── -->
<div class="timeline-item">
    <div class="timeline-year"><h3>[2010] — Graduation</h3></div>
    <div class="timeline-card">
        <p class="card-desc">
        🎓 My academic background includes a Bachelor of Arts (BA) and Bachelor of Education (B.Ed), and I began my career as a school teacher. I dedicated 15 years of my life to teaching with complete passion and commitment. Alongside my school job, I also ran home-based coaching classes, where my students achieved excellent results. Now that I’ve stepped into the field of data analysis, I bring the same dedication and consistency. For the past 4 years, I’ve been working hard with focus and determination, continuously updating and upgrading my skills to stay relevant and effective in this evolving field.
        </p>
    </div>
</div>

<!-- ── Entry 1: Started as Data Analyst ─────────────────────────── -->
<div class="timeline-item">
  <div class="timeline-year"><h3>[2019] — Started as Data Analyst</h3></div>
  <div class="timeline-card">
    <p class="card-desc">
      My turning point came during the COVID-19 pandemic.
      I paused teaching and joined Nishat Welfare Organization (NWO) as a Data Entry Specialist.
      That six-month opportunity became the foundation of my data journey.
      <br>
      🚀 It was during this time that <b>His Excellency Pir Muhammad Sadiq Qureshi</b>,
      Patron-in-Chief of
      <a href="https://nishatwelfare.org/" target="_blank">The Nishat Welfare Organization (NWO)</a>,
      highlighted the organization's need for data professionals.
      Inspired, I began exploring the field of data science.
    </p>
    <!-- Images row — shown side by side after the text -->
    <!-- image of badshah kareem and nishat welfare organization -->
    <div style="display: flex; gap: 40px; margin-top: 20px; flex-wrap: wrap;object-fit: center;">
        <!-- Badshah Kareem image -->
        <img src="{badshah_src}" 
             alt="His Highness Pir Muhammad Sadiq Qureshi" 
             style="width: 300px; 
                    height: 600px; 
                    object-fit: cover; 
                    border-radius: 10px; 
                    border: 2px solid #1E3A5F;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
        <!-- Nishat Welfare Organization image -->
        <img src="{nishat_src}" 
             alt="Nishat Welfare Organization" 
             style="width: 300px; 
                    height: 300px; 
                    object-fit: cover; 
                    border-radius: 10px; 
                    border: 2px solid #1E3A5F;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
    </div>
  </div>
</div>

<!-- ── Entry 2: My Mentors ───────────────────────────────────────── -->
<div class="timeline-item">
  <div class="timeline-year"><h3>[2020] — My Mentors: Dr. Kashif Hussain &amp; TS Dr. Noureen Talpur</h3></div>
  <div class="timeline-card">
    <p class="card-desc">
      I met <b>Dr. Kashif Hussain</b> — PhD in Machine Learning &amp; Data Mining | AI/ML Researcher &amp; Educator |
      UK Global Talent | BCS &amp; ACM Member.
      Currently at University of Roehampton, London, UK.
      He is a passionate educator with a strong commitment to advancing knowledge in machine learning and data mining.
      <a href="https://www.linkedin.com/in/kashif-talpur" target="_blank">Dr. Kashif Hussain on LinkedIn</a>
      <br><br>
      <b>TS Dr. Noureen Talpur</b> — Lecturer | Professional Technologist | Researcher (Machine Learning &amp; Data Science)
      at Universiti Teknologi PETRONAS, Ipoh, Perak, Malaysia.
      <a href="https://www.linkedin.com/in/noureen-talpur" target="_blank">TS Dr. Noureen Talpur on LinkedIn</a>
      <br><br>
      I am sincerely grateful to both mentors for their continuous guidance and support throughout my professional journey.
      Today, I stand as a confident Data Analyst with a strong foundation in data analytics and a growing specialization
      in machine learning and deep learning.
    </p>
    <!-- images of kashif and noureen -->
    <div style="display: flex; gap: 40px; margin-top: 20px; flex-wrap: wrap;">
        <!-- Kashif Hussain image -->
        <img src="{kashif_src}" 
             alt="Dr. Kashif Hussain" 
             style="width: 250px; 
                    height: 250px; 
                    object-fit: cover; 
                    border-radius: 10px; 
                    border: 2px solid #1E3A5F;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
        <!-- Dr. Noureen Talpur image -->
        <img src="{noureen_src}" 
             alt="Dr. Noureen Talpur" 
             style="width: 250px; 
                    height: 250px; 
                    object-fit: cover; 
                    border-radius: 10px; 
                    border: 2px solid #1E3A5F;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
    </div>
  </div>
</div>

<!-- ── Entry 3: Postgraduate Diploma ────────────────────────────── -->
<div class="timeline-item">
  <div class="timeline-year"><h3>[2024-2025] — Postgraduate Diploma in "Data Science with Artificial Intelligence"</h3></div>
  <div class="timeline-card">
    <p class="card-desc">
      I pursued a Postgraduate Diploma in <i>Data Science with Artificial Intelligence</i> at
      <a href="https://academy.neduet.edu.pk/" target="_blank">NED Academy</a>,
      affiliated with NED University of Engineering and Technology.
      <br><br>
      Modules completed:
      <ol style="color:#CBD5E1; margin-top:8px;">
        <li>Data Science with Python</li>
        <li>Business Intelligence and Data Visualization</li>
        <li>Machine Learning</li>
        <li>Deep Learning</li>
        <li>Fundamentals of Agentic AI</li>
        <li>Capstone Project (Final Year Project)</li>
      </ol>
      <br>
      I also had the opportunity to work with <b>Crux International Canada</b>, which provided hands-on
      Business Intelligence experience and guided me throughout my projects.
    </p>
<!-- image of ned and crux -->
    <div style="display: flex; gap: 40px; margin-top: 20px; flex-wrap: wrap;">
    <img src="{ned_src}" 
             alt="NED University of Engineering and Technology" 
             style="width: 400px; 
                    height: 200px; 
                    object-fit: cover; 
                    border-radius: 10px; 
                    border: 2px solid #1E3A5F;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
    <img src="{crux_src}" 
             alt="Crux International Canada" 
             style="width: 200px; 
                    height: 200px; 
                    object-fit: cover; 
                    border-radius: 10px; 
                    border: 2px solid #1E3A5F;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
  </div>
</div>

<!-- ── Entry 4: Started Freelancing on Upwork ───────────────────── -->
<div class="timeline-item">
  <div class="timeline-year"><h3>[2025] — Started Freelancing on Upwork</h3></div>
  <div class="timeline-card">
    <p class="card-desc">
      Launched freelance career on
      <a href="https://www.upwork.com/freelancers/~01d2856ced28d8eca8" target="_blank">Upwork</a>,
      offering data analysis and web development services to global clients.
      I am proud to be part of this leading international freelancing platform.
      </ol>
      <br>
      I am connected with an Upwork Expert <a href="https://www.linkedin.com/in/ibrahim-solanngi-369aba1b1/" target="_blank">Mr. Muhammad Ibrahim</a>,
      who has been a valuable mentor and guide throughout my freelancing journey.
    </p>
  </div>
</div>

<!-- ── Entry 5: Expanded into Web App Development ───────────────── -->
<div class="timeline-item">
  <div class="timeline-year"><h3>[2025] — Expanded into Web App Development</h3></div>
  <div class="timeline-card">
    <p class="card-desc">
      Expanded skill set into web application development using
      Streamlit, Python, and modern web technologies — combining analytical precision
      with creative problem-solving to build impactful, data-driven solutions.
    </p>
  </div>
</div>
"""

# ─── Render in Streamlit ─────────────────────────────────────────────────────
st.markdown(timeline_html, unsafe_allow_html=True)
