import requests
from bs4 import BeautifulSoup

url = "https://www.mangaupdates.com/series.html?id=1"
r = requests.get(url).content

soup = BeautifulSoup(r, 'html.parser')

desc = soup.find("b", text="Description").find_next("div").string

manga_type = soup.find("b", text="Type").find_next("div").string

rel_series = soup.find("b", text="Related Series").find_next("div").string

ass_names = soup.find("b", text="Associated Names").find_next("div").get_text("<br>").split("<br>")
del ass_names[-1]

status = soup.find("div", text=" in Country of Origin").find_next("div").string

complete_scan = soup.find("b", text="Completely Scanlated?").find_next("div").string

anime_status = soup.find("b", text="Anime Start/End Chapter").find_next("div").string

genre = soup.find("b", text="Genre").find_next("div").get_text("<u>").split("<u>")  # TODO Разобраться с лишними элементами в списке

authors = soup.find("b", text="Author(s)").find_next("div")  # TODO Разобраться с сылками

artists = soup.find("b", text="Artist(s)").find_next("div")  # TODO Разобраться с сылками

year = soup.find("b", text="Year").find_next("div").string

pub = soup.find("b", text="Original Publisher").find_next("div")

serialized = soup.find("b", text="Serialized In (magazine)").find_next("div")

licensed = soup.find("b", text="Licensed (in English)").find_next("div").string

eng_pub = soup.find("b", text="English Publisher").find_next("div")

print(genre)
'''
print(desc)
print(manga_type)
print(rel_series)
print(ass_names)
print(g_scan)
print(last_release)
print(status)
print(comp_scan)
print(anime_status)
print(genre)
print(authors)
print(artists)
print(year)
print(pub)
print(serialized)
print(licensed)
print(eng_pub)
'''

