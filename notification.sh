#! /bin/bash

# terminal-notifier is a command-line tool to send macOS User Notifications, which are available on macOS 10.10 and higher.
# See https://github.com/julienXX/terminal-notifier
# To install on MacOS use 'homebrew': brew install terminal-notifier

if [ $1 -eq 0 ]; then
   status="The anime-downloader ran successfully. $2 was downloaded."
else
   status="There was an issue with anime-downloader."
fi

timestamp="Timestamp: $(date)"


terminal-notifier  -title "Anime-Downloader" \
                   -message "$status $(echo $'\r') $timestamp"  \
                   -open "file://$HOME/Library/CloudStorage/OneDrive-Personal/Movies/anipy-cli_output/download" \
                   -ignoreDnD
