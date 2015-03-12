## Movie Trailer website

Create Movie class with movie_title, movie_storyline, poster_image, trailer_youtube

Create instances of Movie class

Send an array of movie classes to fresh_tomatoes.py which builds a web page then opens in.

- To use:

Simply download the project and run "python entertainment_center.py" in your command line
and watch your favorite trailers!

- To Edit:

1. create instances of Movie using this format:
    toy_story = media.Movie('Toy Story',
                            "Toy's in a movie",
                            'http://imgs.abduzeedo.com/files/articles/toystory3/toystory3_35.jpg',
                            'https://www.youtube.com/watch?v=KYz2wyBy3kc')

2. Create movies array with your instances of movies
3. call fresh_tomatoes.create_movie_tiles_content to create a html file
4. call open_movies_page(movies) to open the page with said movies array.