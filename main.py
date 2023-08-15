from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

options = Options()
# Specify your options here if needed, e.g., headless mode, user agent, etc.
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

browser = webdriver.Chrome(options=options)

browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source, "html.parser")
jobs_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = jobs_list.find_all("li", recursive=False)
# Beautiful find all of "li"
# We only want to search for "li"s that are directly under ul tag.
for job in jobs:
    print(job)
    print("//////////////")