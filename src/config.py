# ─────────────────────────────────────────────────────────────
#  config.py  —  API Keys & Settings
#  Fill in your real keys to go live. Leave blank = Demo Mode.
# ─────────────────────────────────────────────────────────────

# ── OpenAI ────────────────────────────────────────────────────
OPENAI_API_KEY = ""           # e.g. "sk-proj-..."
OPENAI_MODEL   = "gpt-4o-mini"

# ── Google Sheets (via gspread + Service Account) ─────────────
# 1. Go to console.cloud.google.com → create a project
# 2. Enable "Google Sheets API" and "Google Drive API"
# 3. Create a Service Account → download the JSON key file
# 4. Share your Google Sheet with the service account email
GOOGLE_SERVICE_ACCOUNT_JSON = ""   # full path to your JSON key file
                                   # e.g. "C:/Users/PMLS/keys/my-project-abc123.json"
GOOGLE_SHEET_NAME = "AI Distiller Output"  # name of the Google Sheet to write to

# ── Email (Gmail SMTP) ────────────────────────────────────────
# Use a Gmail account with an App Password (not your main password)
# Go to: myaccount.google.com → Security → 2-Step Verification → App Passwords
EMAIL_SENDER   = ""   # e.g. "yourname@gmail.com"
EMAIL_PASSWORD = ""   # 16-character App Password from Google
EMAIL_TO       = ""   # recipient email address
