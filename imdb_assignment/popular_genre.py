from imdb import read_json_file

def popular_genere_watched_by_most(file_name):
    data = read_json_file(file_name)
    
    from collections import defaultdict

    genre_count = defaultdict(int)

    for i in data:
        genre_count[tuple(i["genre"])] += 1

    popular_genre = max(genre_count.items(),key = lambda x:x[1])[0]

    return(f"The popular genere watched by most of the audience is {popular_genre}")

print(popular_genere_watched_by_most('imdb_movies.json'))