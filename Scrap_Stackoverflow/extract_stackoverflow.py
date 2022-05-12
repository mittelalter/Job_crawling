import requests
from bs4 import BeautifulSoup

""" Extract the job-infos from StackOverFlow """

URL = "https://stackoverflow.com/jobs/companies?q=python"
SO = "stackoverflow.com"


def extract_total_pages():

    """Extract Total Pages"""

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    pages = soup.select_one("div.s-pagination").select("a span")
    total_pages = pages[-2].get_text()

    print(total_pages)
    return int(total_pages)


def extract_job_infos(pages):
    """Extract Job Infos"""

    jobs = []
    for page in range(pages):
        print(f"Scraping Stack over flow: {page+1}")
        response = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(response.text, "html.parser")
        company_infos = soup.select("div.dismissable-company")
        for info in company_infos:
            title = info.select_one("a.s-link").get_text()
            location, description = (
                info.select_one("div.fs-body1").get_text(strip=True),
                info.select_one("div.fs-body1").get_text(strip=True),
            )

            link = f"{SO}" + info.select_one("a.s-link")["href"]
            jobs.append([title, location, description, link])

    return jobs


def get_job_infos():
    total_pages = extract_total_pages()
    job_infos = extract_job_infos(total_pages)

    return job_infos
