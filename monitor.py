import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = Bot(token=BOT_TOKEN)

async def check_ssc_updates():
    url = "https://ssc.gov.in/home/notice-board"
    today = datetime.now().strftime('%d-%m-%Y')

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        notices = soup.select("ul.list-unstyled li")

        for notice in notices:
            date_tag = notice.select_one('div.card-date span')
            title_tag = notice.select_one('div.card-content a')
            if not date_tag or not title_tag:
                continue

            notice_date = date_tag.text.strip()
            title = title_tag.text.strip()
            link = title_tag['href']
            full_link = f"https://ssc.gov.in{link}" if link.startswith('/') else link

            if notice_date == today:
                message = f"🆕 *SSC Notice* ({today}):\n*{title}*\n👉 [Click to view]({full_link})"
                await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
                return
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(check_ssc_updates())
