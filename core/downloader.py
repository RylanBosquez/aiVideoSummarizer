import os
import re
import yt_dlp

def downloadAudio(videoTitle: str, url: str, outputPath: str):
    
    os.makedirs(outputPath, exist_ok=True)

    # Use sanitized title for output template
    ydl_opts_download = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(outputPath, f"{videoTitle}.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://vimeo.com/848863798"
    outputPath = "./assets/audios"
    downloadAudio(url, outputPath)
