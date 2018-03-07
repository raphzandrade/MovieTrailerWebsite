import media
import fresh_tomatoes

# creates the movie array for later use
movies = []

# creates the movie instance for 'Blade Runner'
# and append into the movies array created previously
movies.append(
    media.Movie(
        'Blade Runner',
        'placeholder',
        'https://cdn.shopify.com/s/files/1/0178/7345/products/IJ3341.jpeg?v=1491760596',
        'https://www.youtube.com/watch?v=t6GvGoNWuhw'))

# creates the movie instance for 'The Shape of Water'
# and append into the movies array created previously
movies.append(
    media.Movie(
        'The Shape of Water',
        'placeholder',
        'https://2.bp.blogspot.com/-5iaMlGi_cz8/Wbrt3ll2ebI/AAAAAAAA2ZM/8Sm-cgcFuPw3iLYE5HBWrbmbK-i4OMLuQCLcBGAs/s1600/shape_of_water.jpg',
        'https://www.youtube.com/watch?v=uiA4B5Y63IQ'))

# creates the movie instance for 'The lord of the Rings'
# and append into the movies array created previously
movies.append(
    media.Movie(
        'The Lord of the Rings: The Fellowship of the Ring',
        'placeholder',
        'https://www.movieartarena.com/imgs/lotr1final.jpg',
        'https://youtu.be/V75dMMIW2B4'))

# creates the movie instance for 'Princess Mononoke'
# and append into the movies array created previously
movies.append(
    media.Movie(
        'Princess Mononoke',
        'placeholder',
        'https://images-na.ssl-images-amazon.com/images/I/51Xl0K7PlUL.jpg',
        'https://youtu.be/4OiMOHRDs14'))

# creates the movie instance for 'Tekkonkinkreet'
# and append into the movies array created previously
movies.append(
    media.Movie(
        'Tekkonkinkreet',
        'placeholder',
        'https://img.fstatic.com/Yfe2gAuY1Q6F_NkXNfximYflzs8=/fit-in/290x478/smart/https://cdn.fstatic.com/media/movies/covers/2015/07/tekkonkinkreet_t9052.jpg',
        'https://youtu.be/W2ku5toXWFc'))

# call the fresh_tomatoes class to open the page with the movies on the array
fresh_tomatoes.open_movies_page(movies)
