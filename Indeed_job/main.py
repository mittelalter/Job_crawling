from extract_indeed import extract_indeed_jobs, extract_pages

pages_to_extract = extract_pages()


extract_indeed_jobs(pages_to_extract)
