import csv
import re
import json

def read_json_and_convert_to_csv():
    with open('imdb.json') as json_file:
        data = json.load(json_file)
    
    header = ['name', 'genre', 'summary', 'director', 'release_year', 'image_url']
    
    movie_rows = []

    for movie in data:
        genre =  movie['Genre']
        genre = genre.strip() if genre else None
        
        summary =  movie['Summary']
        summary = summary.strip() if summary else None
        
        if summary == 'Add a Plot':
            summary = None
        year = movie['Release_Year']
        year = re.sub(r"[a-zA-Z]+", "", year)
        movie_rows.append([
            movie['Name'].strip(),
            genre,
            summary,
            movie['Director'],
            year,
            movie['Image_url']
        ])
    
    with open('imdb.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(movie_rows)
            


read_json_and_convert_to_csv()




print("Hello World!!!")