from imdb import read_json_file

def get_best_director_in_first_hundred_movies(file_name):
    data = read_json_file(file_name)
    best_director = max(data[:100],key = lambda x:x['imdb_score'])
    return(f"The Best Director in the first hundred movies is '{best_director['director']}' and imdb score is {best_director['imdb_score']}")

print(get_best_director_in_first_hundred_movies('imdb_movies.json'))
