#!/bin/bash

cwd=$(pwd)
dir="$cwd/sounds"
url="https://www.youtube.com/playlist?list=PLQiRgzVlXihT6MSiJco1DDyBpLkL5Z4Cx"
ext="mp3"


# Create output directory
echo "Prepare './sounds' directory."
mkdir -p "$dir"


# Download
echo "Download musics from YouTube. URL is $url"
yt-dlp --concurrent-fragments 3 --paths "$dir" --no-windows-filenames --extract-audio --audio-format "$ext" -f bestaudio "$url"


# Renaming downloaded files
echo "Renaming..."
## Debug(printf)
#find "$dir" -name "*.$ext" | awk '{ printf "mv \"%s\" '"$dir"/'%d.'$ext'\n", $0, NR }'
## Rename
find "$dir" -name "*.$ext" | awk '{ printf "mv \"%s\" '"$dir"/'%d.'$ext'\n", $0, NR }' | sh
sleep 3


# Create songs list
echo "Create songs list..."
find "$dir" -name "*.$ext" | sed -e "s|$dir/||g" | awk '{print "file '\''"$0"'\''"}'  > "${dir}/list.txt"
sleep 3
files=$(find "$dir" -name "*.$ext")


# Concat songs
echo "Concat the songs..."
ffmpeg -f concat -i "${dir}/list.txt" -c copy "${dir}/music.$ext" -safe 0


# Cleaning
echo "Cleaning up..."
echo "$files" | awk '{print "\""$0"\""}' | xargs rm
sleep 3

## Complete
echo "Finish"