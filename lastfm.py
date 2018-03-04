import pandas as pd
import pylast

# authentication
API_KEY = "YOUR_API_KEY" 
API_SECRET = "YOUR_API_SECRET"

username = "YOUR_USERNAME"
password_hash = pylast.md5("YOUR_PASSWORD")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)
                  
tagname = "electro house"       
tag = network.get_tag(tagname)
top_techno = tag.get_top_artists(limit=1000)         

results = []
counter = 0
for item in top_techno:
    counter += 1
    print counter
    a = item[0]
    
    name = a.get_name()
    mbid = a.get_mbid()
    play = a.get_playcount()
    results += [[name,mbid,play]]
    
df = pd.DataFrame(results,columns=["name", "mbid","playcount"])

df.to_pickle('/data1/python/data_science/lastfm/topartists_'+tagname)






