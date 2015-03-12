import media
import fresh_tomatoes

#create movie instances
toy_story = media.Movie('Toy Story',
                        "Toy's in a movie",
                        'http://imgs.abduzeedo.com/files/articles/toystory3/toystory3_35.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'New world',
                     'http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg',
                     'https://www.youtube.com/watch?v=_Tkc5pQp_JE')


pulp_fiction = media.Movie('Pulp Fiction',
                           'Killers on the move',
                           'http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg',
                           'https://www.youtube.com/watch?v=s7EdQ4FqbhY')


school_of_rock = media.Movie('School Of Rock',
                           'Rock and roll in school',
                           'http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                           'https://www.youtube.com/watch?v=37oJqWp4rJM')

#create array with movie instances
movies = [toy_story, avatar, pulp_fiction, school_of_rock]
#create html page
fresh_tomatoes.create_movie_tiles_content(movies)
#open html page
fresh_tomatoes.open_movies_page(movies)