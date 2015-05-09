#!/usr/bin/env python

# Akshay Srivatsan
# asrivat1@jhu.edu

# Usage: ./grab_info.py

from lxml.html import parse
from lxml.html import tostring
from collections import defaultdict
import re

startingURL = "http://engineering.jhu.edu/faculty/"
stopWordFileName = "common_words"
outputFileName = "bios"

def main():
    # read in stop words
    stopWords = readStop(stopWordFileName)

    # open output files
    output = open(outputFileName, "w")
    outputNames = open(outputFileName + "-names", "w")

    html = parse(startingURL).getroot()
    # make the links absolute for those that are local
    html.make_links_absolute(html.base_url, True)

    visited = defaultdict(lambda: 0)
    for element, attribute, link, pos in html.iterlinks():
        # find all faculty links on page, excluding redundant ones
        if startingURL in link and "#" not in link and startingURL != link and visited[link] == 0:
            # remeber the names as well
            outputNames.write(element.text_content() + "\n")
            grabInfo(link, stopWords, output)
            visited[link] = 1

    output.close()
    outputNames.close()

def grabInfo(link, stopWords, output):
    print link

    # find all words on the page
    html = parse(link).getroot()
    about = html.get_element_by_id("about", None)
    publications = html.get_element_by_id("publications", None)

    # it's possible this is not a faculty page
    if about is None or publications is None:
        return

    text = ""
    for chunk in about.itertext():
        text += " " + chunk
    for chunk in publications.itertext():
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
