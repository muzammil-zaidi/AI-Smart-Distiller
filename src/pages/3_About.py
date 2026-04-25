import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from fa_icons import inject_fa, fa

st.set_page_config(page_title="About — AI Smart-Distiller", page_icon="📖", layout="wide")

inject_fa()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.page-header {
    background: linear-gradient(135deg, #1a0f2e, #2d1a4a);
    border-radius: 12px; padding: 1.75rem 2rem; margin-bottom: 2rem;
}
.page-header h1 {
    font-family:'Playfair Display',serif; color:#d8c4f0;
    font-size:2rem; margin:0; display:flex; align-items:center; gap:0.6rem;
}
.page-header p  { color:#9a7abf; margin:0.4rem 0 0; font-size:0.9rem; }

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem; color: #9a7abf; margin: 2rem 0 0.75rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #e8d5b7;
}

.member-card {
    background: linear-gradient(135deg, #0f0f23, #1a1a3e);
    border-radius: 12px; padding: 1.25rem 1.5rem;
    display: flex; align-items: center; gap: 1rem;
    border: 1px solid rgba(232,213,183,0.12);
    transition: border-color 0.2s;
}
.member-card:hover { border-color: rgba(232,213,183,0.3); }
.member-avatar {
    width: 48px; height: 48px; border-radius: 50%;
    background: linear-gradient(135deg, #e8d5b7, #c8a882);
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 1rem; color: #1a1a2e; flex-shrink: 0;
}
.member-name  { font-size: 0.95rem; font-weight: 500; color: #e8d5b7; }
.member-id    { font-size: 0.8rem; color: #8899bb; margin-top: 2px; font-family: monospace; }
.member-role  {
    display: inline-flex; align-items: center; gap: 4px;
    font-size: 0.72rem; color: #6677aa; margin-top: 5px;
    background: rgba(232,213,183,0.07);
    border: 1px solid rgba(232,213,183,0.13);
    padding: 2px 8px; border-radius: 20px;
}

.flow-step {
    background: #f8f9ff; border: 1px solid #dde3f5;
    border-radius: 10px; padding: 1rem 1.25rem; margin-bottom: 10px;
}
.flow-header { display:flex; align-items:center; }
.flow-num {
    width: 28px; height: 28px; border-radius: 50%;
    background: #1a1a3e; color: #e8d5b7;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 0.8rem; font-weight: 600; margin-right: 8px; flex-shrink: 0;
}
.flow-title { font-weight: 500; color: #1a1a2e; font-size: 0.95rem; }
.flow-desc  { font-size: 0.83rem; color: #555; margin-top: 4px; margin-left: 36px; line-height: 1.5; }

.setup-box {
    background: #0f0f23; border-radius: 10px; padding: 1.25rem 1.5rem; margin: 0.5rem 0;
}
.setup-title {
    color: #e8d5b7; font-weight: 500; font-size: 0.95rem;
    margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.4rem;
}
.setup-step  { color: #8899bb; font-size: 0.83rem; line-height: 1.8; }
.setup-step code { color: #ffd580; background: #ffffff12; padding: 1px 5px; border-radius: 3px; }

.tech-pill {
    display: inline-block; background: #f0f4ff;
    border: 1px solid #c7d2fe; color: #3730a3;
    padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; margin: 3px;
}
.highlight-box {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    border: 1px solid #86efac; border-radius: 10px;
    padding: 1rem 1.25rem; font-size: 0.88rem; color: #14532d; line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="page-header">
  <h1>{fa("fa-book-open")} About This Project</h1>
  <p>Artificial Intelligence · Spring 2026</p>
</div>
""", unsafe_allow_html=True)

# ── Project Overview ──────────────────────────────────────────
st.markdown('<div class="section-title">Project Overview</div>', unsafe_allow_html=True)
st.markdown("""
**AI Smart-Distiller & Workflow Automator** is a final project for the Artificial Intelligence course at FAST-NUCES.

The system solves the real-world problem of **information overload** — students and professionals constantly deal with long meeting transcripts, project briefs, and articles. Manually reading them, finding deadlines, writing summaries, and then typing everything into spreadsheets is slow and error-prone.

This tool automates that entire pipeline: paste any text → AI extracts structured insights → data is automatically pushed to Google Sheets and emailed to you.
""")

st.markdown('<div class="section-title">The Problem We Solve</div>', unsafe_allow_html=True)
col_prob, col_sol = st.columns(2)
with col_prob:
    st.error("""
**Without this tool:**
- Read 2-page meeting notes manually
- Manually hunt for deadlines and tasks
- Type them into a spreadsheet
- Copy-paste and email to teammates
- ~45 minutes per document
    """)
with col_sol:
    st.success("""
**With AI Smart-Distiller:**
- Paste the text (10 seconds)
- AI extracts summary, tasks, deadlines
- One click → Google Sheets updated
- One click → Email report sent
- ~30 seconds total (**90% faster**)
    """)

# ── How It Works ──────────────────────────────────────────────
st.markdown('<div class="section-title">How It Works — System Flow</div>', unsafe_allow_html=True)

steps = [
    ("Input",          "User pastes long-form text (meeting notes, article, project brief) into the Distiller page."),
    ("AI Extraction",  "The text is sent to OpenAI's GPT-4o-mini via API. A carefully engineered system prompt instructs the model to return only a structured JSON object with <code>summary</code>, <code>tasks</code>, and <code>deadlines</code>."),
    ("JSON Parsing",   "The response is parsed and validated. The mock mode uses regex heuristics to simulate this when no API key is present."),
    ("Google Sheets",  "The extracted data is appended as a new row via the Google Sheets API (gspread + Service Account credentials). Columns: Timestamp, Summary, Tasks, Deadlines."),
    ("Email Report",   "A formatted HTML email is composed and sent via Gmail SMTP, delivering the insights directly to the configured recipient."),
]
for i, (title, desc) in enumerate(steps, 1):
    st.markdown(f"""
    <div class="flow-step">
      <div class="flow-header">
        <span class="flow-num">{i}</span>
        <span class="flow-title">{title}</span>
      </div>
      <div class="flow-desc">{desc}</div>
    </div>""", unsafe_allow_html=True)

# ── Tech Stack ────────────────────────────────────────────────
st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)
techs = ["Python 3.12", "Streamlit", "OpenAI GPT-4o-mini", "gspread",
         "Google Sheets API", "Gmail SMTP", "smtplib", "Prompt Engineering", "JSON Structured Output"]
pills = "".join(f'<span class="tech-pill">{t}</span>' for t in techs)
st.markdown(f'<div style="margin-bottom:1rem;">{pills}</div>', unsafe_allow_html=True)

# ── Setup Guide ───────────────────────────────────────────────
st.markdown('<div class="section-title">Setup & Configuration Guide</div>', unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(f"""
    <div class="setup-box">
      <div class="setup-title">{fa("fa-robot")} OpenAI API</div>
      <div class="setup-step">
        1. Visit <code>platform.openai.com</code><br>
        2. Sign in → API Keys → Create key<br>
        3. Copy key starting with <code>sk-proj-</code><br>
        4. Paste in <code>config.py</code>:<br>
        <code>OPENAI_API_KEY = "sk-proj-..."</code>
      </div>
    </div>""", unsafe_allow_html=True)

with s2:
    st.markdown(f"""
    <div class="setup-box">
      <div class="setup-title">{fa("fa-table-cells")} Google Sheets</div>
      <div class="setup-step">
        1. <code>console.cloud.google.com</code> → New project<br>
        2. Enable Sheets API + Drive API<br>
        3. Create Service Account → Download JSON<br>
        4. Share your Sheet with the service account email<br>
        5. Set <code>GOOGLE_SERVICE_ACCOUNT_JSON</code> in config.py
      </div>
    </div>""", unsafe_allow_html=True)

with s3:
    st.markdown(f"""
    <div class="setup-box">
      <div class="setup-title">{fa("fa-envelope")} Gmail Email</div>
      <div class="setup-step">
        1. Enable 2-Step Verification on Gmail<br>
        2. <code>myaccount.google.com</code> → Security → App Passwords<br>
        3. Generate a 16-char App Password<br>
        4. Set in <code>config.py</code>:<br>
        <code>EMAIL_SENDER = "you@gmail.com"</code><br>
        <code>EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"</code>
      </div>
    </div>""", unsafe_allow_html=True)

# ── AI Innovation ─────────────────────────────────────────────
st.markdown('<div class="section-title">AI Innovation</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
<strong>Why LLM extraction beats simple keyword search:</strong><br>
A keyword search for dates would find every date in a document — including dates mentioned in passing ("the company was founded in 1998"). Our LLM-based approach <em>understands context</em>: it distinguishes a deadline ("submit by May 1") from a historical reference, identifies implicit action items even when not in a numbered list, and generates natural-language summaries that capture intent rather than just words. This is the core AI innovation of this project.
</div>
""", unsafe_allow_html=True)

# ── Team ──────────────────────────────────────────────────────
st.markdown('<div class="section-title">Team</div>', unsafe_allow_html=True)
team = [
    ("MZ", "Muzammil Zaidi",  "24K-0887", "fa-bolt",     "Automation &amp; Workflows"),
    ("MA", "Muzamil Ali",    "24K-1023", "fa-pen-ruler", "Backend &amp; API Integration"),
    ("GM", "Ghulam Mujtaba", "24K-0535", "fa-code",      "UI Design &amp; Project Lead"),
]
c1, c2, c3 = st.columns(3)
for col, (initials, name, sid, icon, role) in zip([c1, c2, c3], team):
    col.markdown(f"""
    <div class="member-card">
      <div class="member-avatar">{initials}</div>
      <div>
        <div class="member-name">{name}</div>
        <div class="member-id">{sid}</div>
        <div class="member-role">{fa(icon)} {role}</div>
      </div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("Instructor: Atif Luqman · FAST-NUCES Karachi")
