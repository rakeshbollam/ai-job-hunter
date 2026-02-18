import requests

async def search_greenhouse():
    print("🔍 Searching Greenhouse boards...")
    boards = [
        "https://boards.greenhouse.io/stripe",
        "https://boards.greenhouse.io/airbnb"
    ]

    jobs = []

    for board in boards:
        try:
            r = requests.get(board)
            if "DevOps" in r.text:
                jobs.append({
                    "platform": "Greenhouse",
                    "title": "DevOps Role",
                    "link": board
                })
        except:
            continue

    print(f"Greenhouse: {len(jobs)} possible matches.")
    return jobs
