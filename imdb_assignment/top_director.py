from imdb import read_json_file

def top_dir_with_max_movies(file_name):
    data = read_json_file("imdb_movies.json")
    
    from collections import defaultdict

    dir_movie_count = defaultdict(int)

    for i in data:
        dir_movie_count[i["director"]] += 1

    top_director = max(dir_movie_count.items(),key = lambda x:x[1])
    return(top_director)

    #return(f"The top director is '{top_director[0]}' with maximum number of movies is {top_director[1]}")

print(top_dir_with_max_movies("imdb_movies.son"))