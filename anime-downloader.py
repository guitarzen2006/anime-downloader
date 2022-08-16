import os
from csv_connector import Csv_connector
from datetime import date

print("Starting anime-downloader.py")

csv_file = Csv_connector()

todays_date = date.today()

series_info = csv_file.search_date(todays_date)

if series_info == []:
    print("No anime today. Exiting...")
    os.sys.exit(0)

for series in series_info:
    series_name = series[0]
    docker_command = f"docker run --rm --mount type=bind,src=\"$(PWD)\",dst=/app/anipy-cli_output/download/ docker.io/guitarzen2006/anime-downloader:0.2 -L {series_name}"
    os.system(docker_command)