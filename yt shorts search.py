import yt_dlp


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





ydl_opts= {
    'quiet': True, 
    'extract_flat': False, 
    'skip_download':True,
    'match_filter': filter,
    'javascript_runtime': 'node',
    #'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
}





def get_ytshorts(search):

    query= f"ytsearch19:{search}"
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        results = ydl.extract_info(query, download=False)
        if results is None:
            print("ts empty bro yt blocking yo ass")
            return []

        shorts = results.get('entries', [])

        results=[]
        for i in shorts:

            views= i.get('view_count')
            sub= i.get('channel_follower_count')
            ratio=views/sub

            if ratio>1.5:
                results.append(
                {
                'title': i.get('title'), 
                'id': i.get('id'),
                'url': f"https://youtube.com/watch?v={i.get('id')}", 
                'views': views,
                'duration': i.get('duration'),
                'sub': sub})

        return results
    





    
topthreeshorts=get_ytshorts(input('what you wanna look for twin?\t:'))






print("Top videos:\n")

for i in topthreeshorts:
    print(f"{i.get('title')}: {i.get('url')}, views: {i.get('views')}, duration: {i.get('duration')}, subs: {i.get('sub')}") #and virality ratio: {i.get('view_count')/i.get('channel_follower_count')}")