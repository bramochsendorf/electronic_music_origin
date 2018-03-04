import pandas as pd
import numpy as np
import musicbrainzngs
import geo_nomi

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
"https://github.com/bramochsendorf",)

genre = 'electro'

# load in data
df = pd.read_pickle('/data1/python/data_science/lastfm/topartists_'+genre)
# limit to certain range?
#df = df.iloc[0:2]

# first we need to filter out all rows which do not have a musicbrainz artist ID 
a = df['mbid']
df = df[a.notnull()]

# obtain artist ids, initiate counter and open string with results
artist_id = df['mbid']
counter = 0
total = []

# now loop over all artist IDs
for art in artist_id:
    counter += 1
    print 'Loop = '+np.str_(counter)
    # get artist info from the API (through artist ID)
    try:
        result = musicbrainzngs.get_artist_by_id(art)
        name = result['artist']['name']
        
        try:
            # if 'begin area' is known, grab that. else, just higher level 'area'
        
            if 'begin-area' in result['artist'] and result['artist']['begin-area']['name'] is not None:
                a = result['artist']['begin-area']['name'] 
                
            elif result['artist']['area']['sort-name'] is not None:
                a = result['artist']['area']['sort-name']
                
            elif result['artist']['area']['name'] is not None:
                a = result['artist']['area']['name']
        
            city = a
            
        # if all else fails, return an empty sring
        except:
            city = ''
            
        # grab country, else return an emptry string.
        try:
            country = result['artist']['country']
        except:
            country = ''

        # now lat/lon
        # print city, country
        try:
            lat, lon =  geo_nomi.geo(city,country)
        except:
            lat = ''
            lon = ''
        
        print lat,lon
        # now begin date
        try: 
            if 'begin' in result['artist']['life-span'] and result['artist']['life-span']['begin'] is not None:
                begin = result['artist']['life-span']['begin']
        except:
            begin = ''
            
        
        # total info is city + country + begin
        print name, city, country, begin, lat, lon
        
        info = name+'|'+city+'|'+country+'|'+begin+'|'+np.str_(lat)+'|'+np.str_(lon)
    
        total += [info.split("|")]
    
    except:
        total += [['','','','','','']]
      
# create dataframe
df2 = pd.DataFrame(total, columns=["name","city","country","birth","lat","lon"])

# save the data?
df2.to_pickle('data/latlon_'+genre)