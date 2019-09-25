# -*- coding: utf-8 -*-

import requests

"""Gracenote's music data can be queried through an API which returns results in a JSON format. Our detailed data can be
used in a variety of end-user applications in creative ways. To experiment with Gracenote's music data API, please go 
through this guided skeleton code and fill in the relevant sections with your own code.

The API endpoints are relative to `https://api.gmd.music.gracenote.com/v1.0`
"""

api_key = "x4vXPRdWbfQIwh0oL4kZkHJ6onYsqqiA"        # global static variable


# Command line example: python3 gracenote_music_data_py3.py


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
    "*** YOUR CODE HERE ***"

    # Check the request status code to see if the request succeeded. If it did, return the Gracenote ID of the returned
    # exact match. If it did not succeed or there was no exact match, return None.
    "*** YOUR CODE HERE ***"

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
    "*** YOUR CODE HERE ***"

    # Check the request status code to see if the request succeeded. If it did, print the artist's name, type, and
    # genre(s). If it did not succeed or there was no exact match, return None.
    "*** YOUR CODE HERE ***"


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
    "*** YOUR CODE HERE ***"

    # Check the request status code to see if the request succeeded. If it did, return a dictionary of the album's
    # tracks. If it did not succeed, return an empty dictionary.
    "*** YOUR CODE HERE ***"

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
    # Using the `requests` library and the API key above, obtain the recording metadata from the GMD API.
    "*** YOUR CODE HERE ***"

    # Check the request status code to see if the request succeeded. If it did, print the recording's name, top 3 moods,
    # and duration in seconds. If it did not succeed, return.
    "*** YOUR CODE HERE ***"


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. Though, feel free to comment out sections to only run the
# functions you have implemented.


def main():
    artist = "Taylor Swift"
    album_gn_id = "GN73N9FGKZRW2P3"         # 1989
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
