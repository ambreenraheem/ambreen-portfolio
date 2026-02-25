# ============================================================
# 4_Certificates.py — Certificates Page
# Displays certificate images from the assets/certificates/ folder
# in a 3-column grid layout with captions below each image.
# ============================================================

import streamlit as st  # Import Streamlit framework
import os               # Import os module for file system operations (listing directory contents)

# --- Page Config ---
# Configure the browser tab title, icon, and layout for this page
st.set_page_config(
    page_title="Certificates | Ambreen Abdul Raheem",  # Browser tab title
    page_icon="🏆",                                      # Trophy emoji favicon
    layout="wide",                                       # Full-width page layout
    initial_sidebar_state="expanded"            # Sidebar starts visible by default
)

def load_css():
    """Load the global CSS file for consistent styling across all pages."""
    try:
        with open("assets/style.css", "r") as f:  # Open global stylesheet
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  # Inject CSS
    except FileNotFoundError:
        pass  # Continue without styles if file is missing

# Apply global CSS styles
load_css()

# ============================================================
# PAGE HEADING
# ============================================================

# Main heading — "Certificates" styled with Playfair Display font
st.markdown(f"""
<div style="flex: 1; min-width: 300px;">
    <!-- Hero name — large Playfair Display heading -->
    <h4 style="font-family: 'Playfair Display', serif; text-align:center; font-size: 2rem; color: #FFFFFF; margin-bottom: 16px;">Certificates</h4>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CERTIFICATE GALLERY — 3 per row from assets/certificates/
# ============================================================

# Define the path to the certificates image folder
cert_folder = "assets/certificates"  # Relative path to certificates directory

# Check if the certificates folder exists
if os.path.exists(cert_folder):
    # List all image files in the certificates folder
    # Filter for common image extensions: .jpg, .jpeg, .png, .gif, .webp
    cert_images = [
        f for f in os.listdir(cert_folder)  # Iterate over all files in the folder
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))  # Keep only image files
    ]
    cert_images.sort()  # Sort alphabetically for consistent display order

    # Check if any certificate images were found
    if cert_images:
        # Process images in groups of 3 to create 3-column rows
        for i in range(0, len(cert_images), 3):  # Step through images in groups of 3
            cols = st.columns(3)  # Create a 3-column layout row
            # Iterate over the current batch of up to 3 images
            for j, col in enumerate(cols):  # j = index within the row, col = column object
                if i + j < len(cert_images):  # Check we haven't exceeded the image list
                    img_name = cert_images[i + j]  # Get the image filename
                    img_path = os.path.join(cert_folder, img_name)  # Build full file path
                    with col:  # Place content in the current column
                        # Display the certificate image using st.image
                        st.image(
                            img_path,  # Path to the image file
                            caption=os.path.splitext(img_name)[0],  # Use filename (without extension) as caption
                            use_container_width=True  # Scale image to fill the column width
                        )
    else:
        # No images found in the folder — show placeholder message
        st.markdown("""
        <div class="content-card" style="text-align: center; max-width: 600px; margin: 40px auto;">
            <p class="card-desc" style="font-size: 1.1rem;">
                📜 Add certificate images to the <code>assets/certificates/</code> folder
                and they will appear here automatically.
            </p>
        </div>
        """, unsafe_allow_html=True)  # Render placeholder card
else:
    # Folder doesn't exist at all — create it and show instructions
    os.makedirs(cert_folder, exist_ok=True)  # Create the certificates directory
    st.markdown("""
    <div class="content-card" style="text-align: center; max-width: 600px; margin: 40px auto;">
        <p class="card-desc" style="font-size: 1.1rem;">
            📜 The <code>assets/certificates/</code> folder has been created.<br>
            Add your certificate images there and they will display here automatically.
        </p>
    </div>
    """, unsafe_allow_html=True)  # Render instruction card
