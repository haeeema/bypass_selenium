from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

options = Options()

browser = webdriver.Chrome(options=options)

browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source, "html.parser")
jobs_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = jobs_list.find_all("li", recursive=False)
# Beautiful find all of "li"
# We only want to search for "li"s that are directly under ul tag.
results = []
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
for result in results:
    print(result, "\n/////////////\n")
