import glob
import os
import subprocess

import yt_dlp

URL = ["https://www.youtube.com/playlist?list=PLQiRgzVlXihT6MSiJco1DDyBpLkL5Z4Cx"]
opt_y = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}


def main():
    # Download
    try:
        with yt_dlp.YoutubeDL(opt_y) as ydl:
            err = ydl.download(URL)
    except Exception:
        pass

    # Change name
    # files = glob.glob('./*.m4a')
    # wd = os.getcwd()
    # amount = len(files)
    # renamed = []
    # print('Detected {} files'.format(amount))
    # for i in range(amount):
    #     name = os.path.join(wd, f'{i}.m4a')
    #     os.rename(files[i], name)
    #     renamed.append(name)
    #
    # # Export filenames
    # with open('list.txt', "w") as f:
    #     for name in renamed:
    #         print(f"file {name.replace('./', '')}", file=f)

    # Concat all files
    # subprocess.run(['ffmpeg', '-f', 'concat', '-i', 'list.txt', '-c', 'copy', 'music.webm'])

    # なんかBashで書いたコマンドをPythonで書き直す気が失せたのでコマンドに頼ります。
    os.system('find -name "*.m4a" | sed "s/.\\///" | awk \'{print "file " $0 ""}\' > list.txt')
    os.system('ffmpeg -f concat -i list.txt -c copy music.webm')


if __name__ == '__main__':
    main()
