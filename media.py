"""Media module to declare media classes"""

import webbrowser


class Movie():
    """Stores information about specified movie.

    Args:
        movie_title (str): Movie's title.
        movie_storyline (str): Movie's storyline summary.
        poster_image (str): URL of image file of movie's poster.
        trailer_youtube (str): URL of movie's trailer on youtube.
        movie_year (int): Year of movie's release.

    Attributes:
        title (str): Movie's title.
        storyline (str): Movie's storyline summary.
        poster_image_url (str): URL of image file of movie's poster.
        trailer_youtube_url (str): URL of movie's trailer on youtube.
        year (int): Year of movie's release.

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year

    def show_trailer(self):
        """Opens Movie's youtube trailer in browser window."""
        webbrowser.open(self.trailer_youtube_url)
