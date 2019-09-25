# -*- coding: utf-8 -*-

import requests

"""Solutions file to be paired with the skeleton code in GRACENOTE_MUSIC_DATA.PY."""

api_key = "zRigsMpMcRUx34HoelY2nzVOkrfUNU2L"  # global static variable


# Command line example: python3 gracenote_music_data_solutions_py3.py


###################
# Artist Metadata #
###################


def artist_gn_id(artist_name):
    """Return the Gracenote ID for the artist Taylor Swift. First, use the artist text search functionality of the API
    to obtain a list of artist match results. Next, parse through the returned results to find the Gracenote ID
    ("artistID") of the artist object whose name exactly matches the string "Taylor Swift".
    Artist text search API endpoint: `/artists/search`
    Parameters to pass in: `artistName`, `apikey`

    :param artist_name: string containing the artist name to be searched on
    :returns: a string containing the Gracenote ID of the artist if successfully found, or None
    """
    artist_match_results = None

    # Using the `requests` library and the API key above, obtain a list of artist match results from the GMD API.
    r = requests.get(
        "https://api.gmd.music.gracenote.com/v1.0/artists/search?artistName={0}&apikey={1}".format(artist_name,
                                                                                                   api_key))

    # Check the request status code to see if the request succeeded. If it did, return the Gracenote ID of the returned
    # exact match. If it did not succeed or there was no exact match, return None.
    if r.status_code == 200:
        artist_search_json = r.json()
        for artist in artist_search_json["artists"]:
            response_artist_name = artist["artistName"]["artistName"]
            if artist_name == response_artist_name:
                artist_match_results = artist["artistID"]
                break

    return artist_match_results


def artist_metadata(artist_gn_id):
    """Send an API request to perform an artist lookup using Taylor Swift's GRACENOTE_ID. Print her name, most highly-
    weighted artist type (which is an artist descriptor), and a list of her genres.
    Artist API endpoint: `/artists/gnid`
    Parameters to pass in: `ids`, `apikey`

    :param artist_gn_id: string containing the artist's Gracenote ID
    :returns: None
    """
    # Using the `requests` library and the API key above, obtain the artist's metadata from the GMD API.
    r = requests.get(
        "https://api.gmd.music.gracenote.com/v1.0/artists/gnid?ids={0}&apikey={1}".format(artist_gn_id, api_key))

    # Check the request status code to see if the request succeeded. If it did, print the artist's name, type, and
    # genre(s). If it did not succeed, return.
    if r.status_code == 200:
        artist_json = r.json()[0]
        print("Artist name: ", artist_json["artistName"]["artistName"])

        types = artist_json["descriptors"]["artistTypes"]
        artist_types_dict = {}
        for t in types:
            artist_types_dict[t["genericName"]] = int(t["weight"])
        artist_type = max(artist_types_dict, key=artist_types_dict.get)
        print("Artist type: ", artist_type)

        genres = artist_json["descriptors"]["genres"]
        artist_genre_list = []
        for g in genres:
            artist_genre_list.append(g["genericName"])
        print("Artist genre(s): ", artist_genre_list)


##################
# Album Metadata #
##################


def album_metadata(album_gn_id):
    """Perform an album lookup for Taylor Swift's album "1989" using the album's Gracenote ID. Return a dictionary of
    the album's tracks, the keys being the track's ordinal and the values being the track name.
    Album API endpoint: `/albums/gnid`
    Parameters to pass in: `ids`, `apikey`

    :param album_gn_id: string containing the album's Gracenote ID
    :returns: a dictionary of tracks if album's metadata is successfully retrieved, else, an empty dictionary
    """
    tracks = {}

    # Using the `requests` library and the API key above, obtain the album metadata from the GMD API.
    r = requests.get(
        "https://api.gmd.music.gracenote.com/v1.0/albums/gnid?ids={0}&apikey={1}".format(album_gn_id, api_key))

    # Check the request status code to see if the request succeeded. If it did, return a dictionary of the album's
    # tracks. If it did not succeed, return an empty dictionary.
    if r.status_code == 200:
        album_json = r.json()[0]
        for t in album_json["tracks"]:
            tracks[t["ord"]] = t["trackName"]

    return tracks


######################
# Recording Metadata #
######################


def recording_metadata(recording_gn_id):
    """Perform a lookup for Taylor Swift's recording "Shake It Off" using the recording's Gracenote ID. Print the
    recording's name, a list of its top 3 moods, and the recording's duration in minutes and seconds, rounding to the
    nearest second. (Hint: it's provided as milliseconds in the API response.)
    Recording API endpoint: `/recordings/gnid`
    Parameters to pass in: `ids`, `apikey`

    :param recording_gn_id: string containing the recording's Gracenote ID
    :returns: None
    """
    r = requests.get(
        "https://api.gmd.music.gracenote.com/v1.0/recordings/gnid?ids={0}&apikey={1}".format(recording_gn_id, api_key))
    if r.status_code == 200:
        recording_json = r.json()[0]
        print("Recording name: ", recording_json["recordingName"])

        moods = recording_json["descriptors"]["moods"]
        rec_mood_list = []
        for i in range(3):
            rec_mood_list.append(moods[i]["genericName"])
        print("Top 3 recording moods: ", rec_mood_list)

        ms_duration = recording_json["duration"]

        # much simpler way to convert to minutes and seconds:
        # sec_duration = round((int(ms_duration) / 1000))
        # mins = int(sec_duration / 60)
        # secs = sec_duration % 60

        sec_duration = int(ms_duration[:-3])
        tenths_digit = int(ms_duration[-3:-2])
        if tenths_digit >= 5:
            sec_duration += 1

        mins, sec, incremental = 0, 0, 60
        while incremental < sec_duration:
            mins += 1
            incremental += 60
        sec = sec_duration - incremental + 60
        print("Duration: {0} mins {1} sec".format(mins, sec))


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. Though, feel free to comment out sections to only run the
# functions you have implemented.


def main():
    artist = "Taylor Swift"
    album_gn_id = "GNCVEF2FWXWB1YN"         # 1989
    recording_gn_id = "GNDA62WP0ZPAYQF"     # Shake It Off

    print("Obtaining artist metadata for artist {0}...".format(artist))
    artist_gracenote_id = artist_gn_id(artist)
    artist_metadata(artist_gracenote_id)

    print("Obtaining album metadata for Gracenote album {0}...".format(album_gn_id))
    res = album_metadata(album_gn_id)
    print(res)

    print("Obtaining recording metadata for Gracenote recording {0}...".format(recording_gn_id))
    recording_metadata(recording_gn_id)


if __name__ == "__main__":
    main()
