from imdb import read_json_file

def get_top_ten_movies_by_imdb_score(file_name):
    data = read_json_file(file_name)
    sorted_imdb_score = sorted(data,key = lambda x: x['imdb_score'],reverse = True)
    top_ten = [(i["name"],i["imdb_score"])for i in sorted_imdb_score[0:10]]
    return(f"The top ten movies, according to imdb score are {top_ten}")

print(get_top_ten_movies_by_imdb_score('imdb_movies.json'))