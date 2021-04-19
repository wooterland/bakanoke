import requests
import re
from bs4 import BeautifulSoup

cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def get_page(manga_id):
    url = f'https://www.mangaupdates.com/series.html?id={manga_id}'
    file_name = f'{manga_id}.html'
    r = requests.get(url).content
    with open(f'raw_data/{file_name}', 'wb') as f:
        f.write(r)
    return file_name


def manga_title(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        title = soup.find("title").string
        title = title.replace("Baka-Updates Manga - ", "")
    return title


def description(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        desc = soup.find("b", text="Description").find_next("div").string
    return desc


def manga_type(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        manga_type = soup.find("b", text="Type").find_next("div").string
    return manga_type


def eelated_series(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        rel_series = soup.find("b", text="Related Series").find_next("div").string
    return rel_series


def associated_names(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        ass_names = soup.find("b", text="Associated Names").find_next("div").get_text("<br>").split("<br>")
        del ass_names[-1]
    return ass_names


def status(manga_id): # TODO
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        status = soup.find("div", text="Status in Country of Origin").find_next("div").string
    return status


def complete_scan(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        complete_scan = soup.find("b", text="Completely Scanlated?").find_next("div").string
    return complete_scan


def anime_status(manga_id): # TODO
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        anime_status = soup.find("b", text="Anime Start/End Chapter").find_next("div").string
    return anime_status


def genre(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        genre = soup.find("b", text="Genre").find_next("div").get_text("<u>").split("<u>")
        for i in range(1, len(genre)):
            del genre[i]
            if i == len(genre):
                break
        del genre[-1]
    return genre


def authors(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        authors = soup.find("b", text="Author(s)").find_next("div").get_text("<u>").split("<u>")
        del authors[-1]
    return authors


def artists(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        artists = soup.find("b", text="Artist(s)").find_next("div").get_text("<u>").split("<u>")
        del artists[-1]
    return artists


def year(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        year = soup.find("b", text="Year").find_next("div").string
    return year


def publisher(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        pub = soup.find("b", text="Original Publisher").find_next("div").get_text("<u>")
        pub = cleaner.sub('', pub)
    return pub


def serialized(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        serialized = soup.find("b", text="Serialized In (magazine)").find_next("div").get_text("<u>")
        serialized = cleaner.sub('', serialized)
    return serialized


def licensed(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        licensed = soup.find("b", text="Licensed (in English)").find_next("div").string
    return licensed


def eng_publisher(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        eng_pub = soup.find("b", text="English Publisher").find_next("div").get_text("<u>")
        eng_pub = cleaner.sub('', eng_pub)
    return eng_pub

print()