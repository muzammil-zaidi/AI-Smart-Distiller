"""
webhook.py — Sends extracted JSON to n8n webhook (or simulates it in mock mode).
"""
import json
import time
from datetime import datetime
from config import N8N_WEBHOOK_URL
from mock_mode import is_mock_mode

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


def send_to_n8n(extracted_data: dict, targets: list) -> dict:
    """
    Sends structured JSON to n8n webhook.
    Returns a dict mapping each target to its HTTP status result.
    """
    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "targets": targets,
        "data": extracted_data
    }

    if is_mock_mode() or not REQUESTS_AVAILABLE:
        return _mock_send(payload, targets)
    else:
        return _real_send(payload, targets)


def _real_send(payload: dict, targets: list) -> dict:
    """Posts to the configured n8n webhook URL."""
    results = {}
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            timeout=10,
            headers={"Content-Type": "application/json"}
        )
        # n8n typically returns 200 for all targets in one call
        for target in targets:
            results[target] = {
                "status_code": response.status_code,
                "message": f"Data sent successfully to {target}." if response.status_code == 200
                           else f"Unexpected response: {response.text[:100]}"
            }
    except Exception as e:
        for target in targets:
            results[target] = {
                "status_code": 500,
                "message": f"Connection error: {str(e)}"
            }
    return results


def _mock_send(payload: dict, targets: list) -> dict:
    """Simulates a successful n8n webhook call."""
    time.sleep(0.3)  # simulate network latency
    messages = {
        "Google Sheets": "Row appended to 'AI Distiller Output' sheet (simulated).",
        "Discord":       "Notification posted to #ai-distiller channel (simulated).",
        "Email":         "Email dispatched to configured recipient (simulated)."
    }
    return {
        target: {
            "status_code": 200,
            "message": messages.get(target, "Data routed successfully (simulated).")
        }
        for target in targets
    }
