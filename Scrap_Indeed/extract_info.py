from types import NoneType
import requests
from bs4 import BeautifulSoup
import csv


INDEED_URL = (
    "https://de.indeed.com/jobs?q=Data%20Analyst&l=K%C3%B6ln&vjk=da9d978c3fc81d52"
)


def extract_pages():
    # extract how many pages there are.

    response = requests.get(INDEED_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    pages = soup.select_one("div.pagination").select("a span.pn")
    total_pages = pages[-2].get_text()

    return int(total_pages)


def extract_job_infos(pages):
    # extract the job infos

    job_infos = []

    for page in range(pages):
        print(f"Scrapping Indeed page{pages+1}")
        response = requests.get(INDEED_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.select_one("#mosaic-provider-jobcards > ul"):
            result_list = soup.select_one("#mosaic-provider-jobcards > ul")

            for result in result_list.select("li"):
                if result.select_one("td.resultContent"):
                    job_title = result.select_one("a span").get_text()
                    company = result.select_one("span.companyName a")
                    if company is not None:
                        company = company.get_text()

                        job_infos.append([job_title, company])

    return job_infos


print(extract_job_infos(1))


def get_job_infos():
    total_pages = extract_pages()
    job_infos = extract_job_infos(total_pages)

    return job_infos
