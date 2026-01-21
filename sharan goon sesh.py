from instaloader import Profile
import instaloader
import time, random
from datetime import datetime, timedelta


SESSION_ID= '77373578060%3AM2L2tGN3ALdAcu%3A19%3AAYi0h2h8UTxKW9wyU0vIy8CbsBMcVoRWG8X1kWIG3g'



cutoff_date= datetime.now() - timedelta(hours=1460)

M= instaloader.Instaloader()

M.load_session_from_file('Sophoz07')
count=0
target='shhharran'


for post in Profile.from_username(M.context, target).get_posts():
    if not post.is_video:
        print('downloading goon material! 👅')
        M.download_post(post, target)
        count+=1
        waittime=random.randrange(10,17)
        print(f"waiting {waittime} seconds")
        time.sleep(waittime)

    elif count>1:
        print('enough gooning nga, stop!')








#all posts upto 2 months
'''
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
'''
    
    