import requests

async def search_lever():
    print("🔍 Searching Lever boards...")

    companies = [
        "https://jobs.lever.co/netflix",
        "https://jobs.lever.co/robinhood"
    ]

    jobs = []

    for company in companies:
        try:
            r = requests.get(company)
            if "DevOps" in r.text:
                jobs.append({
                    "platform": "Lever",
                    "title": "DevOps Role",
                    "link": company
                })
        except:
            continue

    print(f"Lever: {len(jobs)} possible matches.")
    return jobs
