from instaloader import Profile
import instaloader
import time, random
from datetime import datetime, timedelta

cutoff_date= datetime.now() - timedelta(hours=1460)

M= instaloader.Instaloader()

M.load_session_from_file('Sophoz07')
count=0
target='shhharran'

for post in Profile.from_username(M.context, target).get_posts():
    if post.date_utc < cutoff_date:
        print('this all u get to goon twin, hop off.')
        break
    
    if count > 35:
        print('too many posts nga stop gooning')
        break
    
    if not post.is_video:
        print('downloading ts twin')
        M.download_post(post, target)
        count+=1
        waittime=random.randrange(10,17)
        print(f"waiting {waittime} seconds")
        time.sleep(waittime)
        
    else:
        print('skipping')

    
    
        
        

