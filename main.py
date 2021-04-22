import requests
import re
from bs4 import BeautifulSoup

cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def get_local_page(manga_id):
    """Return local html file name"""
    url = f'https://www.mangaupdates.com/series.html?id={manga_id}'
    file_name = f'{manga_id}.html'
    r = requests.get(url).content
    with open(f'raw_data/{file_name}', 'wb') as f:
        f.write(r)
    return file_name

# TODO Done!
def manga_title(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        title = soup.find('title').get_text(strip=True)
        title = title.replace('Baka-Updates Manga - ', '')
    return title


# TODO Done?
def description(manga_id):
    """Return description. Found two types of description. Maybe they have more."""
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        desc = soup.find('div', id='div_desc_more')
        if desc:
            desc = soup.find('div', id='div_desc_more').get_text(strip=True)
            return desc
        if not desc:
            desc = soup.find('b', text='Description').find_next('div').get_text(strip=True)
            return desc


# TODO Done?
def manga_type(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        manga_type = soup.find('b', text='Type').find_next('div').get_text(strip=True)
    return manga_type


# TODO Done!
def related_series(manga_id):
    """Return list with related series"""
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        rel_ser = []
        soup = BeautifulSoup(f, 'html.parser')
        raw_u = soup.find('b', text='Related Series').find_next('div')
        for a in raw_u.find_all('a'):
            i = a.find('u').get_text(strip=True)
            rel_ser.append(i)
    return rel_ser


# TODO Done?
def associated_names(manga_id):
    """Return list with manga title on different languages"""
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        ass_names = soup.find('b', text='Associated Names').find_next('div').get_text('<br>').split('<br>')
        del ass_names[-1]
    return ass_names


# TODO Done?
def status(manga_id):
    """Return status."""
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        status = soup.find('div', text=' in Country of Origin').find_next('div').get_text(strip=True)
        if not status:
            status = 'Unknown'
    return status


# TODO Done!
def complete_scan(manga_id):
    """Return status about scanlete"""
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        comp_scan = soup.find('b', text='Completely Scanlated?').find_next("div").get_text(strip=True)
    return comp_scan


# TODO Done!
def anime_status(manga_id):
    """Return status about anime adaptation"""
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')
        anime = soup.find("b", text="Anime Start/End Chapter").find_next("div").get_text(strip=True)
    return anime


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


def get_manga(manga_id):
    with open(f'raw_data/{manga_id}.html', 'rb') as f:
        soup = BeautifulSoup(f, 'html.parser')

        manga = [{
            'manga_title': soup.find("title").get_text(strip=True).replace("Baka-Updates Manga - ", ""),
            #'description': soup.find("b", text="Description").find_next("div").get_text(strip=True),
            'manga_type': soup.find("b", text="Type").find_next("div").get("u"),
            'related_series': soup.find("b", text="Related Series").find_next("div").get_text( ),
            'associated_names': soup.find("b", text="Associated Names").find_next("div").get_text("<br>").split("<br>"),
            'status': soup.find("div", text=' in Country of Origin').find_next("div").get_text(strip=True),
            'complete_scan': soup.find("b", text="Completely Scanlated?").find_next("div").get_text(strip=True),
            'anime_status': soup.find("b", text="Anime Start/End Chapter").find_next("div").get_text(strip=True),
            'genre': soup.find("b", text="Genre").find_next("div").get_text("<u>").split("<u>"),
            'authors': soup.find("b", text="Author(s)").find_next("div").get_text("<u>").split("<u>"),
            'artists': soup.find("b", text="Artist(s)").find_next("div").get_text("<u>").split("<u>"),
            'year': soup.find("b", text="Year").find_next("div").get_text(strip=True),
            'publisher': soup.find("b", text="Original Publisher").find_next("div").get_text("<u>"),
            'serialized': soup.find("b", text="Serialized In (magazine)").find_next("div").get_text("<u>"),
            'licensed': soup.find("b", text="Licensed (in English)").find_next("div"),
            'eng_pub': soup.find("b", text="English Publisher").find_next("div").get_text(strip=True)
        }]
    return manga
