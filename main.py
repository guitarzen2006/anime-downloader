import sys
from bcolors import bcolors
import csv_connector
import anipy_cli


def main():
    base_url = "https://gogoanime.gg"

    # Creates empty constructor class
    entry = anipy_cli.entry()
    
    # Retrieve Series Name, Episode Number, and Date from episode.csv
    csv = csv_connector.Csv_connector()
    series_csv_info = csv.search_series(input("Enter Series: "))
    series_name = None
    try:
        series_name = series_csv_info[0][0]
    except:
        print(f"{bcolors.FAIL}Series Not Found. Please Check Spelling.{bcolors.ENDC}")
        sys.exit(1)
    episode_number_list = []
    for ep in series_csv_info:
        episode_number_list.append(ep[1])


    # Query gogoanime.com for category links to build the download URL
    query_class = anipy_cli.query(series_name, entry)
    links_and_names = query_class.get_links()

    # Build Entry Class with Required Attributes
    entry.category_url = f"{base_url}"+(''.join(links_and_names[0]))
    entry.show_name = (''.join(links_and_names[1])).replace('\n','')
    entry.ep = series_csv_info[0][1]


    # Episode handler used to work with episode URLS, etc. 'entry' class must be updated with series_name and category_url
    ep_class = anipy_cli.epHandler(entry)
    entry = ep_class.gen_eplink()
    entry = ep_class.get_entry()

    # Extracting Video URL Extracting the video and emebed url is done with the videourl class, it takes an entry
    # that has to at least have ep_url filled.
    url_class = anipy_cli.videourl(entry, "best")
    # generate stream url (this also, automaticlly generates the embed url)
    entry = url_class.get_entry()
    url_class.stream_url()

    # Download a m3u8/mp4 link:
    dl_class = anipy_cli.download(entry, ffmpeg=True)
    # downloads a m3u8 or a mp4 link
    dl_class.download()

    print(entry)    
if __name__ == "__main__":
    main()
