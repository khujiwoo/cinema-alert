import os, json, re
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
from playwright.sync_api import sync_playwright

TARGETS = [('2026-11-11','CGV 왕십리','CGV_WANGSIMNI'),('2026-11-14','CGV 왕십리','CGV_WANGSIMNI'),('2026-11-11','롯데시네마 청량리','LOTTE_CHEONGNYANGNI'),('2026-11-14','롯데시네마 청량리','LOTTE_CHEONGNYANGNI')]

def notify(message):
    token, chat = os.getenv('TELEGRAM_BOT_TOKEN'), os.getenv('TELEGRAM_CHAT_ID')
    if not token or not chat:
        print('Telegram secrets not configured')
        return
    response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage',json={'chat_id':chat,'text':message},timeout=20)
    response.raise_for_status()

def check(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(locale='ko-KR', timezone_id='Asia/Seoul')
        try:
            page.goto(url, wait_until='domcontentloaded', timeout=45000)
            page.wait_for_timeout(3000)
            return page.locator('body').inner_text(timeout=15000)
        finally:
            browser.close()

def main():
    today = datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()
    for date, cinema, key in TARGETS:
        if date < today: continue
        env_name = f'URL_{key}_{date.replace("-", "_")}'
        url = os.getenv(env_name,'').strip()
        if not url:
            print(f'NOT CONFIGURED: {date} {cinema}: {env_name}')
            continue
        try:
            text = check(url)
            # Safety: generic seat counts do not prove a seat in the first screening.
            # Requires cinema-specific selectors/API validation before live alerting.
            print(f'PAGE LOADED: {date} {cinema}, {len(text)} characters. Seat parser not yet validated.')
        except Exception as e:
            print(f'CHECK FAILED: {date} {cinema}: {type(e).__name__}: {e}')

if __name__ == '__main__': main()
