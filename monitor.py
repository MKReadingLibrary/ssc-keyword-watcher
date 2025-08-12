import os
import requests
import urllib3
from datetime import datetime

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
RESULT_URL = "https://sscnr.nic.in/newlook/site/ResultPhaseXI_2023_Examination.html"
WHATS_NEW_URL = "https://sscnr.nic.in/newlook/site/Whatsnew.html"
KEYWORD = "NR13123"
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set these in your environment
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload)
        if response.ok:
            print("✅ Message sent!")
        else:
            print("❌ Telegram error:", response.text)
    except Exception as e:
        print("❌ Exception while sending message:", e)

def check_result_page():
    try:
        print("🔍 Checking result page...")
        response = requests.get(RESULT_URL, verify=False, timeout=20)
        if KEYWORD in response.text:
            message = (
                f"📢 *Result for {KEYWORD} has been published!*\n"
                f"[👉 Click here to view result]({RESULT_URL})"
            )
            send_telegram_message(message)
        else:
            print("❌ Keyword not found in result page.")
    except Exception as e:
        print("❌ Error fetching result page:", e)

def check_whats_new():
    try:
        print("🔍 Checking 'What's New' page...")
        response = requests.get(WHATS_NEW_URL, verify=False, timeout=20)
        content = response.text

        # SSC uses full month names, e.g., [12 August 2025]
        today = datetime.now().strftime("[%d %B %Y]")

        if today in content:
            message = (
                f"🆕 *New notice posted today ({today.strip('[]')})!*\n"
                f"[👉 Check 'What's New']({WHATS_NEW_URL})"
            )
            send_telegram_message(message)
        else:
            print(f"❌ No new notice for today ({today}).")
    except Exception as e:
        print("❌ Error fetching 'What's New' page:", e)

def main():
    check_result_page()
    check_whats_new()

if __name__ == "__main__":
    main()
