# 🌐 Ambreen Abdul Raheem — Personal Portfolio Website

> **Instructions for Lovable AI:** Read this README completely before generating any code. Follow every instruction strictly. Do not add extra sections, animations, or features not mentioned here.

---

## 👤 About the Owner

- **Name:** Ambreen Abdul Raheem
- **Role:** Data Analyst & Web App Developer
- **Experience:** 4+ Years
- **Currently Working At:** Nishat Welfare Organization
- **Freelancing:** Upwork (Data Analyst & Web App Developer)
- **Core Skills:** Python, Power BI, Web Development

---

## 🛠️ Tech Stack to Use

| Layer | Technology |
|-------|-----------|
| Framework | **Streamlit** (Python-based) |
| Language | Python, HTML, CSS (within Streamlit) |
| Markup | Markdown |
| Deployment | Vercel, Streamlit Cloud, Hugging Face Spaces |

---

## 🎨 Design System — STRICTLY FOLLOW

### Color Palette

| Role | Color Name | Hex Code |
|------|-----------|----------|
| Primary Background | Deep Navy | `#0A1628` |
| Secondary Background | Dark Navy | `#0F2044` |
| Card Background | Navy Card | `#132952` |
| Primary Accent | Electric Teal | `#00D4C8` |
| Secondary Accent | Teal Glow | `#00B4AA` |
| Text Primary | White | `#FFFFFF` |
| Text Secondary | Soft White | `#CBD5E1` |
| Border / Subtle | Muted Navy | `#1E3A5F` |

> ❌ No rainbow or multi-color themes. Only Deep Navy + Electric Teal palette throughout the entire site.

### Typography

| Use | Font | Style |
|-----|------|-------|
| Headings / Hero Name | **Playfair Display** | Serif, Bold 700/900 |
| Body / UI Text | **Inter** | Sans-serif, Regular/Medium |

Load both fonts from Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### Visual Texture & Effects

- **Dot-grid texture** on hero section background — use CSS radial-gradient dots at low opacity
- **Glowing animations** on teal accent elements — CSS box-shadow pulse with teal color
- **Smooth scroll** behavior site-wide
- **Hover glow effect** on all cards and buttons using teal box-shadow
- Keep animations lightweight — no heavy particle systems (performance first)

---

## 🧭 Navbar — Fixed & Scroll-Aware

### Behavior
- **On page load / hero section:** Navbar is fully transparent with white text
- **On scroll past hero:** Navbar transitions to solid Deep Navy (`#0A1628`) with a teal bottom border
- **Transition:** smooth CSS transition on background-color and box-shadow

### Navbar Items
`Home` | `About` | `Projects` | `Certificates` | `Blogs` | `Connect`

### Mobile Menu
- Hamburger icon (☰) visible on screens below 768px
- On click: full-width dropdown slides down with Deep Navy background
- Shows all nav links stacked vertically
- Close button (✕) to dismiss

### CSS Reference
```css
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 999;
  padding: 16px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.3s ease, box-shadow 0.3s ease;
}

.navbar.transparent {
  background: transparent;
}

.navbar.scrolled {
  background: #0A1628;
  border-bottom: 2px solid #00D4C8;
  box-shadow: 0 4px 20px rgba(0, 212, 200, 0.15);
}
```

---

## 🏠 Home Page — Stunning Hero

### Hero Section (Full Viewport Height)

**Background:** Deep Navy (`#0A1628`) with a subtle dot-grid texture overlay

**Layout:** Two-column (left: text content | right: animated avatar)

**Left Column:**
- Small label tag at top: `"Data Analyst & Web App Developer"` — teal color, Inter font, small caps style
- Main name heading: `Ambreen Abdul Raheem` — Playfair Display, very large, white
- Subheading: `"Turning Data into Decisions | Power BI • Python • Web Apps"` — Inter, soft white
- Two CTA buttons side by side:
  - **Primary button:** `View My Work` → links to Projects page — teal background, navy text
  - **Secondary button:** `Get In Touch` → links to Connect page — transparent background, teal border and text
- Row of social icon links below buttons: Upwork, LinkedIn, GitHub, YouTube, Facebook — teal on hover

**Right Column:**
- Animated avatar area: a circular frame with a teal glowing ring animation (CSS keyframe pulse)
- Inside: profile picture placeholder (owner replaces with real photo from `assets/profile.jpg`)
- Floating teal glow ring that pulses continuously around the avatar circle

**Dot-grid texture CSS:**
```css
.hero-bg {
  background-color: #0A1628;
  background-image: radial-gradient(#00D4C8 1px, transparent 1px);
  background-size: 30px 30px;
  opacity: 0.04; /* very subtle */
}
```

---

### Stats Bar (Below Hero)

A full-width horizontal strip — Deep Navy background, teal number accents:

| Stat Label | Value |
|------------|-------|
| Years of Experience | 4+ |
| Projects Completed | 20+ |
| Happy Clients | 15+ |
| Tools Mastered | 5+ |

**Style:** Large number in Electric Teal using Playfair Display, label below in soft white Inter font. Evenly spaced across full width. Thin teal dividers between each stat.

---

### Tool Cards Section

**Heading:** `"Tools & Technologies"` — Playfair Display, white

Four cards in a single row:

| # | Icon | Label |
|---|------|-------|
| 1 | 📊 | Power BI |
| 2 | 🐍 | Python |
| 3 | 🗄️ | SQL |
| 4 | 🌐 | Web Apps |

**Card Style:**
- Background: `#132952`
- Border: `1px solid #1E3A5F`
- Rounded corners
- Icon large centered, label below in Inter font, white text
- On hover: `box-shadow: 0 0 20px rgba(0, 212, 200, 0.3)` — teal glow effect

> ❌ NO skill percentage bars, NO progress rings, NO numbers on tool cards — icon + label ONLY

---

### CTA Banner (Bottom of Home Page)

Full-width banner with a teal-to-navy gradient background:
- Text: `"Let's Work Together — Open for Freelance Projects"` — Playfair Display, white
- Button: `Hire Me on Upwork` — white background, navy text, rounded

---

## 👩‍💼 About Page

### Section 1: Full Bio

**Heading:** `About Me` — Playfair Display, white

Two-column layout:
- **Left:** Profile photo — circular, teal glowing border
- **Right:** Bio paragraph text (owner fills — placeholder below)

```
Placeholder:
I am Ambreen Abdul Raheem, a passionate Data Analyst and Web App Developer 
with 4+ years of experience. I currently work at Nishat Welfare Organization 
and freelance on Upwork helping clients turn raw data into actionable insights...
[Owner will complete this section]
```

---

### Section 2: Animated Skill Bars

**Heading:** `Technical Skills` — Playfair Display, white

Horizontal progress bars, each animating from 0% to its value when scrolled into view:

| Skill | Percentage |
|-------|-----------|
| Power BI | 90% |
| Python | 85% |
| Data Analysis | 90% |
| Web Development | 80% |
| SQL | 80% |
| Streamlit | 85% |

**Bar Style:**
- Track background: `#1E3A5F`
- Fill color: Electric Teal `#00D4C8`
- Animated fill using CSS transitions triggered on scroll
- Skill name on left, percentage value on right

---

### Section 3: Professional Journey Timeline

**Heading:** `My Journey` — Playfair Display, white

Vertical timeline design:
- A continuous vertical teal line on the left
- A teal glowing dot at each entry point
- Navy card beside each dot with the entry text

Timeline placeholder entries (owner fills in years and details):
```
[Year] — Started as Data Analyst
         [Owner fills description]

[Year] — Joined Nishat Welfare Organization
         [Owner fills description]

[Year] — Started Freelancing on Upwork
         [Owner fills description]

[Year] — Expanded into Web App Development
         [Owner fills description]
```

---

### Section 4: Values Section

**Heading:** `What I Stand For` — Playfair Display, white

Three cards in a row:

| Value | Description |
|-------|-------------|
| Data-Driven | Every decision should be backed by data |
| Impact-Focused | Solutions that make a real difference |
| Continuous Learning | Always growing and upskilling |

**Card style:** Navy background (`#132952`), teal top border accent, teal glow on hover

---

### Section 5: References & Resources

**Heading:** `People & Resources That Helped Me` — Playfair Display, white

Simple list or card layout — owner will add names, books, YouTube channels, links as references.

Placeholder: `[Owner will add references here]`

---

## 📁 Project File Structure

```
portfolio/
│
├── app.py                    # Main entry — config + global CSS loader
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_About.py
│   ├── 3_Projects.py
│   ├── 4_Certificates.py
│   ├── 5_Blogs.py
│   └── 6_Connect.py
│
├── assets/
│   ├── profile.jpg           # Owner replaces with real photo
│   ├── certificates/         # Owner adds certificate images here
│   └── style.css             # Global custom CSS
│
└── .streamlit/
    └── config.toml           # Theme config
```

---

## ⚙️ Streamlit Theme Config

**File: `.streamlit/config.toml`**

```toml
[theme]
primaryColor = "#00D4C8"
backgroundColor = "#0A1628"
secondaryBackgroundColor = "#0F2044"
textColor = "#FFFFFF"
font = "sans serif"
```

---

## 📄 Remaining Pages

### `pages/3_Projects.py` — Projects

- Heading: `My Projects` (Playfair Display)
- Two subsections: `Power BI Projects` | `Python / Data Analysis Projects`
- Cards: Title + short description + link button
- Layout: 2 columns using `st.columns(2)`
- Card style: Navy bg, teal border, teal glow on hover
- Add 2–3 placeholder cards — owner replaces with real projects

---

### `pages/4_Certificates.py` — Certificates

- Heading: `Certificates` (Playfair Display)
- `st.image()` for each image in `assets/certificates/`
- Layout: 3 per row using `st.columns(3)`
- Caption below each image (certificate name)
- Placeholder: *"Add certificate images to assets/certificates/ folder"*

---

### `pages/5_Blogs.py` — Blogs

- Heading: `Blogs & Sessions` (Playfair Display)
- Subsections: `Sessions I Conducted` + `Informative Posts`
- Session cards: Title, Date, Description, optional link
- Card style: Navy bg, teal left border accent
- Add 1–2 placeholder entries — owner replaces

---

### `pages/6_Connect.py` — Connect

- Heading: `Get In Touch` (Playfair Display)
- Contact form: Name, Email, Message, Submit button
- On submit: send via `smtplib` + Gmail SMTP using `st.secrets`
- Success message: *"Thank you! Your message has been sent."*
- Form styling: Navy card, teal focused input borders
- Repeat social links row at bottom of page

**Secrets config file:**
```toml
# .streamlit/secrets.toml  (do NOT commit to GitHub)
[email]
sender = "your_email@gmail.com"
password = "your_app_password"
receiver = "your_email@gmail.com"
```

---

## 📦 `requirements.txt`

```
streamlit
Pillow
```

> `smtplib` is Python built-in — no install needed.

---

## 🚀 Deployment Instructions

### A) Streamlit Cloud
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo, set main file as `app.py`
4. Add secrets in the Streamlit Cloud dashboard → Secrets tab

### B) Hugging Face Spaces
1. Create new Space → SDK: **Streamlit**
2. Upload all project files
3. Add secrets: Space Settings → Repository Secrets
4. `app.py` auto-detected as entry point

### C) Vercel
> Vercel does not natively support Streamlit. For Vercel, convert to plain HTML/CSS/JS or Next.js. Recommended: use Streamlit Cloud or Hugging Face Spaces for easiest deployment.

---

## 🔗 Social Links (Owner Will Replace `#` with Real URLs)

| Platform | Placeholder |
|----------|------------|
| Upwork | `#` |
| LinkedIn | `#` |
| GitHub | `#` |
| YouTube | `#` |
| Facebook | `#` |
| Nishat Welfare Organization | `#` |

---

## ✅ Final Checklist for Lovable

- [ ] Deep Navy + Electric Teal palette used everywhere
- [ ] Playfair Display for all headings, Inter for body
- [ ] Dot-grid texture on hero background
- [ ] Glowing teal animations on cards, buttons, avatar ring
- [ ] Navbar: transparent on hero, solid navy on scroll, teal bottom border
- [ ] Hamburger mobile menu implemented
- [ ] Hero: name, tagline, two CTA buttons, social icons, animated avatar with glow ring
- [ ] Stats bar: 4 stats with teal numbers
- [ ] Tool cards: Power BI, Python, SQL, Web Apps — icon + label only, NO percentages
- [ ] CTA banner at bottom of Home page
- [ ] About: Bio (2-col) + animated skill bars + vertical timeline + values cards + references
- [ ] Skill bars animate on scroll into view
- [ ] Timeline has teal vertical line and glowing dots
- [ ] 6 pages total
- [ ] Contact form uses smtplib + st.secrets
- [ ] All social links are `#` placeholders
- [ ] .streamlit/config.toml sets Deep Navy + Teal theme
- [ ] No extra sections or features beyond this README

---

*README created for Lovable AI — Upload this file and Lovable will generate the complete project following these specifications.*
