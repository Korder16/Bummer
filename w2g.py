import json
import requests


def read_json(video_url: str) -> str:

    """ Read json request template """
    with open('request.json', 'r') as json_file:
        json_data = json.load(json_file)

    json_data['share'] = video_url
    return json_data


def create_room(video_url: str) -> str:

    """ Post a json request with video url within.
        Creates a Watch2Gether room and returns a link to it.
    """
    URL = 'https://w2g.tv/rooms/create.json'

    request = requests.post(URL, json=read_json(video_url))

    streamkey = request.json()['streamkey']

    url_to_room = f'https://w2g.tv/rooms/{streamkey}'
    return url_to_room
