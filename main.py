from bs4 import BeautifulSoup

from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

options = Options()
'''
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
'''
# options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

browser.get(f"{base_url}{search_term}")

response = browser.last_request.response

if response.status_code != 200:
    print("Can't request page")
else:
    soup = BeautifulSoup(browser.page_source, "html.parser")
    jobs_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = jobs_list.find_all("li", recursive=False)
    # Beautifulsoup find all of "li"
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
