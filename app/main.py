#! /usr/bin/env python3

import sys
import arg_parser as arg_parser
from bcolors import bcolors
import csv_connector as csv_connector
import anipy_cli


def main():
    base_url = "https://gogoanime.gg"
    # Creates empty constructor class
    entry = anipy_cli.entry()

    # Load argparse for argument handeling
    args = arg_parser.arguments()

    series_name = ' '.join(args.series_name)
    filename = args.file
    latest_episode = args.Latest
    episode_num = args.episode_num
    if episode_num != None:
        episode_num = args.episode_num[0]

    # File processing
    if filename != None:  # If file specified in argument
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
    # Series / Show Name required. 
    query_class = anipy_cli.query(series_name, entry)
    links_and_names = query_class.get_links()

    # Update Entry Class with Required Attributes (show_name, category_url, ep)
    entry.category_url = f"{base_url}"+(''.join(links_and_names[0]))
    entry.show_name = (''.join(links_and_names[1])).replace('\n','')
    entry.ep = episode_num

    # Episode handler used to work with episode URLS, etc. 'entry' class must be updated with series_name and category_url
    ep_class = anipy_cli.epHandler(entry)
    # Get latest episode of series
    if latest_episode:
        entry.ep = ep_class.get_latest()
    # else:
    #     entry.ep = episode_num
    # generate ep link, returns a entry
    entry = ep_class.gen_eplink()

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

if __name__ == "__main__":
    main()
