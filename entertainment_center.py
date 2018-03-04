import media
import fresh_tomatoes

movies = []

movies.append(media.Movie('Blade Runner', 'placeholder', 'https://cdn.shopify.com/s/files/1/0178/7345/products/IJ3341.jpeg?v=1491760596',
                        'https://www.youtube.com/watch?v=t6GvGoNWuhw'))

movies.append(media.Movie('The Shape of Water', 'placeholder', 'https://2.bp.blogspot.com/-5iaMlGi_cz8/Wbrt3ll2ebI/AAAAAAAA2ZM/8Sm-cgcFuPw3iLYE5HBWrbmbK-i4OMLuQCLcBGAs/s1600/shape_of_water.jpg',
                        'https://www.youtube.com/watch?v=uiA4B5Y63IQ'))

movies.append(media.Movie('The Lord of the Rings: The Fellowship of the Ring', 'placeholder', 'https://www.movieartarena.com/imgs/lotr1final.jpg',
                        'https://youtu.be/V75dMMIW2B4'))

movies.append(media.Movie('Princess Mononoke', 'placeholder', 'https://images-na.ssl-images-amazon.com/images/I/51Xl0K7PlUL.jpg',
                        'https://youtu.be/4OiMOHRDs14'))

movies.append(media.Movie('Tekkonkinkreet', 'placeholder', 'https://img.fstatic.com/Yfe2gAuY1Q6F_NkXNfximYflzs8=/fit-in/290x478/smart/https://cdn.fstatic.com/media/movies/covers/2015/07/tekkonkinkreet_t9052.jpg',
                        'https://youtu.be/W2ku5toXWFc'))




fresh_tomatoes.open_movies_page(movies)
