import csv
from extract_wework import get_job_infos


def save_as_csv_file(job_infos):
    file = open("wework_job_infos.csv", "w")
    csv_writer = csv.writer(file)
    csv_writer.writerow(["company", "title", "location"])

    for info in job_infos:
        csv_writer.writerow(info)

    return
