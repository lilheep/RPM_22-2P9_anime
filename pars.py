import requests
from bs4 import BeautifulSoup
from models import Anime, Genres, Years, Photo

def get_anime(url):
    """Запись всех аниме"""
    for i in range(129):
        url1 = url + "&page=" + str(i+1)
        req = requests.get(url1, timeout=10)
        scr = req.text
        soup = BeautifulSoup(scr, 'html.parser')
        
        all_anime_title = soup.find_all(attrs={'class':'h5 font-weight-normal mb-1'})
        all_anime_genres = soup.find_all(attrs={'class':'anime-genre d-none d-sm-inline'})
        all_anime_years = soup.find_all(attrs={'class':'anime-year mb-2'})
        all_anime_photo = soup.find_all('div', class_='anime-list-lazy')
        # Создаем списки для хранения жанров и годов
        
        # Создаем записи для аниме
        for title, genre, year, photo in zip(all_anime_title, all_anime_genres, all_anime_years, all_anime_photo):
            item_link = title.find("a").get('href')
            name_anime = title.text.strip()
            photo = photo['data-original']
            genres, _ = Genres.get_or_create(Genre=genre.text.replace(' ','').replace(',',', '))
            years, _ = Years.get_or_create(Year=year.text.strip())
            photos, _ = Photo.get_or_create(PhotoUrl=photo)
            Anime.get_or_create(
                Anime=name_anime,
                Link=item_link,
                Genre=genres,
                Years=years,
                PhotoUrl=photos
            )
# Пример вызова функции
get_anime('https://animego.org/anime?sort=a.createdAt&direction=desc')