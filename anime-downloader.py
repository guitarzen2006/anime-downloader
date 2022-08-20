#!/Users/barryweiss/.pyenv/shims/python

import os
import subprocess  # Note to future self always use subprocess instead of os.system.
from csv_connector import Csv_connector
from datetime import date


def main():
    print("Starting anime-downloader.py")

    csv_file = Csv_connector()
    home_directory = os.environ.get('HOME')
    local_directory = f"{home_directory}/Library/CloudStorage/OneDrive-Personal/Movies/anipy-cli_output/download/"
    container_label = "0.2"
    todays_date = str(date.today())
    series_info = csv_file.search_date(todays_date)

    if series_info == []:
        print("No anime today. Exiting...")
        subprocess.run(["./notification.sh", "0", "Nothing"])
        os.sys.exit(0)

    for series in series_info:
        series_name = series[0]
        docker_command = f"""docker run --rm --mount type=bind,src={local_directory},dst=/app/anipy-cli_output/download/ \
                                docker.io/guitarzen2006/anime-downloader:{container_label} -L {series_name}"""
        command_output = subprocess.run(["bash", "-c", docker_command], capture_output=True)
        error_code = str(command_output.returncode)
        subprocess.run(["./notification.sh", error_code, f"\'{series_name}\'"])

if __name__ == '__main__':
    main()