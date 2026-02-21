# ============================================================
# 6_Connect.py — Connect / Contact Page
# Contact form (Name, Email, Message) that sends via smtplib + Gmail SMTP.
# Uses st.secrets for email credentials. Social links row at bottom.
# ============================================================

import streamlit as st  # Import Streamlit framework
import smtplib           # Built-in Python library for sending emails via SMTP protocol
from email.mime.text import MIMEText        # Create plain text email message objects
from email.mime.multipart import MIMEMultipart  # Create multipart email messages (for headers)

# --- Page Config ---
# Configure browser tab title, icon, and layout for this page
st.set_page_config(
    page_title="Connect | Ambreen Abdul Raheem",  # Browser tab title
    page_icon="📬",                                 # Mailbox emoji favicon
    layout="wide",                                  # Full-width layout
    initial_sidebar_state="expanded"            # Sidebar starts visible by default
)

def load_css():
    """Load the global CSS file for consistent styling across all pages."""
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

# Main heading — "Get In Touch" in Playfair Display
st.markdown('<h2 class="section-heading">Get In Touch</h2>', unsafe_allow_html=True)

# ============================================================
# CONTACT FORM — Styled Navy Card with Teal Focused Borders
# ============================================================

# Center the form in a navy card container with max width
st.markdown("""
<div style="max-width: 600px; margin: 0 auto;">
""", unsafe_allow_html=True)  # Open the centered container div

# --- Contact Form using Streamlit's st.form ---
# st.form groups inputs together and submits them all at once
with st.form("contact_form", clear_on_submit=True):  # Clear inputs after successful submit
    # Name input field — single-line text input
    name = st.text_input(
        "Your Name",                # Label displayed above the input field
        placeholder="Enter your name"  # Grey placeholder text inside the field
    )
    # Email input field — single-line text input
    email = st.text_input(
        "Your Email",               # Label displayed above the input
        placeholder="Enter your email address"  # Placeholder text
    )
    # Message textarea — multi-line text input for the message body
    message = st.text_area(
        "Your Message",             # Label displayed above the textarea
        placeholder="Write your message here...",  # Placeholder text
        height=150                  # Height of the textarea in pixels
    )
    # Submit button — styled via CSS as teal button with navy text
    submitted = st.form_submit_button("Send Message")  # Returns True when clicked

    # --- Handle Form Submission ---
    if submitted:  # Check if the submit button was clicked
        # Validate that all fields are filled in
        if name and email and message:  # All three fields must be non-empty
            try:
                # Attempt to read email credentials from Streamlit secrets
                # These are stored in .streamlit/secrets.toml (NOT committed to GitHub)
                sender_email = st.secrets["email"]["sender"]     # Sender email address
                sender_password = st.secrets["email"]["password"]  # App-specific password
                receiver_email = st.secrets["email"]["receiver"]   # Receiver email address

                # Create the email message object (multipart for headers + body)
                msg = MIMEMultipart()                   # Initialize empty email message
                msg['From'] = sender_email              # Set the From header
                msg['To'] = receiver_email              # Set the To header
                msg['Subject'] = f"Portfolio Contact: {name}"  # Subject line with sender's name

                # Build the email body text with all form fields
                body = f"""
New message from your portfolio contact form:

Name: {name}
Email: {email}
Message: {message}
                """
                msg.attach(MIMEText(body, 'plain'))     # Attach body as plain text

                # Connect to Gmail SMTP server and send the email
                server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail on port 587
                server.starttls()                       # Upgrade connection to TLS encryption
                server.login(sender_email, sender_password)  # Authenticate with Gmail
                server.send_message(msg)                # Send the email
                server.quit()                           # Close the SMTP connection

                # Show success message to the user
                st.success("Thank you! Your message has been sent. ✅")

            except KeyError:
                # st.secrets doesn't have the required email keys
                # This means .streamlit/secrets.toml is missing or misconfigured
                st.warning("Email not configured. Please set up .streamlit/secrets.toml")
                # Still show the message that was attempted so owner can see it
                st.info(f"Message from {name} ({email}): {message}")

            except Exception as e:
                # Catch any other errors (network, auth, etc.)
                st.error(f"Failed to send message: {str(e)}")
        else:
            # One or more fields were left empty
            st.warning("Please fill in all fields before submitting.")

# Close the centered container div
st.markdown("</div>", unsafe_allow_html=True)

# --- Horizontal separator before social links ---
st.markdown("<hr style='border-color: #1E3A5F; margin: 40px 0;'>", unsafe_allow_html=True)

# ============================================================
# SOCIAL LINKS ROW — Repeated at the bottom of the Connect page
# Owner replaces "#" with real profile URLs
# ============================================================

# Social links heading
st.markdown("""
<h3 style="
    font-family: 'Playfair Display', serif;
    color: #FFFFFF;
    font-size: 1.3rem;
    text-align: center;
    margin-bottom: 20px;
">Find Me Online</h3>
""", unsafe_allow_html=True)  # Render heading

# Row of social media links — centered, teal on hover
st.markdown("""
<div class="social-links" style="justify-content: center; gap: 30px; margin-bottom: 40px;">
    <!-- Each link: emoji + platform name, owner replaces # with real URL -->
    <a href="#" title="Upwork" style="font-size: 1.1rem;">💼 Upwork</a>
    <a href="#" title="LinkedIn" style="font-size: 1.1rem;">🔗 LinkedIn</a>
    <a href="#" title="GitHub" style="font-size: 1.1rem;">💻 GitHub</a>
    <a href="#" title="YouTube" style="font-size: 1.1rem;">🎬 YouTube</a>
    <a href="#" title="Facebook" style="font-size: 1.1rem;">📘 Facebook</a>
    <a href="#" title="Nishat Welfare Organization" style="font-size: 1.1rem;">🏢 Nishat Welfare</a>
</div>
""", unsafe_allow_html=True)  # Render social links row
