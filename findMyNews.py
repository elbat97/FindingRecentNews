from bs4 import BeautifulSoup
import requests
import csv
page_link ='https://www.cp24.com/world'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where title of the news article is stored
storyTitle = page_content.find_all(class_='teaserTitle')
# This is the list that is going to store all the news data
strings2 = list()

# This is removing the tags and the extra whitespace to give just the string
for n in storyTitle:
    strings2.append(n.get_text().strip())

# Here we are putting all the data in a csv file for the user to observe
with open('news.csv', 'w') as csvFile:
    newFileWriter = csv.writer(csvFile, lineterminator = '\n')
    for n in strings2:
        newstr = list()
        newstr.append(n)
        newFileWriter.writerow(newstr)
csvFile.close()
