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

# Build base64 data URI for the profile image from assets/Profile.jpeg
profile_img_path = "assets/Profile.jpeg"  # Path to the actual profile photo
if os.path.exists(profile_img_path):  # Verify the image exists
    profile_b64 = get_image_base64(profile_img_path)  # Encode to base64
    profile_src = f"data:image/jpeg;base64,{profile_b64}"  # Create data URI
else:
    profile_src = "https://via.placeholder.com/250x250/132952/00D4C8?text=AR"  # Fallback

# Build base64 for BADSHAHKAREEM.png
badshah_img_path = "assets/BADSHAHKAREEM.png"
if os.path.exists(badshah_img_path):
    badshah_b64 = get_image_base64(badshah_img_path)
    badshah_src = f"data:image/png;base64,{badshah_b64}"
else:
    badshah_src = "https://via.placeholder.com/150"

# Build base64 for nishat.jpeg
nishat_img_path = "assets/nishat.jpeg"
if os.path.exists(nishat_img_path):
    nishat_b64 = get_image_base64(nishat_img_path)
    nishat_src = f"data:image/jpeg;base64,{nishat_b64}"
else:
    nishat_src = "https://via.placeholder.com/150"

# --- Page Config ---
# Configure browser tab title, icon, and layout for this page
st.set_page_config(
    page_title="About | Ambreen Abdul Raheem",  # Browser tab title
    page_icon="👩‍💼",                              # About page favicon
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
st.markdown('<h2 class="section-heading">About Me</h2>', unsafe_allow_html=True)

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

# ============================================================
# NOTE: Section 2 (Animated Skill Bars) — REMOVED
# The skill bars section has been intentionally omitted
# as per the user's request to remove Section 2.
# ============================================================

# ============================================================
# SECTION 3: PROFESSIONAL JOURNEY TIMELINE
# Vertical timeline with teal line, glowing dots, and navy cards
# ============================================================

# # Section heading — "My Journey" in Playfair Display
# st.markdown('<h2 class="section-heading">My Journey</h2>', unsafe_allow_html=True)

# # Inject the vertical timeline HTML structure
# # Uses CSS classes from style.css: .timeline, .timeline-item, .timeline-year, .timeline-card
# st.markdown("""
# <div class="timeline" style="max-width: 800px; margin: 0 auto;">
#     <!-- Timeline Entry 0: Graduation -->
#     <div class="timeline-item">
#         <!-- Year label in teal -->
#         <div class="timeline-year">[2010] — Graduation</div>
#         <!-- Navy card with description text -->
#         <div class="timeline-card">
#             <p class="card-desc">
#                 🎓 My academic background includes a Bachelor of Arts (BA) and Bachelor of Education (B.Ed), and I began my career as a school teacher. I dedicated 15 years of my life to teaching with complete passion and commitment. Alongside my school job, I also ran home-based coaching classes, where my students achieved excellent results. Now that I’ve stepped into the field of data analysis, I bring the same dedication and consistency. For the past 4 years, I’ve been working hard with focus and determination, continuously updating and upgrading my skills to stay relevant and effective in this evolving field.
            
#             </p>
#         </div>
#     </div>
#     <!-- Timeline Entry 1: Started as Data Analyst -->
#     <div class="timeline-item">
#         <!-- Year label in teal -->
#         <div class="timeline-year">[2019] — Started as Data Analyst</div>
#         <!-- Navy card with description text -->
#         <div class="timeline-card">
#             <p class="card-desc">
#                 My turning point came during the COVID-19 pandemic:
#                 During the COVID-19 pandemic, I paused teaching and joined Nishat Welfare Organization (NWO) as a Data Entry Specialist. That six-month opportunity became the foundation of my data journey.
#                 🚀 It was during this time that <b>Mr. Pir Muhammad Sadiq</b>, Patron-in-Chief of <a href="https://nishatwelfare.org/">The Nishat Welfare Organization (NWO)</a>, highlighted the organization’s need for data professionals.
#                 Inspired, I began exploring the field of data science.
#                 <div style="display: flex; gap: 10px; margin-top: 15px; justify-content: center; flex-wrap: wrap;">
#                     <img src="{badshah_src}" style="width: 150px; border-radius: 8px; border: 2px solid var(--accent); box-shadow: 0 4px 10px rgba(0,212,200,0.2);">
#                     <img src="{nishat_src}" style="width: 150px; border-radius: 8px; border: 2px solid var(--accent); box-shadow: 0 4px 10px rgba(0,212,200,0.2);">
#                 </div>
#             </p>
#         </div>
#     </div>
#     <!-- Timeline Entry 2: My Mentors -->
#     <div class="timeline-item">
#         <div class="timeline-year">[2020] — My Mentor: Dr. Kashif Hussain and TS Dr. Noureen Talpur.</div>
#         <div class="timeline-card">
#             <p class="card-desc">
#                 I met Mr. Kashif Hussain, who introduced me to the world of data analytics. 
#                 <b>Dr. Kashif Hussain</b> PhD in Machine Learning & Data Mining | AI/ML Researcher & Educator | UK Global Talent | BCS & ACM Member (a lecturer at Solent University, Southampton, and now he is at University of Roehampton, London, UK).
#                 He is a passionate educator and researcher with a strong commitment to advancing knowledge in the field of machine learning and data mining. <a href="https://www.linkedin.com/in/kashif-talpur">Dr. Kashif Hussain</a>           
#                 <b>TS Dr. Noureen Talpur</b> Lecturer | Professional Technologist | Researcher (Machine Learning & Data Science)(a lecturer in Universiti Teknologi PETRONAS, Ipoh, Perak, Malaysia) <a href="https://www.linkedin.com/in/noureen-talpur">TS Dr. Noureen Talpur</a>
#                 I am sincerely grateful to both mentors for their continuous guidance and support throughout my professional journey.
#                 Today, I stand as a confident Data Analyst with a strong foundation in data analytics and a growing specialization in machine learning and deep learning. I am deeply motivated to contribute meaningfully to the field of data science by delivering analytical solutions that drive informed decision-making.
#                 I also take pride in being a critical thinker and a creative web developer, combining analytical precision with innovative problem-solving to build impactful, data-driven solutions.
#             </p>
#         </div>
#     </div>
#     <!-- Timeline Entry 3: Postgraduate Diploma (2024-2025) in "Data Science with Artificial Intelligence" -->
#     <div class="timeline-item">
#         <div class="timeline-year">[2024-2025] — Postgraduate Diploma in "Data Science with Artificial Intelligence"</div>
#         <div class="timeline-card">
#             <p class="card-desc">
#                 I pursued a Postgraduate Diploma in "Data Science with Artificial Intelligence" at <a href="https://academy.neduet.edu.pk//">NED Academy</a>, affiliated with NED (Nadirshaw Edulji Dinshaw University of Engineering and Technology).
#                 This program significantly enhanced my understanding of machine learning, deep learning, and advanced data analytics techniques.
#                 I am pleased to share that I have successfully completed my postgraduate diploma, and I can confidently say that my journey throughout this program was truly outstanding and transformative.

#                 During this PGD program, I completed the following modules:
#                 1. Data Science with Python
#                 2. Business Intelligence and Data Visualization
#                 3. Machine Learning
#                 4. Deep Learning
#                 5. Fundamentals of Agentic AI
#                 6. Capstone Project (Final Year Project)

#                 This program provided me with a much deeper and more structured understanding of these domains. I worked on multiple practical projects that strengthened my applied skills, many of which are available for review on my GitHub profile.

#                 And here, I got the opportunity to work with <b>Crux International Canada</b> and to deepen my understanding of Business Intelligence. Crux International Canada provides emerging talent and dedicated data analysts with valuable opportunities to grow and actively guides them throughout their projects.                
#             </p>
#         </div>
#     </div>
#     <!-- Timeline Entry 3: Started Freelancing on Upwork -->
#     <div class="timeline-item">
#         <div class="timeline-year">[2025] — Started Freelancing on Upwork</div>
#         <div class="timeline-card">
#             <p class="card-desc">
#                 Launched freelance career on Upwork, offering data analysis and web development services to global clients. <a href="https://www.upwork.com/freelancers/~01d2856ced28d8eca8">Upwork</a> is a leading international freelancing platform. And I am proud to be a part of it.
#             </p>
#         </div>
#     </div>
#     <!-- Timeline Entry 4: Expanded into Web App Development -->
#     <div class="timeline-item">
#         <div class="timeline-year">[Year] — Expanded into Web App Development</div>
#         <div class="timeline-card">
#             <p class="card-desc">
#                 Expanded skill set into web application development using
#                 Streamlit, Python, and modern web technologies.
#             </p>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)  # Render timeline HTML

# # --- Horizontal separator ---
# st.markdown("<hr style='border-color: #1E3A5F; margin: 40px 0;'>", unsafe_allow_html=True)

# # ============================================================
# # SECTION 4: VALUES — "What I Stand For"
# # Three cards in a row with teal top border accent
# # ============================================================

# # Section heading — "What I Stand For" in Playfair Display
# st.markdown('<h2 class="section-heading">What I Stand For</h2>', unsafe_allow_html=True)

# # Inject three values cards in a flex row
# # Each card has a teal top border, navy background, and teal glow on hover
# st.markdown("""
# <div style="
#     display: flex;
#     justify-content: center;
#     gap: 24px;
#     flex-wrap: wrap;
#     max-width: 1000px;
#     margin: 0 auto;
#     padding: 0 20px;
# ">
#     <!-- Value Card 1: Data-Driven -->
#     <div class="content-card card-top-accent" style="flex: 1; min-width: 250px; max-width: 300px;">
#         <!-- Card title — value name -->
#         <h3 class="card-title" style="color: #00D4C8;">📊 Data-Driven</h3>
#         <!-- Card description — value explanation -->
#         <p class="card-desc">Every decision should be backed by data. I believe in letting
#         numbers guide strategy and action.</p>
#     </div>
#     <!-- Value Card 2: Impact-Focused -->
#     <div class="content-card card-top-accent" style="flex: 1; min-width: 250px; max-width: 300px;">
#         <h3 class="card-title" style="color: #00D4C8;">🎯 Impact-Focused</h3>
#         <p class="card-desc">Solutions that make a real difference. I focus on delivering
#         work that creates measurable impact.</p>
#     </div>
#     <!-- Value Card 3: Continuous Learning -->
#     <div class="content-card card-top-accent" style="flex: 1; min-width: 250px; max-width: 300px;">
#         <h3 class="card-title" style="color: #00D4C8;">📚 Continuous Learning</h3>
#         <p class="card-desc">Always growing and upskilling. Technology evolves rapidly,
#         and I stay ahead by continuous learning.</p>
#     </div>
# </div>
# """, unsafe_allow_html=True)  # Render values cards HTML

# # --- Horizontal separator ---
# st.markdown("<hr style='border-color: #1E3A5F; margin: 40px 0;'>", unsafe_allow_html=True)

# # ============================================================
# # SECTION 5: REFERENCES & RESOURCES
# # Simple placeholder section for the owner to fill with names,
# # books, YouTube channels, and links that helped them grow.
# # ============================================================

# # Section heading — "People & Resources That Helped Me"
# st.markdown('<h2 class="section-heading">People & Resources That Helped Me</h2>', unsafe_allow_html=True)

# # Placeholder card — owner will add actual references here
# st.markdown("""
# <div class="content-card" style="max-width: 800px; margin: 0 auto; text-align: center;">
#     <!-- Placeholder text — owner replaces with real references -->
#     <p class="card-desc" style="font-size: 1.1rem;">
#         [Owner will add references here — mentors, books, YouTube channels,
#         courses, and resources that helped along the journey]
#     </p>
# </div>
# """, unsafe_allow_html=True)  # Render references placeholder


import streamlit as st
import base64
from pathlib import Path

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

# ─── Image paths (owner apni actual files yahan rakh ke paths update kare) ──
# assets/ folder mein yeh dono images rakho:
#   assets/badshah.jpg   ←  Mr. Pir Muhammad Sadiq ki photo
#   assets/nishat.jpg    ←  Nishat Welfare Organization ka logo / photo
# badshah_src = img_to_base64("assets/badshah.jpg")
# nishat_src  = img_to_base64("assets/nishat.jpg")

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
    <div class="timeline-year">[2010] — Graduation</div>
    <div class="timeline-card">
        <p class="card-desc">
        🎓 My academic background includes a Bachelor of Arts (BA) and Bachelor of Education (B.Ed), and I began my career as a school teacher. I dedicated 15 years of my life to teaching with complete passion and commitment. Alongside my school job, I also ran home-based coaching classes, where my students achieved excellent results. Now that I’ve stepped into the field of data analysis, I bring the same dedication and consistency. For the past 4 years, I’ve been working hard with focus and determination, continuously updating and upgrading my skills to stay relevant and effective in this evolving field.
        </p>
    </div>
</div>

<!-- ── Entry 1: Started as Data Analyst ─────────────────────────── -->
<div class="timeline-item">
  <div class="timeline-year">[2019] — Started as Data Analyst</div>
  <div class="timeline-card">
    <p class="card-desc">
      My turning point came during the COVID-19 pandemic.
      I paused teaching and joined Nishat Welfare Organization (NWO) as a Data Entry Specialist.
      That six-month opportunity became the foundation of my data journey.
      <br><br>
      🚀 It was during this time that <b>Mr. Pir Muhammad Sadiq</b>,
      Patron-in-Chief of
      <a href="https://nishatwelfare.org/" target="_blank">The Nishat Welfare Organization (NWO)</a>,
      highlighted the organization's need for data professionals.
      Inspired, I began exploring the field of data science.
    </p>
  </div>
</div>

<!-- ── Entry 2: My Mentors ───────────────────────────────────────── -->
<div class="timeline-item">
  <div class="timeline-year">[2020] — My Mentors: Dr. Kashif Hussain &amp; TS Dr. Noureen Talpur</div>
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
  </div>
</div>

<!-- ── Entry 3: Postgraduate Diploma ────────────────────────────── -->
<div class="timeline-item">
  <div class="timeline-year">[2024–2025] — Postgraduate Diploma in "Data Science with Artificial Intelligence"</div>
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
  </div>
</div>

<!-- ── Entry 4: Started Freelancing on Upwork ───────────────────── -->
<div class="timeline-item">
  <div class="timeline-year">[2025] — Started Freelancing on Upwork</div>
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
  <div class="timeline-year">[2025] — Expanded into Web App Development</div>
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
