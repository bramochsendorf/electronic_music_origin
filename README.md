# electronic_music_origin
This repository harbors some scripts and analyses aimed at visualizing the origin of current electronic music. Is German techno truly the best? Which country harbors the most house talent? 

## Conclusions
The electro, techno, and house music charts are dominated by artists from Europe and the United States. I measure popularity by the amount of times each artist has been listened to on LastFM. After grouping this data by country, I infer that Electro and House music from France is most popular, whereas Belgium boasts the most popular Techno. Interestingly, the United States hosts the largest number of Electro and House talent, but these artists appear to be less popular on average. Whether this is because US House/Electro is upcoming, or artists in the US are less talented remains to be seen.   

NB: the popularity of Belgium Techno is caused because 'Scooter' is tagged in the LastFM database as a Techno artist (...). Neglecting this obvious misclassification, Germany has both the highest total plays and amount of top artists in Techno.

## Analysis
This analysis involves a cross-match between data from the LastFM and Musicbrainz APIs, some pandas data juggling, geocoding, and data visualization in Leaflet. 

### LastFM API results
I started by querying the LastFM API to obtain the 1000 top artist within a given music genre. For the sake of simplicity, I restricted myself to the 'Electro', 'Techno', and 'House' genres following my analysis on the evolution of electronic music (described in the electronic_music_evo repository). From this I obtained a list of top artists and the total amount that their songs have been played on LastFM, which is the measure of popularity. Code for this step is given in lastfm.py

### Cross-matching results from the LastFM and Musicbrainz APIs
LastFM does not offer info on the country-of-origin of each artist. Therefore, I cross-matched the LastFM API results to the Musicbrainz API through Musicbrainz Artist IDs (which are given by LastFM!). This allowed me to get a list of artists, their total playcount, and their country-of-origin (in ISO 3166-1 alpha-2 format). I also parsed city-of-origin when available, which could be used for interesting geocoding experiments. Code for these steps are given in musicbrainz.py

### Barcharts and plugging results into JSON data for Leaflet map
I then made some barchart plots by grouping the artists by country in pandas, plotting both the (1) amount of artists per country and (2) the total playcounts per country. Code and plots for are given in the IPython notebook plots_and_json_prep.ipynb. 

In this notebook, I also load JSON polygons for the entire world, and add three features to the JSON data: total LastFM plays for each country, normalized LastFM plays for each country (which I use to define the color palette for the Leaflet map), and the rank (i.e., number 1 for France in House and Electro) which is used for the pop-ups in the Leaflet map. I populate the JSON datafile with these results by matching both datasets on the ISO 3166-1 alpha-2 feature. 

### live Leaflet map
With the JSON world map in hand, I constructed a simple interactive map using Leaflet, where countries are color-coded by the popularity of Electro/House/Techno. The more red, the more popular music is from that given country! Click on the country to see its rank in a given genre (if listed). A link to the live version of the Electro popularity map is given below. Feel free to grab the source code and plot the equivalent house and techno maps, or grab the entire repository and repeat the analysis for 80's power ballads if that tickles your fancy!

https://bramochsendorf.github.io/electronic_music_origin/
