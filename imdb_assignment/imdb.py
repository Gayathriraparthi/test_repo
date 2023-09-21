
# importing json module
import json

def read_json_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data

print(read_json_file("imdb_movies.json"))


