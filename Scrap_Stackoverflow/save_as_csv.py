import csv


def save_as_csv_file(job_infos):
    file = open("Job_infos_from_SO.csv", "w")
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "location", "description", "link"])

    for info in job_infos:
        csv_writer.writerow(info)

    return "Scrapping done"
