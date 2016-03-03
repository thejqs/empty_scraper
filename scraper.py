#!usr/bin/env python

import urllib
import urllib2
from lxml import etree
import StringIO
import re


def open_url(url):
    '''
    checks the url to make sure it's valid and, if so,
    reads in the html
    '''
    click = urllib.urlopen(url)
    if click.getcode() == 200:
        html = click.read()
        return html
    else:
        raise Exception("Nice try. Bad link.")


def parse_html(html):
    '''
    the initial parse of the html
    '''
    parser = etree.HTMLParser()
    return etree.parse(StringIO.StringIO(html), parser)


def treeify(url):
    '''
    gets the parsed tree to begin the scrape
    '''
    html = PDFScraper.open_url(url)
    return PDFScraper.parse_html(html)


def start_scrape():
    '''
    runs the functions to do the damn thang
    '''
    # your code here.




