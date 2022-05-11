from extract_SO.extract_so import get_job_infos
from extract_SO.save_as_csv import save_as_csv_file

job_infos = get_job_infos()
csv_file = save_as_csv_file(job_infos)

print(csv_file)
