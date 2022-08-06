import anipy_cli
import csv


# Retriev data from CSV
 with open('episode.csv', newline='') as f:
        episode_db = csv.reader(f)
        for row in episode_db:
            if row[2] == current_isoformat_date:
                #print(row[0],row[1],row[a2])
                anime_name = row[0]
                episode = row[1]


# Creates empty constructor class
entry = anipy_cli.entry(anime_name)

print(entry)