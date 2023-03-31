import requests
import org.json.XML
import JSONObject
# https://musicbrainz.org/doc/MusicBrainz_API
# https://musicbrainz.org/doc/MusicBrainz_API/Examples
# https://realpython.com/api-integration-in-python/

# REST API data access 
api_url = 'https://musicbrainz.org/ws/2/'

req1 = 'https://musicbrainz.org/ws/2/area/45f07934-675a-46d6-a577-6f8637a411b1?inc=aliases'
response = requests.get(req1)
# print(response.json())

# response.raise_for_status()  # raises exception when not a 2xx response
# if response.status_code != 204:
#     print(response.json())

# JSONObject response = XML.toJSONObject("<XMLStringValue>");

# header('Content-Type: application/xml');

# $response=simplexml_load_string($response);