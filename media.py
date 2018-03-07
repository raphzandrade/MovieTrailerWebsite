import webbrowser


class Movie():
    """ Class used to create movie instances """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Constructor fot the class Movie

        :param title: string
        :param storyline: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This method opens the trailer on a new web browser window.
        """
        webbrowser.open(self.trailer_youtube_url)
