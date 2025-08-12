import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
URL = "https://sscnr.nic.in/newlook/site/ResultPhaseXI_2023_Examination.html"
KEYWORD = "NR13123"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message():
    message = (
        f"📢 *Result for {KEYWORD} has been published!*\n"
        f"[👉 Click here to view result]({URL})"
    )
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
        print("❌ Exception:", e)

def main():
    try:
        print("🔍 Checking page...")
        response = requests.get(URL, verify=False, timeout=20)
        if KEYWORD in response.text:
            send_telegram_message()
        else:
            print("❌ Keyword not found.")
    except Exception as e:
        print("❌ Error fetching:", e)

if __name__ == "__main__":
    main()
