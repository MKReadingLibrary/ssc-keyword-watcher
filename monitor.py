import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Config
URL = "https://sscnr.nic.in/newlook/site/ResultPhaseXI_2023_Examination.html"
KEYWORD = "NR16323"
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message():
    message = f"✅ Keyword '{KEYWORD}' found on the SSC NR website!"
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(telegram_url, data=payload)
        if response.ok:
            print("Message sent!")
        else:
            print("Failed to send message:", response.text)
    except Exception as e:
        print("Telegram error:", e)

def main():
    try:
        response = requests.get(URL, verify=False, timeout=20)
        if KEYWORD in response.text:
            send_telegram_message()
        else:
            print("Keyword not found.")
    except Exception as e:
        print("Error fetching:", e)

if __name__ == "__main__":
    main()
