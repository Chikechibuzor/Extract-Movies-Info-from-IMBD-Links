import json

from bs4 import BeautifulSoup
import requests


IMDB_URL = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2019-01-01,2022-12-31&countries=ng&count=250&start={start}'



def get_movieinfo_from_imdb_dot_com(url):
    data = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    
    movie_cards = soup.find_all('div', attrs={'class': ["lister-item", "mode-advanced"]})

    for card in movie_cards:
        h3 = card.find('h3')
        Name = h3.find('a')
        div_with_id = card.find('div', attrs={'data-caller':"filmosearch"})
        Movie_id = div_with_id['data-tconst']
        Genre = card.find('span', attrs={'class': 'genre'})
        Summary = card.find_all('p', attrs={'class': "text-muted"})
        plot = Summary[1]
        Release_yr = card.find_all('span', attrs={'class': ["lister-item-year text-muted unbold"]})
        Release_yr = Release_yr[0].text
        Release_yr = Release_yr.replace("(", "")
        Release_yr = Release_yr.replace(")", "")
        Director = card.find('p', attrs={'class': ""})
        Director = Director.find('a')
        Directot_name = None
        if Director:
            Director_name = Director.text
        a = card.find('a')
        Image = card.find('img', attrs={'class': "loadlate"})

        single_info = {
            'Name': Name.text,
            'Genre': Genre.text if Genre else None,
            'Summary': plot.text,
            'Release_Year': Release_yr,
            'Director': Director_name,
            'Image_url': Image['loadlate'],
            'Movie_id': Movie_id
        }
        data.append(single_info)
    return data

def generate_data():
    data = []
    for i in range(0, 6):
        start =( 250 * i ) + 1

        url = IMDB_URL.format(start=start)
        page_data = get_movieinfo_from_imdb_dot_com(url)
        data.extend(page_data)

    json_object = json.dumps(data)
    with open("imdb.json", "w") as outfile:
        outfile.write(json_object)

generate_data()