import os
import requests
import smtplib
from email.mime.text import MIMEText

URL = "https://sscnr.nic.in/newlook/site/ResultPhaseXI_2023_Examination.html"
KEYWORD = "NR13123"

FROM_EMAIL = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = FROM_EMAIL

def send_email():
    msg = MIMEText(f"🔎 Keyword '{KEYWORD}' found on the SSC results page!")
    msg["Subject"] = f"Alert: {KEYWORD} Found!"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(FROM_EMAIL, PASSWORD)
        smtp.send_message(msg)
    print("Email sent!")

def main():
    print("Checking webpage…")
    try:
        r = requests.get(URL, timeout=30)
        if KEYWORD in r.text:
            print("Keyword found!")
            send_email()
        else:
            print("Keyword not found.")
    except Exception as e:
        print("Error fetching:", e)

if __name__ == "__main__":
    main()
