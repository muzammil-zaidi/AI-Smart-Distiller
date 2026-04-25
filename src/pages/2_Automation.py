import streamlit as st
import time, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from sheets import append_to_sheet
from mailer  import send_email
from mock_mode import sheets_configured, email_configured
from fa_icons import inject_fa, fa

st.set_page_config(page_title="Automation — AI Smart-Distiller", page_icon="⚡", layout="wide")
inject_fa()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.page-header { background: linear-gradient(135deg, #0d1f0d, #1a3a1a); border-radius: 12px; padding: 1.75rem 2rem; margin-bottom: 1.5rem; }
.page-header h1 { font-family:'Playfair Display',serif; color:#c8f0c8; font-size:2rem; margin:0; display:flex; align-items:center; gap:0.6rem; }
.page-header p  { color:#7aaa7a; margin:0.4rem 0 0; font-size:0.9rem; }
.dest-card { border: 1.5px solid #e0e0e0; border-radius: 12px; padding: 1.5rem; background: #fafafa; transition: border-color 0.2s; }
.dest-card.active { border-color: #2563eb; background: #f0f6ff; }
.dest-title { font-size: 1.05rem; font-weight: 500; color: #1a1a2e; display: flex; align-items: center; gap: 0.5rem; }
.dest-desc  { font-size: 0.83rem; color: #666; margin-top: 4px; line-height: 1.5; }
.result-preview { background: #f8f9ff; border: 1px solid #dde3f5; border-radius: 8px; padding: 1rem 1.25rem; font-size: 0.88rem; color: #3a3a6a; line-height: 1.7; max-height: 180px; overflow-y: auto; }
.config-box { background: #fff7ed; border: 1px solid #fdba74; border-radius: 8px; padding: 0.75rem 1rem; font-size: 0.83rem; color: #92400e; margin-top: 0.75rem; }
.config-step { background: #f1f5f9; border-radius: 4px; padding: 3px 8px; margin: 3px 0; font-family: monospace; font-size: 0.8rem; color: #334155; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="page-header">
  <h1>{fa("fa-bolt")} Automation</h1>
  <p>Push extracted insights to Google Sheets and Email automatically</p>
</div>
""", unsafe_allow_html=True)

result = st.session_state.get("last_result", None)
if not result:
    st.warning("No extracted data yet. Go to **Distiller** first and run the pipeline.")
    st.stop()

with st.expander("Preview: data that will be sent", expanded=True):
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Summary**")
        st.markdown(f'<div class="result-preview">{result.get("summary","—")}</div>', unsafe_allow_html=True)
        st.markdown("**Tasks**")
        tasks_html = "".join(f'<div>{fa("fa-check-circle","color:#2563eb;")} {t}</div>' for t in result.get("tasks",[])) or "<i>None found</i>"
        st.markdown(f'<div class="result-preview">{tasks_html}</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown("**Deadlines**")
        dl_html = "".join(f'<div>{fa("fa-calendar-days","color:#ca8a04;")} <b>{d["date"]}</b> — {d["context"]}</div>' for d in result.get("deadlines",[])) or "<i>None found</i>"
        st.markdown(f'<div class="result-preview">{dl_html}</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("Choose destinations")

col1, col2 = st.columns(2)

with col1:
    sheets_ok = sheets_configured()
    st.markdown(f"""
    <div class="dest-card {'active' if sheets_ok else ''}">
      <div class="dest-title">{fa("fa-table-cells")} Google Sheets</div>
      <div class="dest-desc">Appends one row: Timestamp · Summary · Tasks · Deadlines<br>Sheet: <strong>AI Distiller Output</strong></div>
      {'<div class="config-box">Add <code>GOOGLE_SERVICE_ACCOUNT_JSON</code> and <code>GOOGLE_SHEET_NAME</code> in config.py to enable.</div>' if not sheets_ok else ''}
    </div>""", unsafe_allow_html=True)
    send_sheets = st.checkbox("Send to Google Sheets", value=sheets_ok)

with col2:
    email_ok = email_configured()
    st.markdown(f"""
    <div class="dest-card {'active' if email_ok else ''}">
      <div class="dest-title">{fa("fa-envelope")} Email Report</div>
      <div class="dest-desc">Sends a formatted HTML email with all insights<br>Via Gmail SMTP</div>
      {'<div class="config-box">Add <code>EMAIL_SENDER</code>, <code>EMAIL_PASSWORD</code>, <code>EMAIL_TO</code> in config.py to enable.</div>' if not email_ok else ''}
    </div>""", unsafe_allow_html=True)
    send_mail = st.checkbox("Send Email Report", value=email_ok)

st.markdown("<br>", unsafe_allow_html=True)
run_auto = st.button("Run Automation", type="primary")

if run_auto:
    if not send_sheets and not send_mail:
        st.error("Select at least one destination.")
    else:
        log = {}
        with st.status("Running automation pipeline…", expanded=True) as status:
            if send_sheets:
                st.write("Appending row to Google Sheets…")
                r = append_to_sheet(result, st.session_state.get("last_input",""))
                log["Google Sheets"] = r
                st.write(("Done — " if r["success"] else "Error — ") + r["message"])
            if send_mail:
                st.write("Sending email report…")
                r = send_email(result)
                log["Email"] = r
                st.write(("Done — " if r["success"] else "Error — ") + r["message"])
            all_ok = all(v["success"] for v in log.values())
            status.update(label="Automation complete!" if all_ok else "Completed with errors.", state="complete" if all_ok else "error")

        st.markdown("---")
        for dest, res in log.items():
            if res["success"]: st.success(f"**{dest}** — {res['message']}")
            else:              st.error(f"**{dest}** — {res['message']}")
