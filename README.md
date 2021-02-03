# Spotify-charts-to-youtube-csv

You can find any charts at : https://spotifycharts.com/regional

Once you downloaded your chart, just put the csv file in the project's folder

Modify the 6th line of `script.py` so the variable fname is the name of your file (don't put the extension)

Run the `script.py` wait for a kinda long period depending of your file size.
You'll always get a youtube video-id even if it fails (it will try again until found -> youtube's api fault)

## Requirements

You need **python3 installed** and **youtube-search** package installed

You can easely install python3 on any os, no help is needed

For the **youtube-search** package, if you have pip just run `pip install youtube-search`

How to install pip ???  Go [there](https://pip.pypa.io/en/stable/) and good luck 

##
