#!/usr/bin/env python

# Akshay Srivatsan
# asrivat1@jhu.edu

# Usage: ./grab_info.py

from lxml.html import parse
from lxml.html import tostring
from lxml.html import document_fromstring
from collections import defaultdict
from urllib2 import Request
from urllib2 import urlopen
import re

startingURL = "http://store.steampowered.com/app/237930/?snr=1_300_307__307"
stopWordFileName = "common_words"
outputFileName = "games"

def main():
    # read in stop words
    stopWords = readStop(stopWordFileName)

    # open output files
    output = open(outputFileName, "w")
    outputNames = open(outputFileName + "-names", "w")

    # track what we've already seen
    visited = defaultdict(lambda: 0)
    visited[startingURL] = 1
    queue = [startingURL]

    while queue:
        # pop off a url and mark as visited
        url = queue.pop(0)

        # get the recommended titles section for links
        try:
            html = parse(url).getroot()
        except:
            continue

        # it's possible that this game is rated Mature
        # if so we aren't looking at the store page, but a form asking for our age
        # in this case we skip
        try:
            recommended = html.get_element_by_id("recommended_block")
        except:
            continue

        # make the links absolute for those that are local
        recommended.make_links_absolute(html.base_url, True)

        # get the info from this page
        grabInfo(url, stopWords, output, outputNames)

        # add the children to the queue
        recTitlesLinks = recommended.iterlinks()
        for link in recTitlesLinks:
            [queue.append(x) for x in getRecs(link[2], visited)]

    output.close()
    outputNames.close()

def getRecs(link, visited):
    similarLinks = []
    html = parse(link).getroot()
    similarItems = html.find_class("similar_grid_item")
    for item in similarItems:
        for element, attribute, link, pos in item.iterlinks():
            if "store.steampowered.com/app" in link and visited[link] == 0:
                similarLinks.append(link)
                visited[link] = 1
    return similarLinks

def grabInfo(link, stopWords, output, outputNames):

    # find all words on the page
    html = parse(link).getroot()
    # get the name of the game, removing non-ascii
    name = re.sub(r"[^\x00-\x7F]+", "", html.find_class("apphub_AppName")[0].text)
    print name
    outputNames.write(name + "\n")

    # it's possible that this game is rated Mature
    # if so we aren't looking at the store page, but a form asking for our age
    # in this case we skip
    if len(html.find_class("page_content")) <= 2:
        return

    # find the element that actually contains useful text
    html = html.find_class("page_content")[2]

    # grab just the alphabetic text
    text = ""
    for chunk in html.itertext():
        text += " " + chunk
    words = re.findall(r"[A-Za-z]{2,}", text)

    # remove stop words
    for word in words:
        word = word.lower()
        if stopWords[word] == 0:
            output.write(word + " ")
    output.write("\n")

def readStop(fileName):
    stopFile = open(fileName)
    stopWords = defaultdict(lambda: 0)
    for line in stopFile:
        line = line.strip()
        stopWords[line] = 1
    return stopWords

if __name__ == "__main__":
    main()
