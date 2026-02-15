import yt_dlp
import datetime



def filter(info_dict, *, incomplete):
    if incomplete:
        return None
    duration = info_dict.get('duration') or 0
    view=info_dict.get('view_count') or 0 
    sub=info_dict.get('channel_follower_count') or 1
    
    ratio=view/sub

    if duration > 60:
        return 'too long, get out'
    if ratio >= 1.5:
        return None 
    return 'too niche bruv remove'

#elib- C:\Program Files\nodejs\node.exe


node=r'C:\Program Files\nodejs\node.exe'


ydl_opts= {
    'quiet': True, 
    'extract_flat': False, 
    'skip_download':True,
    'match_filter': filter,
    'javascript_runtime': node,
    'sleep_interval': 3,
    'max_sleep_interval': 5, 
    'ignoreerrors': True,
    'search_sort':'date'
    #'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
}





def get_ytshorts(search):

    query= f"ytsearch100:{search} #shorts"
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        results = ydl.extract_info(query, download=False)
        if results is None:
            print("No results found.")
            return []

        shorts = results.get('entries', [])

        results=[]
        for i in shorts:

            #upload date to hours 
            udate= i.get('upload_date')
            if not udate:
                continue

            udatereal=datetime.datetime.strptime(udate, '%Y%m%d')
            udaterealreal= (datetime.datetime.now() - udatereal).total_seconds()/3600
            

            duration = i.get('duration') or 0
            views= i.get('view_count') or 0
            sub= i.get('channel_follower_count') or 1
            ratio=views/sub

            vph = views/udaterealreal

    
            print({
                'title': i.get('title'), 
                'id': i.get('id'),
                'url': f"https://youtube.com/watch?v={i.get('id')}", 
                'views': views,
                'duration': i.get('duration'),
                'sub': sub})

            if duration == 0 or duration > 60:
                continue

            if ratio>1.5 and duration<=60 and vph > 500:
                results.append(
                {
                'title': i.get('title'), 
                'id': i.get('id'),
                'url': f"https://youtube.com/watch?v={i.get('id')}", 
                'views': views,
                'duration': i.get('duration'),
                'sub': sub})

        return results
    





    
topthreeshorts=get_ytshorts(input('what you wanna look for?\t:'))



print("Top videos:\n")

for i in topthreeshorts:
    print(f"{i.get('title')}: {i.get('url')}, views: {i.get('views')}, duration: {i.get('duration')}, subs: {i.get('sub')}") #and virality ratio: {i.get('view_count')/i.get('channel_follower_count')}")