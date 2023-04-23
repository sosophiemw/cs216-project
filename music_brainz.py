



import requests
import musicbrainzngs as mbz 
# https://musicbrainz.org/doc/MusicBrainz_API
# https://musicbrainz.org/doc/MusicBrainz_API/Examples
# https://realpython.com/api-integration-in-python/


# https://python-musicbrainzngs.readthedocs.io/en/latest/api/

# REST API data access 
api_url = 'https://musicbrainz.org/ws/2/'

req1 = 'https://musicbrainz.org/ws/2/area/45f07934-675a-46d6-a577-6f8637a411b1?inc=aliases'
req2 = 'https://musicbrainz.org/ws/2/artist/all?fmt=json'
req3 = 'https://musicbrainz.org/ws/2/area/db325bd7-ae64-40bd-966a-a3af3cef8bb9?fmt=json'
req4 = api_url + 'area?query=california&fmt=json'
req5 = api_url + 'artist'

response = requests.get(req4)

# print(response.text)


# musicbrainzngs.browse_places(area=None, includes=[], limit=None, offset=None)¶

#Python bindings
app = "RecordIndustry.io"
version = "0.1"
mbz.set_useragent(app, version, contact=None)
result = mbz.search_artists(artist="Queen", type="group",
                                       country="California")
#result2=musicbrainzngs.browse_places(area=None, includes=[], limit=None, offset=None)

for artist in result['artist-list']:
    print(u"{id}: {name}".format(id=artist['id'], name=artist["name"]))
