from extract_wework import get_job_infos
from save_as_csv import save_as_csv_file


job_infos = get_job_infos()
csv_file = save_as_csv_file(job_infos)

print(csv_file)
