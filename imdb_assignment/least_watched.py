from imdb import read_json_file

def least_watched_movie_by_imdb_score(file_name):
    data = read_json_file(file_name)
    least_watched = min(data,key = lambda x:x['imdb_score'])
    return(f"The least watched movie is '{least_watched['name']}' and imdb score is {least_watched['imdb_score']}")


print(least_watched_movie_by_imdb_score('imdb_movies.json'))