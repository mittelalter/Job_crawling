import requests
from bs4 import BeautifulSoup

URL = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"


def extract_job_infos():
    count = 0
    jobs = []
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    company_infos = soup.select("li.feature")
    for info in company_infos:
        count += 1
        print(f"extracting...{count}")
        company = info.select_one("span.company").get_text()
        title = info.select_one("span.title").get_text()
        location = info.select_one("span.region.company").get_text()
        jobs.append([company, title, location])

    return jobs


def get_job_infos():
    job_infos = extract_job_infos()

    return job_infos
