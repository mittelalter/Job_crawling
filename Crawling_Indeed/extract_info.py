import requests
from bs4 import BeautifulSoup
import csv


INDEED_URL = requests.get(
    "https://de.indeed.com/jobs?q=Data%20Analyst&l=Bonn&vjk=0016d1d7fcc6750b"
)


def extract_pages():
    """Extract the pages of Indeed"""

    soup = BeautifulSoup(INDEED_URL.text, "html.parser")
    pagination = soup.select_one("div.pagination")
    if pagination.select("a"):
        pages = pagination.select("a")

    page_list = []

    # Extract the pages
    for page in pages:
        if page.select_one("span").get_text() != "":
            page_list.append(int(page.select_one("span").get_text()))

    return len(page_list) + 2


def extract_indeed_jobs(pages):
    """Extract the job information from each page"""

    csv_file = open("indeed_job_infos.csv", "w")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["job_title", "company"])

    job_infos = []

    # Extract the job information from the extracted pages
    for page in range(pages):
        detail_page = requests.get(
            f"https://de.indeed.com/jobs?q=Data%20Analyst&l=Bonn&start={page*10}&vjk=0016d1d7fcc6750b"
        )
        soup = BeautifulSoup(detail_page.text, "html.parser")
        if soup.select_one("#mosaic-provider-jobcards > ul"):
            result_list = soup.select_one("#mosaic-provider-jobcards > ul")

            for result in result_list.select("li"):
                some_list = []
                if result.select_one("td.resultContent"):
                    job_title = result.select_one("a").select_one("span").get_text()
                    company = result.select_one("span.companyName a")
                    if company is not None:
                        company = company.get_text()

                    csv_writer.writerow([job_title, company])
