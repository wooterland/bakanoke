import requests
import re
from bs4 import BeautifulSoup


url = "https://www.mangaupdates.com/series.html?id=177979"
r = requests.get(url).content

soup = BeautifulSoup(r, 'html.parser')
cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


desc = soup.find("b", text="Description").find_next("div").string

manga_type = soup.find("b", text="Type").find_next("div").string

rel_series = soup.find("b", text="Related Series").find_next("div").string

ass_names = soup.find("b", text="Associated Names").find_next("div").get_text("<br>").split("<br>")
del ass_names[-1]

status = soup.find("div", text=" in Country of Origin").find_next("div").string

complete_scan = soup.find("b", text="Completely Scanlated?").find_next("div").string

anime_status = soup.find("b", text="Anime Start/End Chapter").find_next("div").string

genre = soup.find("b", text="Genre").find_next("div").get_text("<u>").split("<u>")
for i in range(1, len(genre)):
    del genre[i]
    if i == len(genre):
        break
del genre[-1]


authors = soup.find("b", text="Author(s)").find_next("div").get_text("<u>").split("<u>")
print(authors)

artists = soup.find("b", text="Artist(s)").find_next("div").get_text("<u>").split("<u>")
del artists[-1]

year = soup.find("b", text="Year").find_next("div").string

pub = soup.find("b", text="Original Publisher").find_next("div").get_text("<u>")
pub = cleaner.sub('', pub)

serialized = soup.find("b", text="Serialized In (magazine)").find_next("div").get_text("<u>")
serialized = cleaner.sub('', serialized)

licensed = soup.find("b", text="Licensed (in English)").find_next("div").string

eng_pub = soup.find("b", text="English Publisher").find_next("div").get_text("<u>")
eng_pub = cleaner.sub('', eng_pub)
