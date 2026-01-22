import yt_dlp


ydl_opts= {'quiet': True, 'extract_flat': True, 'force_generic_extractor': False, 'skip_download':True}

#https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D

def get_ytshorts():
    shorts_trending_url='https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D'
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        meta=ydl.extract_info(shorts_trending_url, download=False)

        
