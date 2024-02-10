from operator import itemgetter
movie = {'name': 'Parasite', 'year': '2019'}

print(movie.keys())
print(movie.values())
print(movie.items())

copy_movies = movie.copy()
copy_movies['director'] = 'Bong Joon-ho'

for key, value in movie.items():
    print(key, value)

for key, value in copy_movies.items():
    print(key, value)

filmes_de_terror = [
    {"filme": "O Exorcista", "ano": 1973, "diretor": "William Friedkin"},
    {"filme": "O Iluminado", "ano": 1980, "diretor": "Stanley Kubrick"},
    {"filme": "A Hora do Pesadelo", "ano": 1984, "diretor": "Wes Craven"},
    {"filme": "O Sexto Sentido", "ano": 1999, "diretor": "M. Night Shyamalan"},
    {"filme": "O Chamado", "ano": 2002, "diretor": "Gore Verbinski"},
    {"filme": "Jogos Mortais", "ano": 2004, "diretor": "James Wan"},
    {"filme": "Atividade Paranormal", "ano": 2007, "diretor": "Oren Peli"},
    {"filme": "Arraste-me para o Inferno", "ano": 2009, "diretor": "Sam Raimi"},
    {"filme": "Invocação do Mal", "ano": 2013, "diretor": "James Wan"},
    {"filme": "Corra!", "ano": 2017, "diretor": "Jordan Peele"}
]

sorted_horror_movies = sorted(filmes_de_terror, key=itemgetter('ano'), reverse=True)
print(sorted_horror_movies)