import webbrowser
class Movie():
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_url=poster_image
        self.trailer_url=trailer_youtube
        self.showtrailer=webbrowser.open(self.trailer_url)
