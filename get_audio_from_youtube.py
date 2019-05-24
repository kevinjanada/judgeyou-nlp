import os
import youtube_dl

VIDEO_URL = 'https://www.youtube.com/watch?v=6cgxSL926N8'


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(download):
    if download['status'] == 'finished':
        print('Done downloading, now converting ...')

def move_audio_file_to_directory(INFO_DICT, EXT, DIR):
    TITLE = INFO_DICT['title']
    UPLOADER = INFO_DICT['uploader']
    AUDIO_FILE = '{uploader} {title}.{ext}'.format(uploader=UPLOADER, title=TITLE, ext=EXT)
    if '/' in DIR == False:
        DIR += '/'
    os.rename(AUDIO_FILE, DIR + AUDIO_FILE)

YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        # 'preferredcodec': 'mp3',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': '%(uploader)s %(title)s.%(ext)s',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

ydl = youtube_dl.YoutubeDL(YDL_OPTS)
info_dict = ydl.extract_info(VIDEO_URL, download=False)

ydl.download([VIDEO_URL])
move_audio_file_to_directory(info_dict, 'wav', 'downloads/')
