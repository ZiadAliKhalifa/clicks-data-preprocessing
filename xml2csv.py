import csv
import re
import xml.etree.ElementTree as ET

file = open('Input/news_articles.xml', 'r')
lines = file.readlines()
file = open('output.csv', 'w')
writer = csv.writer(file)

for line in lines:
    xml = ET.fromstring(line)

    id = xml.attrib.get('ID')
    title = xml.attrib.get('Title')
    story = xml.attrib.get('Story')

    title = re.sub('<[^>]+>|\"', '', title)
    story = re.sub('<[^>]+>|\"', '', story)

    writer.writerow([id, title, story])
