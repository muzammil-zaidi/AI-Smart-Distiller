"""
sheets.py — Writes extracted data to Google Sheets via gspread.
"""
from datetime import datetime
from config import GOOGLE_SERVICE_ACCOUNT_JSON, GOOGLE_SHEET_NAME
from mock_mode import sheets_configured


def append_to_sheet(extracted: dict, source_snippet: str = "") -> dict:
    if not sheets_configured():
        return {
            "success": False,
            "message": "Google Sheets not configured. Add GOOGLE_SERVICE_ACCOUNT_JSON in config.py."
        }
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        creds = Credentials.from_service_account_file(
            GOOGLE_SERVICE_ACCOUNT_JSON, scopes=scopes
        )
        gc = gspread.authorize(creds)
        sh = gc.open(GOOGLE_SHEET_NAME)
        ws = sh.sheet1

        if not ws.get_all_values():
            ws.append_row(
                ["Timestamp", "Summary", "Tasks", "Deadlines", "Source Snippet"],
                value_input_option="USER_ENTERED",
            )

        tasks_str = " | ".join(extracted.get("tasks", []))
        deadlines_str = " | ".join(
            f"{d['date']}: {d['context']}" for d in extracted.get("deadlines", [])
        )
        row = [
            datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
            extracted.get("summary", ""),
            tasks_str,
            deadlines_str,
            source_snippet[:200],
        ]
        ws.append_row(row, value_input_option="USER_ENTERED")
        return {"success": True, "message": f"Row appended to '{GOOGLE_SHEET_NAME}' successfully."}
    except Exception as e:
        return {"success": False, "message": f"Google Sheets error: {str(e)}"}
