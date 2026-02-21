# ============================================================
# 3_Projects.py — Projects Page
# Displays Power BI and Python/Data Analysis projects in a
# 2-column card layout with teal glow hover effects.
# ============================================================

import streamlit as st  # Import Streamlit framework

# --- Page Config ---
st.set_page_config(
    page_title="Projects | Ambreen Abdul Raheem",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    """Load the global CSS file for consistent styling."""
    try:
        with open("assets/style.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# --- Expander Styling — match dark theme ---
st.markdown("""
<style>
    /* Expander background and border */
    [data-testid="stExpander"] {
        background-color: #0A1628;
        border: 1px solid #1E3A5F;
        border-radius: 8px;
        margin-top: 8px;
    }
    /* Expander header text */
    [data-testid="stExpander"] summary {
        color: #00D4C8;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
    }
    /* Expander content text */
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] li {
        color: #B0C4D8;
        font-family: 'Inter', sans-serif;
        font-size: 0.88rem;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# PAGE HEADING
# ============================================================

st.markdown('<h2 class="section-heading">My Projects</h2>', unsafe_allow_html=True)

# ============================================================
# SUBSECTION 1: POWER BI PROJECTS
# ============================================================

st.markdown("""
<h3 style="
    font-family: 'Playfair Display', serif;
    color: #00D4C8;
    font-size: 1.5rem;
    margin: 30px 0 20px;
    text-align: center;
">Power BI Projects</h3>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# --- Power BI Card 1 ---
with col1:
    # Clean short card
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">SUPERSTORE SALES ANALYSIS</h3>
        <p class="card-desc">
            Power BI report analyzing sales trends, customer segments, and order 
            decline for a hypermarket — built in collaboration with 
            Crux International Canada.
        </p>
        <a href="https://youtu.be/_r7lJlX_P4U?si=lKDAViI3vYRmTela" class="btn-primary" style="
            display: inline-block;
            margin-top: 16px;
            font-size: 0.9rem;
            padding: 8px 20px;
        ">View Project</a>
    </div>
    """, unsafe_allow_html=True)

    # Detail expander below the card
    with st.expander("📄 View Details"):
        st.markdown("""
        **Collaboration:**  
        Partnered with Sir Qaisar Ali (Founder: Crux International Canada), a leading 
        consulting firm specializing in data-driven business solutions.

        **Overview:**  
        Superstore is a hypermarket selling furniture, office supplies, and IT products. 
        Customers are grouped into the following segments:
        - Consumer
        - Corporate
        - Home Office

        **Problem Statement:**  
        Management was concerned about a decreasing number of orders. I was hired as a 
        Data Analytics & BI specialist to investigate the issue.

        **Deliverables:**  
        Analyzed the provided dataset, prepared a 4-page Power BI report, and presented 
        findings and suggestions to the board of corporate directors.
        """)

# --- Power BI Card 2 ---
with col2:
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">365 BUSINESS BANK</h3>
        <p class="card-desc">
            Power BI report analyzing the bank transactions of 365 Business Bank
            — built in collaboration with Crux International Canada.
        </p>
        <a href="https://youtu.be/VgL1-t2sjt0?si=T4uQSQS9pPXXitdH" class="btn-primary" style="
            display: inline-block;
            margin-top: 16px;
            font-size: 0.9rem;
            padding: 8px 20px;
        ">View Project</a>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 View Details"):
        st.markdown("""
        **Overview:**

        365 Business Bank is a forward-thinking financial institution dedicated to fostering innovation and customer-centric decision-making.
        With a commitment to excellence, we leverage data-driven insights to enhance operational efficiency,
        optimize product offerings, and maintain robust security measures.
        Our comprehensive approach to analytics ensures that every facet of our operations aligns with our strategic goals and market demands.
        
        **Objective:**
        The objective of this project is to harness the power of an integrated dataset:
        - Encompassing MCC Data, Card Data, User Data, and Transaction Data
        - To extract actionable insights
        - By developing a robust analytics framework in Power BI
        
        **We aim to:**
        - Enhance customer segmentation and personalization
        - Optimize resource allocation and operational efficiency
        - Identify and mitigate potential risks and fraud
        - Drive strategic initiatives that foster growth and competitive advantage
        """)

# # --- Power BI Card 3 ---
# with col3:
#     st.markdown("""
#     <div class="content-card">
#         <h3 class="card-title">365 BUSINESS BANK</h3>
#         <p class="card-desc">
#             Power BI report analyzing the bank transactions of 365 Business Bank
#             — built in collaboration with Crux International Canada.
#         </p>
#         <a href="https://youtu.be/VgL1-t2sjt0?si=T4uQSQS9pPXXitdH" class="btn-primary" style="
#             display: inline-block;
#             margin-top: 16px;
#             font-size: 0.9rem;
#             padding: 8px 20px;
#         ">View Project</a>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.expander("📄 View Details"):
#         st.markdown("""
#         **Overview:**

#         365 Business Bank is a forward-thinking financial institution dedicated to fostering innovation and customer-centric decision-making.
#         With a commitment to excellence, we leverage data-driven insights to enhance operational efficiency,
#         optimize product offerings, and maintain robust security measures.
#         Our comprehensive approach to analytics ensures that every facet of our operations aligns with our strategic goals and market demands.
        
#         **Objective:**
#         The objective of this project is to harness the power of an integrated dataset:
#         - Encompassing MCC Data, Card Data, User Data, and Transaction Data
#         - To extract actionable insights
#         - By developing a robust analytics framework in Power BI
        
#         **We aim to:**
#         - Enhance customer segmentation and personalization
#         - Optimize resource allocation and operational efficiency
#         - Identify and mitigate potential risks and fraud
#         - Drive strategic initiatives that foster growth and competitive advantage
#         """)

# --- Separator ---
st.markdown("<hr style='border-color: #1E3A5F; margin: 40px 0;'>", unsafe_allow_html=True)

# ============================================================
# SUBSECTION 2: PYTHON / DATA ANALYSIS PROJECTS
# ============================================================

st.markdown("""
<h3 style="
    font-family: 'Playfair Display', serif;
    color: #00D4C8;
    font-size: 1.5rem;
    margin: 30px 0 20px;
    text-align: center;
">Python / Data Analysis Projects</h3>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

# --- Python Card 1 ---
with col3:
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">🚨 Taxi Trip Fraud Detection with Deep Learning! 🚨</h3>
        <p class="card-desc">
            Yellow and green taxi trip records include pickup/drop-off times, locations, trip distances, fares, rate types, payment types, and passenger counts.
            The data was collected by NYC Taxi and Limousine Commission (TLC) through authorized technology providers under the TPEP/LPEP programs.
            TLC does not guarantee the accuracy of this data.
        </p>
        <a href="https://youtu.be/kWqTuHhm1vE?si=KHHCaCHsj5fZnkZe" class="btn-primary" style="
            display: inline-block;
            margin-top: 16px;
            font-size: 0.9rem;
            padding: 8px 20px;
        ">View Project</a>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 View Details"):
        st.markdown("""
        **Overview:**

        This project focuses on building a robust fraud detection system for taxi trips using deep learning. The dataset comprises yellow and green taxi trip records from New York City, including detailed information about pickup/drop-off times, locations, trip distances, fares, rate types, payment methods, and passenger counts. Collected by the NYC Taxi and Limousine Commission (TLC) through authorized technology providers, this dataset provides a comprehensive view of taxi operations across the city.

        **Objective:**
        The primary objective of this project is to develop an advanced fraud detection model that can accurately identify fraudulent taxi trips. By leveraging deep learning techniques, we aim to uncover complex patterns and anomalies indicative of fraudulent activities that may not be easily detectable through traditional methods. The model will be trained on historical trip data to learn the characteristics of both legitimate and fraudulent trips, enabling it to proactively flag suspicious transactions.

        **Key Features:**
        - **Comprehensive Data Analysis:** Thorough exploration of trip data to understand distributions, correlations, and potential fraud indicators.
        - **Advanced Feature Engineering:** Creation of meaningful features from raw data to enhance model performance.
        - **Deep Learning Modeling:** Implementation of deep learning architectures to capture intricate patterns in the data.
        - **Fraud Detection:** Development of a system to identify and flag potentially fraudulent taxi trips.
        - **Performance Evaluation:** Rigorous testing and validation of the model to ensure accuracy and reliability.
        """)

# --- Python Card 2 ---
with col4:
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">🚲 Toronto Bike Share Station Status</h3>
        <p class="card-desc">
            Toronto Bike Share is a bike-sharing system in Toronto, Ontario, Canada.
            It is owned by the City of Toronto and operated by PBSC Urban Solutions.
            The system has 6,893 bikes and 625 stations across the city.
            Created in Streamlit and Python. Deployed on Hugging Face Spaces.
        </p>
        <a href="https://huggingface.co/spaces/ambreenraheem/Toronto_Bikeshare_app" class="btn-primary" style="
            display: inline-block;
            margin-top: 16px;
            font-size: 0.9rem;
            padding: 8px 20px;
        ">View Project</a>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 View Details"):
        st.markdown("""
        **Overview:**

        Toronto Bike Share is a bike-sharing system in Toronto, Ontario, Canada.
        It is owned by the City of Toronto and operated by PBSC Urban Solutions.
        The system has 6,893 bikes and 625 stations across the city. Created in Streamlit and Python. Deployed on Hugging Face Spaces.

        **Objective:**
        The primary objective of this project is to develop an advanced fraud detection model that can accurately identify fraudulent taxi trips. By leveraging deep learning techniques, we aim to uncover complex patterns and anomalies indicative of fraudulent activities that may not be easily detectable through traditional methods. The model will be trained on historical trip data to learn the characteristics of both legitimate and fraudulent trips, enabling it to proactively flag suspicious transactions.

        **Key Features:**
        - **Comprehensive Data Analysis:** Thorough exploration of trip data to understand distributions, correlations, and potential fraud indicators.
        - **Advanced Feature Engineering:** Creation of meaningful features from raw data to enhance model performance.
        - **Deep Learning Modeling:** Implementation of deep learning architectures to capture intricate patterns in the data.
        - **Fraud Detection:** Development of a system to identify and flag potentially fraudulent taxi trips.
        - **Performance Evaluation:** Rigorous testing and validation of the model to ensure accuracy and reliability.
        """)
