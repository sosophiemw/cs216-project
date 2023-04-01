import requests
import musicbrainzngs as mbz 


mbz.set_useragent('TheRecordIndustry.io', '0.1')

artist_list = mbz.search_artists(query='Queen')['artist-list']

result = mbz.search_artists(ended="false", country="US")

#red_sovine = artist_list[0] 
#print(red_sovine)


#release_list = mbz.browse_releases(artist=red_sovine['id'])['release-list']
#print(release_list)

#phantom_309 = release_list[4] 
#cover_art_b = mbz.get_image(phantom_309['id'], coverid='front', size='500')

#print(red_sovine['life-span'])

"""
# https://musicbrainz.org/doc/MusicBrainz_API
# https://musicbrainz.org/doc/MusicBrainz_API/Examples
# https://realpython.com/api-integration-in-python/

# REST API data access 
api_url = 'https://musicbrainz.org/ws/2/'

req1 = 'https://musicbrainz.org/ws/2/area/45f07934-675a-46d6-a577-6f8637a411b1?inc=aliases'
response = requests.get(req1)
#print(response.text)

# area, artist, event, genre, instrument, label, place, recording, release, release-group, series, work, url

#req2= 'http://musicbrainz.org/artist/c0b2500e-0cef-4130-869d-732b23ed9df5'
req2= "https://musicbrainz.org/ws/2/genre/all/fmt=json "
response2 = requests.get(req2)
print(response2.text)


artistQuery = Object {
  created: "2023-03-31T20:30:09.335Z"
  count: 23
  offset: 0
  artists: Array(23) [Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, Object, …]
}

artistQuery = (await fetch("https://musicbrainz.org/ws/2/artist/?query=artist:queen%20AND%20country:GB%20AND%20NOT%20type:person&fmt=json")).json()
artists = artistQuery.artists
"""




