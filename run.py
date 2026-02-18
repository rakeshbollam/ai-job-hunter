import asyncio
from scraper.indeed import search_indeed
from scraper.greenhouse import search_greenhouse
from scraper.lever import search_lever
import pandas as pd
from datetime import datetime

async def main():
    print("🚀 Searching jobs posted in last 24 hours...\n")

    indeed_jobs = await search_indeed()
    greenhouse_jobs = await search_greenhouse()
    lever_jobs = await search_lever()

    all_jobs = indeed_jobs + greenhouse_jobs + lever_jobs

    if not all_jobs:
        print("No jobs found.")
        return

    df = pd.DataFrame(all_jobs)
    df["scraped_at"] = datetime.now()

    df.to_csv("jobs_24hr_results.csv", index=False)

    print(f"\n✅ Found {len(all_jobs)} jobs.")
    print("Saved to jobs_24hr_results.csv")

if __name__ == "__main__":
    asyncio.run(main())
