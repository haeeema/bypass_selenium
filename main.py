from indeed import extract_indeed_jobs
from wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
# open() : Built-in function, open or create file
# CSV : comma-separated-value, a format of a file
# "w" : only write mode
file.write("Position, Company, Location, URL\n")
# Write a column seperated by comma

for job in jobs:
    file.write(
        f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
