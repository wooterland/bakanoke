import requests
from bs4 import BeautifulSoup

url = "https://www.mangaupdates.com/series.html?id=1"
r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser')
desc = soup.find("b", text="Description").find_next("div").string
manga_type = soup.find("b", text="Type").find_next("div").string
rel_series = soup.find("b", text="Related Series").find_next("div").string
ass_names = soup.find("b", text="Associated Names").find_next("div")  # TODO Разобраться с наборов имен
g_scan = soup.find("b", text="Groups Scanlating").find_next("div")  # TODO Разобраться с сылками
last_release = soup.find("b", text="Latest Release(s)").find_next("div")  # TODO Разобраться с сылками
status = soup.find("div", text=" in Country of Origin").find_next("div").string
comp_scan = soup.find("b", text="Completely Scanlated?").find_next("div").string
anime_status = soup.find("b", text="Anime Start/End Chapter").find_next("div").string
genre = soup.find("b", text="Genre").find_next("div")  # TODO Разобраться с сылками
authors = soup.find("b", text="Author(s)").find_next("div")
artists = soup.find("b", text="Artist(s)").find_next("div")
year = soup.find("b", text="Year").find_next("div").string
publisher = soup.find("b", text="Original Publisher").find_next("div")
serialized = soup.find("b", text="Serialized In (magazine)").find_next("div")
licensed = soup.find("b", text="Licensed (in English)").find_next("div").string
eng_pub = soup.find("b", text="English Publisher").find_next("div")

print(eng_pub)
