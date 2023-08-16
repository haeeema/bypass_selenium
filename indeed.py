from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="ecydgvn0")
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        options = Options()
        browser = webdriver.Chrome(options=options)
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        jobs_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = jobs_list.find_all("li", recursive=False)
        # Beautifulsoup find all of "li"
        # We only want to search for "li"s that are directly under ul tag.
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                # h2 = job.find("h2", class_="jobTitle")
                # a = h2.find("a")
                anchor = job.select_one("h2 a")
                title = anchor["aria-label"]
                link = anchor["href"]
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    "link": f"https://kr.indeed.com{link}",
                    "company": company.string,
                    "location": location.string,
                    "position": title,
                }
                results.append(job_data)
    return results
