 # -*- coding: utf-8 -*-

import requests
import json

def test_requests():
    """
    Sends a simple HTTP GET request
    :return: True if request succeeds, False if failure
    """
    resp = requests.get('http://www.google.com')
    return True if resp.status_code == 200 else False

def test_json():
    """
    Loads artist json and returns the artist name
    :return: artist name (in this example should be Beyoncé)
    """

    filename = 'artist-object-1.json'
    with open(filename) as fd:
        js = json.load(fd)

    artist_name = js[0]['artistName']['artistName']
    return artist_name

if __name__ == '__main__':
    print "Requests test result: ", test_requests()
    print "Json test result: ", test_json()