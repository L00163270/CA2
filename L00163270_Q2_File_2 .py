# --------------------
# File      : .py
# Created   : 15-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

import requests
from bs4 import BeautifulSoup

URL = 'http://192.168.206.128'


def scrape_data():
    try:
        response = requests.get( URL )
        page_content = BeautifulSoup( response.content, "html.parser" )
        get_headers( page_content )
        get_countapache( page_content )
    except Exception as e:
        print( e )



def get_headers(web_response):
    page_title = web_response.find( "title" ).text
    print( page_title )
""" Function is to find title of the page"""


def get_headlines(web_response):
    page_title = web_response.find_all( "h2" ).text
    print( page_title )
"""Function is  find header h2 in the page"""


def get_countapache(web_response):
    count = web_response.find_all( string=lambda text: "apache2" in text.lower() )
    print( "Apache2 appears {} times".format( len( count ) ) )

"""Function to find how many times Apache found in the page"""

if __name__ == '__main__':
    scrape_data()
