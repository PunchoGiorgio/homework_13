from awards_data import films_titles, films_awards
from pathlib import Path
import string
import os

movie_titles = []
for mov_names in films_titles["results"]:
    movie_titles.append(mov_names["title"])


if not os.path.isdir('Harry Potter'):
    os.mkdir('Harry Potter')


for letters in string.ascii_uppercase:
    for titles_dir in films_titles['results']:
        os.makedirs('{}/{}/{}'.format('Harry Potter', titles_dir["title"], letters), exist_ok=True)

awards_lists = films_titles['results']

count = 0
while count < len(movie_titles):
    awards_lists[count] = list(
        {'type': result_elem['type'], 'award_name': result_elem['award_name'], 'award': result_elem['award']}
        for awards_elem in films_awards
        for result_elem in awards_elem['results']
        if movie_titles[count] == result_elem['movie']["title"])

    count += 1


sorted_lists = []
for i in awards_lists:
    sorted_lists.append(sorted(i, key=lambda x: x['award_name']))

counter = 0
while counter < len(movie_titles):
    for sort_elem in sorted_lists[counter]:
        for walk_elem in list(os.walk(os.getcwd() + '\Harry Potter\{}'.format(movie_titles[counter]))):
            if sort_elem['award_name'][0] == walk_elem[0][-1]:
                file_obj = Path(walk_elem[0] + '/{}.txt'.format(sort_elem['award_name']))
                file_obj.touch()
                with open(file_obj, 'w', encoding='UTF-8') as f:
                    f.write('{}'.format(sort_elem['award']))

    counter += 1
