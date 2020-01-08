**Welcome Python coder!**

In this repo, you'll find the following files:
  * Sample JSON files for Gracenote Music Metadata
    * Artist Metadata File: artist-object-1.json 
    * Album Metadata File: album-object-1.json
    * Recording Metadata File: recording-object-1.json 
  * Test Scripts
    * Python 2 version: test_script_python2.py (Removed 01/08/2020)
    * Python 3 version: test_script_python3.py
  * Skeleton Code
    * Python 2 version: Gracenote_music_data_python2.py (Removed 01/08/2020)
    * Python 3 version: Gracenote_music_data_python3.py

**Please run the test script on your machine to make sure you can run the `json` and `requests` libraries.**

There are 2 test scripts and skeleton files, one for Python2 and one for Python3.  To check which version of python you have installed, run the command `python --version`

Once you know what version of Python you have installed, clone the repo using: 

`git clone https://github.com/gracenote/python_meetup.git`

Then navigate to the directory:

`cd python_meetup`

Next, run the test script:

`python test_script_pythonX.py`   (where X = version of Python on your machine)

The output should look like this:

`Requests test result: True`

`Json test result: Taylor Swift`

Sample API Requests:

`https://api.gmd.music.gracenote.com/v1.0/artists/search?artistName=Taylor Swift&apikey=[KEY]`

`https://api.gmd.music.gracenote.com/v1.0/artists/gnid?ids=[GNID]&apikey=[KEY]`


Resources:

Requests Library: https://pypi.org/project/requests/2.7.0/

Info on RESTful APIs: https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f
