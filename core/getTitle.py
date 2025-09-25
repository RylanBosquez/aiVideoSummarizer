import yt_dlp
import re

def getTitle(url: str) -> str:
    
    ydl_opts = {"quiet": True, "no_warnings": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        info_dict = ydl.extract_info(url, download=False)
        title = info_dict.get("title", "untitled")
    
    # Sanitize filename for Windows/Linux
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)  # remove illegal chars
    safe_title = safe_title.rstrip(". ")             # remove trailing dots/spaces
    return safe_title



if __name__ == "__main__":
    
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    title = getTitle(url)
    print(title)