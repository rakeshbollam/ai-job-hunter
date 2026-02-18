import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

KEYWORD = os.getenv("KEYWORD", "DevOps Engineer")
LOCATION = os.getenv("LOCATION", "United States")
DAYS = os.getenv("DAYS_FILTER", "1")
MAX = int(os.getenv("MAX_RESULTS", "50"))

async def search_indeed():
    print("🔍 Searching Indeed...")
    url = f"https://www.indeed.com/jobs?q={KEYWORD.replace(' ','+')}&l={LOCATION.replace(' ','+')}&fromage={DAYS}"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    cards = soup.find_all("a", class_="jcs-JobTitle")[:MAX]

    for card in cards:
        title = card.text.strip()
        link = "https://www.indeed.com" + card.get("href")

        jobs.append({
            "platform": "Indeed",
            "title": title,
            "link": link
        })

    print(f"Indeed: {len(jobs)} jobs found.")
    return jobs
