import urllib.request
import csv
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://www.imdb.com/chart/top'


def download_page(url):
    return urllib.request.urlopen(url)

# tbody : table body ; tr: table row 

def parse_html(html):
    soup = BeautifulSoup(html)
    movie_table_soup = soup.find('tbody', attrs={'class': 'lister-list'})
    movie_name_list = []
    for movie_row in movie_table_soup.find_all('tr'):
        detail = movie_row.find('td', attrs={'class': 'titleColumn'})
        movie_name = detail.find('a').string
        movie_actor = detail.find('a')["title"]
        movie_actor.strip('"')
        # print(movie_name)
        # print (movie_actor)
        year = detail.find(
            'span', attrs={'class': 'secondaryInfo'}).string.strip('()')
        # print(year)

        rating_detail = movie_row.find(
            'td', attrs={'class': 'ratingColumn imdbRating'})
        rating = rating_detail.find('strong').string
        # print(rating)
        movie_name_list.append((movie_name, year, rating, movie_actor))
    return movie_name_list


def main():
    url = DOWNLOAD_URL
    # html = download_page(url)
    # parse_html(html)

    with open('imdb_top250.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        fields = ('name', 'year', 'rating', 'actors')
        writer.writerow(fields)

        html = download_page(url)
        movies = parse_html(html)
        writer.writerows(movies)

if __name__ == '__main__':
    main()
