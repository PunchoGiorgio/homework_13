from task_13_data import ganres, films_data
from itertools import chain
from pathlib import Path
import json
import csv
import os

dict_genres = json.loads(ganres)

for i in dict_genres['results']:
    os.makedirs('{}/{}'.format('film_genres', i['genre']), exist_ok=True)


columns = ['title', 'year', 'rating', 'type', 'genres']


main_val = []
for k in films_data:
    list_val = []
    for w in list(k.keys()):
        if 'title' in w:
            list_val.append(k['title'])
            list_val.append(k['year'])
            list_val.append(k['rating'])
            list_val.append(k['type'])

    main_val.append(list_val)

main_list_gen = []
for z in films_data:
    list_gen = []
    for f in z['gen']:
        list_gen.append(f['genre'])
    main_list_gen.append(list_gen)


res_list = [list(tup) for tup in zip(main_val, main_list_gen)]


for p in res_list:
    p[0].append(p[1])
    p.remove(p[1])


new_list = [list(chain(*l)) for l in res_list]
print(new_list)


for j in list(os.walk(os.getcwd() + '/film_genres'))[1:]:
    file_obj = Path(j[0] + '/{}.csv'.format('movie_info'))
    file_obj.touch()

    sort_genre = []
    sort_genre.insert(0, columns)
    for p in new_list:
        for g in p[4]:
            if g in j[0]:
                sort_genre.append(p)

                films_csv_file_1 = os.getcwd() + '/film_genres/{}/movie_info.csv'.format(g)
                new_file_obj_1 = open(films_csv_file_1, 'w', encoding='UTF-8')
                writer_1 = csv.writer(new_file_obj_1)
                writer_1.writerows(sort_genre)
                new_file_obj_1.close()
